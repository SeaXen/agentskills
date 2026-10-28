#!/usr/bin/env python3
"""Capture README screenshots with Playwright, across browser engines.

Usage:
  python capture_screenshots.py --root <app_root> --url http://localhost:3000 \
      --route / --name home --out docs/screenshots [--width 1440] [--full-page]

  python capture_screenshots.py --root <app_root> --url http://localhost:3000 \
      --routes /,/pricing,/about --out docs/screenshots \
      --browsers chromium,firefox,webkit

Produces:
  <out>/<name>.png             full-page screenshot (single-browser runs)
  <out>/<name>-<browser>.png   per-browser screenshots (multi-browser runs)
  <out>/contact-sheet.png      grid of all captures (Pillow)
  <out>/manifest.json          machine-readable capture manifest (browsers,
                               routes, files, console errors) used as Gate A
                               evidence

Read-only against the app; writes only into --out.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, resolve_out_dir, resolve_root, root_error
import framework_profiles

BROWSERS = ("chromium", "firefox", "webkit")

# In --json mode stdout carries ONLY the JSON payload, so every progress
# message is routed to stderr.
_JSON_MODE = False


def log(message: str) -> None:
    """Progress output that never pollutes a JSON stdout stream."""
    print(message, file=sys.stderr if _JSON_MODE else sys.stdout)


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return s or "home"


def join_url(base: str, route: str) -> str:
    """Join a base URL with a route, handling http(s) and file:// bases."""
    base = base.rstrip("/")
    if route in ("", "/"):
        return base + "/" if base.startswith("http") else base
    if base.startswith("http"):
        return base + "/" + route.lstrip("/")
    # file:// or filesystem path
    return base.rstrip("/") + "/" + route.lstrip("/")


def capture(page, url: str, out: Path, name: str, width: int, height: int,
            full_page: bool, wait: int, browser: str = "chromium",
            suffix: bool = False) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    page.set_viewport_size({"width": width, "height": height})
    resp = page.goto(url, wait_until="networkidle", timeout=45000)
    if resp is not None and resp.status >= 400:
        log(f"  ! HTTP {resp.status} for {url}")
    try:
        page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    if wait:
        page.wait_for_timeout(wait)
    stem = f"{slug(name)}-{browser}" if suffix else slug(name)
    path = out / f"{stem}.png"
    # Some engines (WebKit) re-evaluate CSP while rasterising and log a bogus
    # "Refused to apply a stylesheet" message. Console capture is paused for
    # the screenshot itself so load-time errors are still reported.
    page._qa_collect = False
    try:
        page.screenshot(path=str(path), full_page=full_page)
    finally:
        page._qa_collect = True
    size_kb = path.stat().st_size // 1024
    log(f"  + {path.name} ({size_kb} KB)")
    return path


def launch_engines(p, names):
    """Launch every requested engine. Returns (list of (name, browser), skipped)."""
    live, skipped = [], []
    for name in names:
        engine = getattr(p, name, None)
        if engine is None:
            skipped.append((name, "unknown engine"))
            continue
        try:
            browser = engine.launch(args=["--disable-dev-shm-usage"]) if name == "chromium" \
                else engine.launch()
        except Exception as exc:
            reason = str(exc).splitlines()[0][:120]
            skipped.append((name, f"browser not installed ({reason})"))
            continue
        live.append((name, browser))
    return live, skipped


def contact_sheet(paths: list, out: Path, cols: int = 3) -> None:
    if not paths:
        return
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        log("  (Pillow not installed - skipping contact sheet)")
        return
    thumbs = []
    for p in paths:
        try:
            im = Image.open(p).convert("RGB")
            im.thumbnail((420, 260))
            thumbs.append((p, im))
        except Exception:
            continue
    if not thumbs:
        return
    w, h = 440, 300
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), "#0d1117")
    draw = ImageDraw.Draw(sheet)
    for i, (p, im) in enumerate(thumbs):
        x = (i % cols) * w + 10
        y = (i // cols) * h + 10
        sheet.paste(im, (x, y))
        draw.text((x, y + 265), p.stem[:46], fill="#e6edf3")
    sheet_path = out / "contact-sheet.png"
    sheet.save(sheet_path)
    log(f"  + {sheet_path.name} (contact sheet)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--routes", default="/")
    ap.add_argument("--out", default="docs/screenshots")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--full-page", action="store_true", default=True)
    ap.add_argument("--no-full-page", dest="full_page", action="store_false")
    ap.add_argument("--wait", type=int, default=800)
    ap.add_argument("--name", default=None)
    ap.add_argument("--browsers", default="chromium",
                    help="comma separated: chromium,firefox,webkit")
    ap.add_argument("--json", action="store_true", help="JSON payload on stdout")
    args = ap.parse_args()
    global _JSON_MODE
    _JSON_MODE = bool(args.json)

    root = resolve_root(args.root)
    err = root_error(root)
    if err:
        payload = {"error": err, "captures": []}
        emit([f"ERROR: {err}"], payload, True) if args.json else print(f"ERROR: {err}", file=sys.stderr)
        return 1
    # The output directory MUST stay inside the project root: a stray
    # `--out ../../somewhere/else` must never write outside the app.
    out, out_err = resolve_out_dir(root, args.out)
    if out_err:
        payload = {"error": out_err, "captures": []}
        emit([f"ERROR: {out_err}"], payload, True) if args.json else print(f"ERROR: {out_err}", file=sys.stderr)
        return 1
    routes = [r.strip() for r in args.routes.split(",") if r.strip()]
    browsers = [b.strip().lower() for b in args.browsers.split(",") if b.strip()]
    browsers = [b for b in browsers if b in BROWSERS] or ["chromium"]
    suffix = len(browsers) > 1

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        msg = "playwright not installed. pip install playwright && playwright install chromium"
        payload = {"error": msg, "captures": []}
        emit([f"ERROR: {msg}"], payload, True) if args.json else print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    captured = []
    records = []
    skipped = []
    console_errors = {}
    dev_console_noise = {}
    with sync_playwright() as p:
        live, skipped = launch_engines(p, browsers)
        if not live:
            payload = {"error": "no browser engine could be launched",
                       "skipped": [{"browser": b, "reason": r} for b, r in skipped],
                       "captures": []}
            emit(["ERROR: no browser engine could be launched"], payload, True) if args.json \
                else print("ERROR: no browser engine could be launched", file=sys.stderr)
            return 2
        for bname, browser in live:
            ctx = browser.new_context(device_scale_factor=2, reduced_motion="reduce")
            page = ctx.new_page()
            errors = []
            page._qa_collect = True
            page.on("console", lambda m, e=errors: e.append(m.text)
                    if m.type == "error" and getattr(page, "_qa_collect", True) else None)

            for r in routes:
                url = join_url(args.url, r)
                name = args.name if (args.name and len(routes) == 1) else (
                    "home" if r == "/" else r.strip("/").replace("/", "-"))
                log(f"capturing {url} [{bname}]")
                try:
                    path = capture(page, url, out, name, args.width, args.height,
                                   args.full_page, args.wait, bname, suffix)
                    captured.append(path)
                    records.append({
                        "route": r, "browser": bname, "file": str(path.relative_to(root)),
                        "bytes": path.stat().st_size,
                    })
                except Exception as e:
                    log(f"  ! failed {url} [{bname}]: {e}")

            if errors:
                # Framework dev noise (HMR websockets, the dev overlay) is not
                # an app defect - the profile knows what each framework prints.
                app_errors = [e for e in errors
                              if not framework_profiles.is_dev_console_noise(e, args.root)]
                dev_errors = [e for e in errors if e not in app_errors]
                if app_errors:
                    console_errors[bname] = app_errors[:20]
                    log(f"  console errors ({len(app_errors)}) in {bname}:")
                    for e in app_errors[:5]:
                        log(f"    - {e[:120]}")
                if dev_errors:
                    dev_console_noise[bname] = dev_errors[:20]
                    log(f"  ({len(dev_errors)} framework dev console message(s) ignored "
                        f"in {bname})")

            browser.close()

    contact_sheet(captured, out)
    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "url": args.url,
        "routes": routes,
        "browsers": sorted({r["browser"] for r in records}),
        "requested_browsers": browsers,
        "skipped_browsers": [{"browser": b, "reason": r} for b, r in skipped],
        "captures": records,
        "console_errors": console_errors,
        "dev_console_noise": dev_console_noise,
        "framework": framework_profiles.describe(root)["label"],
        "contact_sheet": str((out / "contact-sheet.png").relative_to(root))
        if (out / "contact-sheet.png").exists() else None,
    }
    try:
        out.mkdir(parents=True, exist_ok=True)
        (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    except OSError:
        pass

    lines = [f"done: {len(captured)} screenshot(s) -> {out}"]
    if skipped:
        lines.append("skipped browsers: " + ", ".join(f"{b} ({r})" for b, r in skipped))
    if console_errors:
        lines.append("console errors detected in: " + ", ".join(console_errors))
    emit(lines, manifest, args.json)
    return 0 if captured else 1


if __name__ == "__main__":
    raise SystemExit(main())

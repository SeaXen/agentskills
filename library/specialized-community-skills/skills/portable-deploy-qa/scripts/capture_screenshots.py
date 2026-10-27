#!/usr/bin/env python3
"""Capture README screenshots with Playwright (Chromium), plus a contact sheet.

Usage:
  python capture_screenshots.py --root <app_root> --url http://localhost:3000 \
      --route / --name home --out docs/screenshots [--width 1440] [--full-page]

  python capture_screenshots.py --root <app_root> --url http://localhost:3000 \
      --routes /,/pricing,/about --out docs/screenshots

Produces:
  <out>/<name>.png          full-page screenshot
  <out>/contact-sheet.png   grid of all captures (Pillow)

Read-only against the app; writes only into --out.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import resolve_out_dir, resolve_root, root_error


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
            full_page: bool, wait: int) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    page.set_viewport_size({"width": width, "height": height})
    resp = page.goto(url, wait_until="networkidle", timeout=45000)
    if resp is not None and resp.status >= 400:
        print(f"  ! HTTP {resp.status} for {url}")
    try:
        page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    if wait:
        page.wait_for_timeout(wait)
    path = out / f"{slug(name)}.png"
    page.screenshot(path=str(path), full_page=full_page)
    size_kb = path.stat().st_size // 1024
    print(f"  + {path.name} ({size_kb} KB)")
    return path


def contact_sheet(paths: list, out: Path, cols: int = 3) -> None:
    if not paths:
        return
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("  (Pillow not installed - skipping contact sheet)")
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
    print(f"  + {sheet_path.name} (contact sheet)")


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
    args = ap.parse_args()

    root = resolve_root(args.root)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    # The output directory MUST stay inside the project root: a stray
    # `--out ../../somewhere/else` must never write outside the app.
    out, out_err = resolve_out_dir(root, args.out)
    if out_err:
        print(f"ERROR: {out_err}", file=sys.stderr)
        return 1
    routes = [r.strip() for r in args.routes.split(",") if r.strip()]

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright not installed. pip install playwright && playwright install chromium")
        return 2

    captured = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--disable-dev-shm-usage"])
        ctx = browser.new_context(device_scale_factor=2, reduced_motion="reduce")
        page = ctx.new_page()
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)

        for r in routes:
            url = join_url(args.url, r)
            name = args.name if (args.name and len(routes) == 1) else (
                "home" if r == "/" else r.strip("/").replace("/", "-"))
            print(f"capturing {url}")
            try:
                captured.append(capture(page, url, out, name, args.width,
                                        args.height, args.full_page, args.wait))
            except Exception as e:
                print(f"  ! failed {url}: {e}")

        if errors:
            print(f"  console errors ({len(errors)}):")
            for e in errors[:5]:
                print(f"    - {e[:120]}")

        browser.close()

    contact_sheet(captured, out)
    print(f"done: {len(captured)} screenshot(s) -> {out}")
    return 0 if captured else 1


if __name__ == "__main__":
    raise SystemExit(main())

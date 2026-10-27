#!/usr/bin/env python3
"""Runtime checks against a LIVE app: headers, health, SEO metadata, 404, CORS.

This is the part of the review that can only be done against a running
server. It turns Gates F/G/I from prose into measurements.

Usage:
  python runtime_check.py --url http://localhost:3000 --routes /,/pricing \\
      --healthz /healthz [--json] [--timeout 15]

Exit 0: every required runtime check passed | Exit 1: a required check failed
"""
from __future__ import annotations

import gzip
import io
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli

USER_AGENT = "app-production-readiness/1.0 (+read-only runtime check)"
SEO_REQUIRED = ("title", "meta description", "h1", "lang attribute",
                "canonical link", "open graph tags")
SECURITY_HEADERS = {
    "x-content-type-options": "nosniff",
    "referrer-policy": "strict-origin-when-cross-origin",
    "content-security-policy": None,      # any CSP counts
    "x-frame-options": None,              # any value counts (frame-ancestors alt.)
    "strict-transport-security": None,
}


def fetch(url: str, timeout: float = 15.0, accept_gzip: bool = True):
    """GET a URL. Returns a dict with status, headers, body, ttfb."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if accept_gzip:
        req.add_header("Accept-Encoding", "gzip")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            ttfb = time.perf_counter() - started
            headers = {k.lower(): v for k, v in resp.headers.items()}
            body = raw
            if headers.get("content-encoding", "").lower() == "gzip":
                try:
                    body = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
                except OSError:
                    body = raw
            return {"url": url, "status": resp.status, "headers": headers,
                    "body": body, "ttfb_ms": round(ttfb * 1000, 1), "error": None}
    except urllib.error.HTTPError as exc:
        ttfb = time.perf_counter() - started
        body = b""
        try:
            body = exc.read()
        except Exception:
            pass
        headers = {k.lower(): v for k, v in (exc.headers or {}).items()}
        return {"url": url, "status": exc.code, "headers": headers, "body": body,
                "ttfb_ms": round(ttfb * 1000, 1), "error": None}
    except (urllib.error.URLError, socket.timeout, OSError) as exc:
        return {"url": url, "status": 0, "headers": {}, "body": b"",
                "ttfb_ms": round((time.perf_counter() - started) * 1000, 1),
                "error": str(exc)}


def html_of(res) -> str:
    try:
        return res["body"].decode("utf-8", errors="ignore")
    except Exception:
        return ""


def meta_checks(html: str, res) -> list:
    """SEO/metadata checks for one HTML document."""
    out = []
    lower = html.lower()

    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = (title_m.group(1).strip() if title_m else "")
    out.append(("title present", bool(title), f"title={title[:60]!r}"))
    if title:
        out.append(("title length 10-70 chars", 10 <= len(title) <= 70,
                    f"{len(title)} chars"))

    desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)',
                     html, re.I)
    if not desc:
        desc = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']',
                         html, re.I)
    out.append(("meta description present", bool(desc and desc.group(1).strip()),
                (desc.group(1)[:60] if desc else "")))

    og = re.search(r'<meta[^>]+property=["\']og:title["\']', html, re.I)
    out.append(("open graph tags present", bool(og), "og:title" if og else "missing og:title"))

    canon = re.search(r'<link[^>]+rel=["\']canonical["\']', html, re.I)
    out.append(("canonical link present", bool(canon), ""))

    lang = re.search(r"<html[^>]*\blang\s*=\s*[\"'][^\"']+[\"']", html, re.I)
    out.append(("lang attribute present", bool(lang), ""))

    h1 = re.findall(r"<h1\b", lower)
    out.append(("exactly one h1", len(h1) == 1, f"{len(h1)} h1 element(s)"))

    viewport = re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.I)
    out.append(("viewport meta present", bool(viewport), ""))

    # aria / a11y basics that are cheap to assert server-side
    img_no_alt = len(re.findall(r"<img\b(?![^>]*\balt\s*=)[^>]*>", html, re.I))
    out.append(("all images have alt text", img_no_alt == 0,
                f"{img_no_alt} image(s) without alt"))

    inputs_no_label = 0
    for tag in re.findall(r"<(?:input|select|textarea)\b[^>]*>", html, re.I):
        if re.search(r"\btype\s*=\s*[\"']hidden[\"']", tag, re.I):
            continue
        if re.search(r"\baria-label(?:ledby)?\s*=", tag, re.I):
            continue
        if re.search(r"\bid\s*=\s*[\"'][^\"']+[\"']", tag, re.I):
            continue
        inputs_no_label += 1
    out.append(("form controls labelled", inputs_no_label == 0,
                f"{inputs_no_label} control(s) without label/aria-label/id"))

    return out


def header_checks(res, secure: bool = False) -> list:
    """Security headers.

    HSTS is only meaningful over TLS: over plain HTTP the header is inert,
    so it is reported as a non-blocking warning instead of a failure.
    """
    out = []
    headers = res.get("headers") or {}
    for h, expected in SECURITY_HEADERS.items():
        value = headers.get(h)
        required = True
        name = f"header {h}"
        if h == "strict-transport-security" and not secure:
            required = False
            name = f"header {h} (HTTPS only)"
        if expected is None:
            out.append((name, bool(value), value or "missing", required))
        else:
            ok = bool(value) and expected.lower() in str(value).lower()
            out.append((f"{name}={expected}", ok, value or "missing", required))
    return out


def check_route(base: str, route: str, timeout: float) -> dict:
    url = base.rstrip("/") + "/" + route.lstrip("/") if route != "/" else base.rstrip("/") + "/"
    res = fetch(url, timeout)
    out = {
        "route": route,
        "url": url,
        "status": res["status"],
        "ttfb_ms": res["ttfb_ms"],
        "checks": [],
        "error": res.get("error"),
    }

    def add(name, ok, detail="", required=True):
        out["checks"].append({"name": name, "ok": bool(ok), "required": required,
                              "detail": detail})

    if res["error"]:
        add("route reachable", False, res["error"])
        return out
    add("route reachable", 200 <= res["status"] < 400, f"HTTP {res['status']}")
    add("response time < 1000 ms", res["ttfb_ms"] < 1000,
        f"{res['ttfb_ms']} ms", required=False)

    ctype = (res["headers"].get("content-type") or "").lower()
    is_html = "html" in ctype
    is_json = "json" in ctype
    secure = url.lower().startswith("https://")
    if is_html:
        add("HTML content-type", True, ctype or "no content-type", required=False)
    else:
        add("content-type is html or json", is_json, ctype or "no content-type", required=False)

    if is_html:
        html = html_of(res)
        for name, ok, detail in meta_checks(html, res):
            add(f"seo: {name}", ok, detail, required=True)

    for name, ok, detail, required in header_checks(res, secure=secure):
        add(f"security: {name}", ok, detail, required=required)

    if is_html:
        enc = (res["headers"].get("content-encoding") or "").lower()
        add("response is compressed", bool(enc) and len(res["body"]) > 200,
            f"content-encoding={enc or 'none'}", required=False)
        cc = (res["headers"].get("cache-control") or "").lower()
        add("cache-control set", bool(cc), cc or "missing", required=False)
    return out


def check_global(base: str, healthz: str, timeout: float) -> dict:
    out = {"checks": []}

    def add(name, ok, detail="", required=True):
        out["checks"].append({"name": name, "ok": bool(ok), "required": required,
                              "detail": detail})

    # health endpoint
    hres = fetch(base.rstrip("/") + "/" + healthz.lstrip("/"), timeout)
    add("health endpoint returns 2xx", 200 <= hres["status"] < 300,
        f"HTTP {hres['status']} at {healthz}")
    add("health response is small", len(hres["body"]) < 4096,
        f"{len(hres['body'])} bytes", required=False)

    # robots + sitemap
    for path, label in (("/robots.txt", "robots.txt"), ("/sitemap.xml", "sitemap.xml")):
        r = fetch(base.rstrip("/") + path, timeout)
        add(f"{label} reachable", r["status"] == 200, f"HTTP {r['status']}", required=False)

    # 404 handling
    missing = fetch(base.rstrip("/") + "/qa-nonexistent-route-9f2c", timeout)
    if missing["status"] == 404:
        add("unknown route returns 404", True, "HTTP 404")
    elif missing["status"] == 200 and "html" in (missing["headers"].get("content-type") or ""):
        add("unknown route returns 404", False,
            "soft 404: unknown route serves HTTP 200 - crawlers index duplicate content")
    else:
        add("unknown route returns 404", False, f"HTTP {missing['status']}", required=False)

    # CORS on API routes
    api = fetch(base.rstrip("/") + "/api/qa-cors-probe", timeout)
    acao = (api["headers"].get("access-control-allow-origin") or "")
    add("no wildcard CORS on /api", acao != "*", f"Access-Control-Allow-Origin: {acao or 'none'}",
        required=False)

    return out


def run(base: str, routes: list, healthz: str, timeout: float) -> dict:
    report = {"url": base, "routes": [], "global": {}, "status": "ok"}
    for r in routes:
        report["routes"].append(check_route(base, r, timeout))
    report["global"] = check_global(base, healthz, timeout)

    failures = []
    for entry in report["routes"]:
        for c in entry["checks"]:
            if c["required"] and not c["ok"]:
                failures.append(f"{entry['route']}: {c['name']} ({c['detail']})")
    for c in report["global"]["checks"]:
        if c["required"] and not c["ok"]:
            failures.append(f"global: {c['name']} ({c['detail']})")
    report["failures"] = failures
    report["status"] = "fail" if failures else "ok"
    return report


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = os.environ.get("APP_URL")
    routes_arg = os.environ.get("ROUTES")
    healthz = os.environ.get("HEALTHZ")
    timeout = 15.0
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--routes" and i + 1 < len(args):
            routes_arg = args[i + 1]
            i += 1
        elif a == "--healthz" and i + 1 < len(args):
            healthz = args[i + 1]
            i += 1
        elif a == "--timeout" and i + 1 < len(args):
            try:
                timeout = float(args[i + 1])
            except ValueError:
                pass
            i += 1
        i += 1
    if want_help:
        print(__doc__)
        return 0
    if not url:
        print("ERROR: --url is required (or set APP_URL)", file=sys.stderr)
        return 1
    routes = [r.strip() for r in (routes_arg or "/").split(",") if r.strip()] or ["/"]
    healthz = healthz or "/healthz"

    report = run(url, routes, healthz, timeout)
    lines = ["=" * 62, f"RUNTIME CHECK  [{url}]", "=" * 62]
    for entry in report["routes"]:
        lines.append(f"-- {entry['route']} (HTTP {entry['status']}, {entry['ttfb_ms']} ms) --")
        if entry.get("error"):
            lines.append(f"  [FAIL] unreachable -> {entry['error']}")
            continue
        for c in entry["checks"]:
            icon = "PASS" if c["ok"] else ("FAIL" if c["required"] else "warn")
            lines.append(f"  [{icon}] {c['name']}" + (f"  -> {c['detail']}" if not c["ok"] and c["detail"] else ""))
    lines.append("-- global --")
    for c in report["global"]["checks"]:
        icon = "PASS" if c["ok"] else ("FAIL" if c["required"] else "warn")
        lines.append(f"  [{icon}] {c['name']}" + (f"  -> {c['detail']}" if not c["ok"] and c["detail"] else ""))
    lines.append("-" * 62)
    lines.append(f"blocking failures: {len(report['failures'])}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

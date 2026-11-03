#!/usr/bin/env python3
"""
Render an HTML file to PNG via headless Chromium and crop to the page extent.

Usage:
    python render.py input.html [output.png] [--width 794] [--height 1123]

Defaults to A4 portrait at 96dpi (794x1123) — the standard Sea Knowledge
infographic size. Increase --window-h if your content might overflow the page
(see skill SKILL.md "Window-size: pick height larger than the page").
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image


def render(html_path: str, out_path: str, width: int, height: int,
           page_height: int, window_h: int) -> None:
    html_path = os.path.abspath(html_path)
    if not os.path.exists(html_path):
        sys.exit(f"HTML not found: {html_path}")

    # Capture via headless Chromium. window_h > page_height so the full document
    # is laid out; we crop down to the page extent afterwards.
    tmp = Path(tempfile.gettempdir()) / "chromium_capture.png"
    cmd = [
        "chromium",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{window_h}",
        "--virtual-time-budget=5000",
        f"--screenshot={tmp}",
        f"file://{html_path}",
    ]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, capture_output=True)

    img = Image.open(tmp)
    w, h = img.size
    print(f"Captured: {w}x{h}")

    # Crop to page extent. Find the page boundary by looking for the
    # paper color (lighter than the body background).
    px = img.load()

    # Page bg candidates (the .page CSS sets the lighter paper color)
    def is_paper(rgb):
        r, g, b = rgb
        return r > 248 and g > 240 and b > 225 and r >= g and g >= b - 5

    last_paper = 0
    for y in range(h):
        # Sample the left edge inside the page border (skip outer 8px)
        if is_paper(px[10, y]):
            last_paper = y

    crop_bot = min(last_paper + 12, h)
    page = img.crop((0, 0, w, crop_bot))
    print(f"Cropped to: {page.size}")

    if page.size != (width, page_height):
        print(f"  (Note: target was {width}x{page_height}; got {page.size}. "
              "Tune --window-h or check page CSS overflow.)")

    page.save(out_path, optimize=True)
    print(f"Saved: {out_path} ({os.path.getsize(out_path):,} bytes)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="Input HTML file")
    ap.add_argument("output", nargs="?", default=None,
                    help="Output PNG (default: <html>.png)")
    ap.add_argument("--width", type=int, default=794,
                    help="Page width in px (default: 794 = A4 at 96dpi)")
    ap.add_argument("--height", type=int, default=1123,
                    help="Target page height in px (default: 1123 = A4 at 96dpi)")
    ap.add_argument("--window-h", type=int, default=None,
                    help="Chromium window height (default: 1.6x --height, "
                         "raise if content overflows)")
    args = ap.parse_args()

    out = args.output or args.html.rsplit(".", 1)[0] + ".png"
    window_h = args.window_h or int(args.height * 1.6)

    if not shutil.which("chromium"):
        sys.exit("chromium not found in PATH. Install chromium or chromium-browser.")

    render(args.html, out, args.width, args.height, args.height, window_h)


if __name__ == "__main__":
    main()

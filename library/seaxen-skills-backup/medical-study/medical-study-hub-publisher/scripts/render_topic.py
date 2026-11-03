#!/usr/bin/env python3
"""
Render a Sea Knowledge style infographic from a markdown file.

Takes a topic name + markdown content with the standard 10-section structure,
produces:
  - <out_dir>/<slug>/<slug>.md   (the source markdown)
  - <out_dir>/<slug>/<slug>.html (the rendered HTML, viewable in any browser)
  - <out_dir>/<slug>/<slug>.png  (A4 portrait screenshot)

The PNG height auto-grows to fit content (no fixed A4 truncation). The IHD
reference topic is ~7.9K chars and fits one A4 page (794x1123); broader topics
(10-13K chars) produce 1.5-2.5 A4-page tall PNGs, which is fine — one
continuous image per topic.

Usage:
    python3 render_topic.py --slug "heart-failure" --title "Heart Failure" --markdown-file content.md
    python3 render_topic.py --slug "ihd" --title "Ischemic Heart Disease" --markdown-file /root/ihd_content.md --out-dir /tmp
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} — Sea Knowledge</title>
<style>
  :root {{
    --rose:        #c09db1;
    --rose-deep:   #996677;
    --rose-soft:   #f3dde4;
    --cream:       #faf1d0;
    --cream-deep:  #e0b13f;
    --sage:        #bfc3a6;
    --sage-deep:   #8a9a72;
    --coral:       #f68773;
    --coral-deep:  #d65a4a;
    --ink:         #3b2a32;
    --ink-soft:    #6b5460;
    --paper:       #fdf8ee;
    --paper-edge:  #ece1c8;
    --line:        #c9b59a;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0; padding: 0;
    background: #efe6d3;
    font-family: "Georgia", "Times New Roman", serif;
    color: var(--ink);
    -webkit-font-smoothing: antialiased;
  }}
  .page {{
    width: 794px;
    min-height: 1123px;
    background: var(--paper);
    margin: 0 auto;
    padding: 16px 22px 14px 22px;
    position: relative;
    background-image:
      radial-gradient(circle at 12% 18%, rgba(192,157,177,0.08), transparent 35%),
      radial-gradient(circle at 88% 82%, rgba(224,177,63,0.07), transparent 40%);
  }}
  .page::before {{
    content: ""; position: absolute; inset: 5px;
    border: 1px solid var(--paper-edge);
    border-radius: 4px;
    pointer-events: none;
  }}
  .sk-header {{
    display: flex; align-items: center; justify-content: space-between;
    border-bottom: 1.6px solid var(--rose-deep);
    padding-bottom: 5px; margin-bottom: 6px;
  }}
  .sk-brand {{ display: flex; align-items: center; gap: 8px; }}
  .sk-logo {{ width: 30px; height: 30px; }}
  .brand-text {{
    font-family: "Georgia", serif;
    font-size: 11px; letter-spacing: 1.6px;
    color: var(--rose-deep); font-weight: 700;
  }}
  .brand-text small {{ display:block; font-size: 7.5px; letter-spacing: 1.2px; color: var(--ink-soft); font-weight: 400; }}
  .sk-topic {{ text-align: right; }}
  .sk-topic .tag {{
    display: inline-block; background: var(--rose-deep); color: #fff;
    font-size: 7.5px; letter-spacing: 1.4px; padding: 1.5px 7px; border-radius: 8px;
  }}
  .sk-topic .h1 {{
    font-size: 16px; font-weight: 800; color: var(--ink);
    margin-top: 2px; letter-spacing: 0.4px;
  }}
  .sec {{
    border: 1px solid var(--line);
    border-radius: 4px;
    background: #fffdf6;
    margin-bottom: 5px;
    overflow: hidden;
  }}
  .sec-head {{
    display: flex; align-items: center; gap: 6px;
    background: linear-gradient(90deg, var(--rose-soft) 0%, #fff 95%);
    padding: 2px 7px;
    border-bottom: 0.8px solid var(--line);
  }}
  .sec-num {{
    background: var(--rose-deep); color: #fff;
    width: 15px; height: 15px; border-radius: 50%;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 8.5px; font-weight: 800;
    flex-shrink: 0;
  }}
  .sec-title {{
    font-size: 9.2px; font-weight: 800; letter-spacing: 1px;
    color: var(--rose-deep); text-transform: uppercase;
  }}
  .sec-body {{ padding: 3px 8px 4px 8px; font-size: 8.3px; line-height: 1.3; }}
  .sub-h {{
    font-size: 8px; font-weight: 800; color: var(--sage-deep);
    letter-spacing: 0.8px; text-transform: uppercase;
    margin: 3px 0 1px 0;
    display: flex; align-items: center; gap: 4px;
  }}
  .sub-h::before {{
    content: ""; width: 10px; height: 1.5px; background: var(--coral);
  }}
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }}
  .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; }}
  ul, ol {{ margin: 1px 0 2px 13px; padding: 0; }}
  li {{ margin-bottom: 1px; }}
  b, strong {{ color: var(--ink); }}
  p {{ margin: 1px 0 2px 0; }}
  .chip {{
    display: inline-block;
    background: var(--cream);
    color: var(--ink);
    border: 0.8px solid var(--cream-deep);
    border-radius: 8px;
    padding: 0 5px;
    font-size: 7.5px;
    font-weight: 700;
    margin: 0 1px;
  }}
  .chip.rose {{ background: var(--rose-soft); border-color: var(--rose); color: var(--rose-deep); }}
  .chip.sage {{ background: #eef0e3; border-color: var(--sage); color: var(--sage-deep); }}
  .chip.coral {{ background: #fde2da; border-color: var(--coral); color: var(--coral-deep); }}
  .callout {{
    background: linear-gradient(180deg, #fff7e0 0%, #fdeec0 100%);
    border: 0.8px solid var(--cream-deep);
    border-left: 3px solid var(--cream-deep);
    border-radius: 3px;
    padding: 4px 7px;
    font-size: 7.8px;
    line-height: 1.3;
    color: #5a4513;
    margin-top: 3px;
  }}
  .callout b {{ color: #5a4513; }}
  .ctable {{
    width: 100%; border-collapse: collapse; font-size: 7.6px;
    border: 0.8px solid var(--line);
  }}
  .ctable th, .ctable td {{
    border: 0.6px solid var(--line);
    padding: 1.5px 4px;
    text-align: left;
    vertical-align: top;
    line-height: 1.25;
  }}
  .ctable thead th {{
    background: var(--rose-deep); color: #fff;
    font-size: 7.5px; letter-spacing: 0.6px; text-transform: uppercase;
    text-align: center;
    font-weight: 700;
  }}
  .ctable tbody tr:nth-child(even) td {{ background: #fbf6e6; }}
  .ctable td.label {{ background: #f1e6d3; font-weight: 700; color: var(--ink); }}
  .pearls {{
    list-style: none; margin: 0; padding: 0;
    display: grid; grid-template-columns: 1fr 1fr; gap: 2px 8px;
  }}
  .pearls li {{
    position: relative; padding-left: 11px;
    font-size: 7.6px; line-height: 1.3;
  }}
  .pearls li::before {{
    content: "★";
    position: absolute; left: 0; top: 0;
    color: var(--cream-deep); font-size: 9px; line-height: 1;
  }}
  .fig {{
    border: 0.7px dashed var(--line);
    background: #fffaf0;
    border-radius: 3px;
    padding: 2px;
    text-align: center;
    font-size: 6.8px; color: var(--ink-soft);
  }}
  .fig svg {{ display: block; margin: 0 auto; }}
  .fig .cap {{ margin-top: 1px; font-style: italic; font-size: 6.5px; }}
  .sk-footer {{
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 5px; padding-top: 4px;
    border-top: 1.4px solid var(--rose-deep);
    font-size: 7.2px; color: var(--ink-soft);
  }}
  .sk-footer .logo-text {{
    font-weight: 800; letter-spacing: 1.4px; color: var(--rose-deep);
  }}
  .arrow-down {{
    width: 0; height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid var(--rose-deep);
    margin: 0 auto;
  }}
  .arrow-text {{
    text-align: center; font-size: 7px; color: var(--rose-deep);
    font-weight: 700; letter-spacing: 0.3px;
    line-height: 1;
  }}
  .flow {{
    display: flex; align-items: center; justify-content: space-between;
    gap: 2px;
  }}
  .flow .step {{
    flex: 1; text-align: center;
    background: #fff; border: 0.7px solid var(--rose);
    border-radius: 3px; padding: 2px 2px;
    font-size: 7px; color: var(--rose-deep); font-weight: 700;
    line-height: 1.15;
  }}
  .flow .step.cream {{ background: var(--cream); border-color: var(--cream-deep); color: #6a4a13; }}
  .flow .step.coral {{ background: #fde2da; border-color: var(--coral); color: var(--coral-deep); }}
  .flow .arrow {{
    color: var(--rose-deep); font-weight: 800; font-size: 10px;
  }}
  .small {{ font-size: 7.5px; color: var(--ink-soft); }}
</style>
</head>
<body>
<div class="page">

  <div class="sk-header">
    <div class="sk-brand">
      <svg class="sk-logo" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
        <circle cx="32" cy="32" r="30" fill="#f3dde4" stroke="#996677" stroke-width="2"/>
        <path d="M10 36 Q16 30 22 36 T34 36 T46 36 T58 36" fill="none" stroke="#996677" stroke-width="2.2" stroke-linecap="round"/>
        <path d="M10 44 Q16 38 22 44 T34 44 T46 44 T58 44" fill="none" stroke="#e0b13f" stroke-width="2" stroke-linecap="round"/>
        <circle cx="32" cy="22" r="3" fill="#d65a4a"/>
      </svg>
      <div class="brand-text">
        SEA KNOWLEDGE
        <small>STUDY NOTES</small>
      </div>
    </div>
    <div class="sk-topic">
      <span class="tag">CARDIOLOGY</span>
      <div class="h1">{title}</div>
    </div>
  </div>

  {body}

  <div class="sk-footer">
    <span class="logo-text">★ SEA KNOWLEDGE</span>
    <span>Cardiology · {title} · v1.0</span>
    <span>For FCPS / MRCP exam prep</span>
  </div>

</div>
</body>
</html>
"""


def parse_markdown_to_html(md):
    """Parse structured markdown into the section blocks expected by the template.

    The markdown must follow this structure:
      ## 1. Section Title
      Body content with H3, bullets, callouts, tables, etc.
      ## 2. Next Section
      ...
    """
    lines = md.split("\n")
    sections = []
    current = None
    in_table = False
    table_rows = []

    def flush_table():
        if not table_rows:
            return ""
        html_rows = []
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            cell_html = "".join(f"<{tag}>{c}</{tag}>" for c in cells)
            html_rows.append(f"<tr>{cell_html}</tr>")
        return f'<table class="ctable">{"".join(html_rows)}</table>'

    for line in lines:
        m = re.match(r"^##\s+(\d+)\.\s+(.+)$", line)
        if m:
            if current:
                table_html = flush_table()
                if table_html:
                    current["body_lines"].append(table_html)
                sections.append(current)
            current = {"num": m.group(1), "title": m.group(2).strip(), "body_lines": []}
            in_table = False
            table_rows = []
            continue

        if current is None:
            continue

        if line.strip().startswith("|"):
            table_rows.append(line)
            in_table = True
            continue
        elif in_table:
            table_html = flush_table()
            current["body_lines"].append(table_html)
            table_rows = []
            in_table = False

        current["body_lines"].append(line)

    if current:
        table_html = flush_table()
        if table_html:
            current["body_lines"].append(table_html)
        sections.append(current)

    out = []
    for s in sections:
        body_md = "\n".join(s["body_lines"]).strip()
        body_html = render_section_body(body_md)
        out.append(
            f'<div class="sec">\n'
            f'  <div class="sec-head">\n'
            f'    <span class="sec-num">{s["num"]}</span>\n'
            f'    <span class="sec-title">{s["title"]}</span>\n'
            f'  </div>\n'
            f'  <div class="sec-body">\n{body_html}\n  </div>\n'
            f'</div>'
        )
    return "\n".join(out)


def render_section_body(md):
    md = md.strip()
    lines = md.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("### "):
            text = s[4:].strip()
            out.append(f'<div class="sub-h">{escape(text)}</div>')
            i += 1
            continue
        if s == "---":
            out.append('<hr style="border:none; border-top:0.8px solid var(--line); margin:3px 0;">')
            i += 1
            continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            li_html = "".join(f"<li>{render_inline(it)}</li>" for it in items)
            out.append(f'<ol>{li_html}</ol>')
            continue
        if s.startswith("- ") or s.startswith("* "):
            items = []
            while i < len(lines) and (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            li_html = "".join(f"<li>{render_inline(it)}</li>" for it in items)
            out.append(f'<ul>{li_html}</ul>')
            continue
        if s.startswith("<table"):
            out.append(line)
            i += 1
            continue
        if s.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            text = " ".join(quote_lines)
            out.append(f'<div class="callout">{render_inline(text)}</div>')
            continue
        para_lines = []
        while i < len(lines) and lines[i].strip() and not (
            lines[i].strip().startswith("### ") or
            lines[i].strip().startswith("## ") or
            lines[i].strip().startswith("- ") or
            lines[i].strip().startswith("* ") or
            re.match(r"^\d+\.\s+", lines[i].strip()) or
            lines[i].strip() == "---" or
            lines[i].strip().startswith(">") or
            lines[i].strip().startswith("|")
        ):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            text = " ".join(para_lines)
            out.append(f'<p>{render_inline(text)}</p>')

    return "\n".join(out)


def render_inline(text):
    text = escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--markdown-file", required=True)
    ap.add_argument("--out-dir", default="/mnt/tb/Sea-knowledge")
    ap.add_argument("--tag", default="Cardiology")
    args = ap.parse_args()

    out_dir = Path(args.out_dir) / args.slug
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = Path(args.markdown_file)
    md_content = md_path.read_text(encoding="utf-8")
    md_out = out_dir / f"{args.slug}.md"
    md_out.write_text(md_content, encoding="utf-8")
    print(f"[OK] Markdown: {md_out}")

    md_body = re.sub(r"^#\s+.+?\n", "", md_content, count=1).strip()

    body_html = parse_markdown_to_html(md_body)
    html = HTML_TEMPLATE.format(title=escape(args.title), body=body_html)
    html = html.replace('>CARDIOLOGY<', f'>{args.tag.upper()}<')
    html_out = out_dir / f"{args.slug}.html"
    html_out.write_text(html, encoding="utf-8")
    print(f"[OK] HTML: {html_out}")

    png_tmp = Path("/tmp") / f"sk-{args.slug}.png"
    subprocess.run([
        "chromium", "--headless=new", "--no-sandbox", "--disable-gpu",
        "--hide-scrollbars", "--window-size=794,2000",
        "--virtual-time-budget=5000",
        f"--screenshot={png_tmp}",
        f"file://{html_out}"
    ], check=True, capture_output=True)

    from PIL import Image
    img = Image.open(png_tmp)
    w, h = img.size
    px = img.load()
    def is_paper(rgb):
        r, g, b = rgb
        return r > 248 and g > 240 and b > 230
    last_paper = 0
    for y in range(h - 1, -1, -1):
        if is_paper(px[10, y]):
            last_paper = y
            break
    if last_paper < 1123:
        last_paper = 1123
    cropped = img.crop((0, 0, w, min(last_paper + 12, h)))
    png_out = out_dir / f"{args.slug}.png"
    cropped.save(png_out, optimize=True)
    print(f"[OK] PNG: {png_out} ({png_out.stat().st_size:,} bytes, {cropped.size[0]}x{cropped.size[1]})")

    print(f"\nAll files in: {out_dir}")
    for f in sorted(out_dir.iterdir()):
        print(f"  - {f.name}  ({f.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

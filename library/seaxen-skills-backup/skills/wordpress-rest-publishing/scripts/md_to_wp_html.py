#!/usr/bin/env python3
"""
Convert Markdown to WordPress-ready HTML.

Usage:
  python3 md_to_wp_html.py --input note.md --output post.html

Reads a markdown file and outputs WordPress-compatible HTML.
Handles: headings, tables, blockquotes, lists, code blocks, bold/italic/code inline,
         wiki-style links, <details> blocks (converts to styled divs), horizontal rules,
         checkboxes.

Designed for medical study notes (FCPS/MRCP format) but works for any markdown.
Converts YAML frontmatter, callout blocks (> [!important]), collapsible answers.
"""

import argparse
import re
import html as html_lib


def md_to_wp_html(md_text, title=None):
    lines = md_text.split('\n')
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip YAML frontmatter
        if line.strip() == '---' and i == 0:
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            i += 1
            continue

        if line.strip() == '---':
            i += 1
            continue

        # H1 — skip (used as post title)
        if line.startswith('# ') and not line.startswith('## '):
            i += 1
            continue

        # H2
        if line.startswith('## '):
            text = _inline_format(line[3:].strip())
            html_parts.append(f'<h2>{text}</h2>')
            i += 1
            continue

        # H3
        if line.startswith('### '):
            text = _inline_format(line[4:].strip())
            html_parts.append(f'<h3>{text}</h3>')
            i += 1
            continue

        # H4
        if line.startswith('#### '):
            text = _inline_format(line[5:].strip())
            html_parts.append(f'<h4>{text}</h4>')
            i += 1
            continue

        # HR
        if line.strip() == '---':
            html_parts.append('<hr />')
            i += 1
            continue

        # Blockquote / callout
        if line.startswith('> '):
            quote_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                ql = lines[i][2:].strip()
                ql = re.sub(r'^\[!\w+\]\s*', '', ql)
                quote_lines.append(ql)
                i += 1
            quote_text = ' '.join(quote_lines)
            quote_text = _inline_format(quote_text)
            html_parts.append(f'<blockquote><p>{quote_text}</p></blockquote>')
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and re.match(r'\|[-| :]+\|', lines[i + 1]):
            headers = [h.strip() for h in line.strip().strip('|').split('|')]
            i += 2  # skip header + separator
            table_rows = []
            while i < len(lines) and '|' in lines[i]:
                cells = [_inline_format(c.strip()) for c in lines[i].strip().strip('|').split('|')]
                table_rows.append(cells)
                i += 1
            table_html = '<table class="wp-block-table"><thead><tr>'
            for h in headers:
                table_html += f'<th>{_inline_format(h)}</th>'
            table_html += '</tr></thead><tbody>'
            for row in table_rows:
                table_html += '<tr>'
                for cell in row:
                    table_html += f'<td>{cell}</td>'
                table_html += '</tr>'
            table_html += '</tbody></table>'
            html_parts.append(table_html)
            continue

        # Code blocks (flowcharts, etc.)
        if line.strip() == '```':
            code_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                code_lines.append(html_lib.escape(lines[i]))
                i += 1
            i += 1  # skip closing ```
            html_parts.append(f'<pre class="wp-block-code"><code>{"\\n".join(code_lines)}</code></pre>')
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', line.strip()):
            items = []
            while i < len(lines) and re.match(r'^\d+\.\s', lines[i].strip()):
                item = re.sub(r'^\d+\.\s', '', lines[i].strip())
                items.append(f'<li>{_inline_format(item)}</li>')
                i += 1
            html_parts.append(f'<ol>{"".join(items)}</ol>')
            continue

        # Bullet list
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                marker = '- ' if lines[i].strip().startswith('- ') else '* '
                item = lines[i].strip()[len(marker):]
                items.append(f'<li>{_inline_format(item)}</li>')
                i += 1
            html_parts.append(f'<ul>{"".join(items)}</ul>')
            continue

        # Collapsible <details> blocks (convert to styled div)
        if line.strip().startswith('<details>'):
            detail_lines = []
            while i < len(lines) and '</details>' not in lines[i]:
                detail_lines.append(lines[i])
                i += 1
            if i < len(lines):
                detail_lines.append(lines[i])
                i += 1
            detail_html = '\n'.join(detail_lines)
            detail_html = detail_html.replace('<summary>Answer</summary>',
                                              '<summary><strong>Answer</strong></summary>')
            wp_block = '<div class="wp-block-group has-background" style="background-color:#f0f4f8;padding:16px;border-radius:8px;margin:12px 0;">'
            wp_block += detail_html.replace('<details>', '').replace('</details>', '')
            wp_block += '</div>'
            html_parts.append(wp_block)
            continue

        # Empty line
        if line.strip() == '':
            i += 1
            continue

        # Regular paragraph
        p_text = _inline_format(line.strip())
        p_text = p_text.replace('- [ ]', '☐').replace('- [x]', '☑')
        html_parts.append(f'<p>{p_text}</p>')
        i += 1

    return '\n'.join(html_parts)


def _inline_format(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[\[(.+?)\]\]', r'<strong>\1</strong>', text)
    return text


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to WordPress HTML')
    parser.add_argument('--input', required=True, help='Input markdown file')
    parser.add_argument('--output', required=True, help='Output HTML file')
    parser.add_argument('--title', default=None, help='Post title (excluded from body)')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        md = f.read()

    html_out = md_to_wp_html(md, title=args.title)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html_out)

    print(f'Converted {args.input} -> {args.output} ({len(html_out)} chars)')


if __name__ == '__main__':
    main()

"""Pre-process source markdown for Sea Knowledge renderer.

The renderer (render_topic.py) only creates `sec` blocks from headers matching
`^## \d+\. `. Raw source files with `## Learning Objectives`, `## Aetiology`,
etc. produce blank PNGs. This script strips frontmatter and auto-numbers all
`## ` headers sequentially while preserving `### ` sub-headers unchanged.

Usage:
    python3 preprocess_headers.py <src_dir> <out_dir>
    # e.g. python3 preprocess_headers.py /mnt/tb/Medicine/'Nephrology and Urology' /root/nephro-content

Pattern is reusable for any new chapter where source headers aren't pre-numbered.
Cardiology source already lived pre-numbered in /root/sk-content/; this script
is needed for nephrology and any future chapter that starts from raw source.
"""
import re
import sys
from pathlib import Path


def preprocess(src_path: Path, out_path: Path) -> bool:
    raw = src_path.read_text(encoding='utf-8', errors='replace')
    # Strip YAML frontmatter
    raw = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.DOTALL)
    # Auto-number `## ` headers (NOT `### `)
    counter = 0
    out_lines = []
    for line in raw.splitlines():
        m = re.match(r'^## (?!#)(.+)$', line)
        if m:
            counter += 1
            out_lines.append(f'## {counter}. {m.group(1)}')
        else:
            out_lines.append(line)
    out_path.write_text('\n'.join(out_lines), encoding='utf-8')
    return counter > 0


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    processed = 0
    for src in sorted(src_dir.glob('*.md')):
        dst = out_dir / src.name
        if preprocess(src, dst):
            processed += 1
    print(f"Processed {processed} files into {out_dir}")


if __name__ == '__main__':
    main()

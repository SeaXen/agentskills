# Bengali PDF export fallback

Use this when the user wants a Bangla PDF and common converters are unavailable.

## Trigger

- `pandoc`, `wkhtmltopdf`, `libreoffice`, and `soffice` are missing
- The environment still has `python3`, `pip3`, network access, and permission to create a temp venv
- The document is primarily Bengali and needs a readable PDF quickly

## Workflow used successfully

1. Check available tools.
   - Probe for `pandoc`, `wkhtmltopdf`, `libreoffice`, `soffice`
   - Probe Python with `python3`

2. Create a temporary virtual environment.
   - `python3 -m venv /tmp/pdfenv`
   - `/tmp/pdfenv/bin/pip install fpdf2`

3. Download Bengali fonts.
   - System fonts may not include Bengali.
   - A reliable route is to query Google Fonts CSS for `Noto Sans Bengali` and then download the `.ttf` URLs from `fonts.gstatic.com`.
   - In this session, these worked:
     - regular: `https://fonts.gstatic.com/s/notosansbengali/v33/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6KmsolLudA.ttf`
     - bold: `https://fonts.gstatic.com/s/notosansbengali/v33/Cn-SJsCGWQxOjaGwMQ6fIiMywrNJIky6nvd8BjzVMvJx2mcSPVFpVEqE-6Kmsm5MudA.ttf`

4. Convert markdown to PDF with a small Python script.
   - Register regular + bold Bengali fonts in `fpdf2`
   - Parse headings (`#`, `##`, `###`), bullets, numbered references, and paragraphs
   - Use `multi_cell()` with explicit width calculations
   - Add a footer with page numbers

5. Verify output.
   - Confirm the PDF file exists
   - Confirm non-zero size with `stat()`

## Important pitfalls

- `pip3 install --user ...` can fail in externally managed environments (PEP 668). Use a virtual environment instead.
- GitHub HTML pages are not fonts. If you download from `github.com/.../raw/...`, inspect the file; bad downloads may start with `<!DOCTYPE html>`.
- Prefer `raw.githubusercontent.com` or direct `fonts.gstatic.com` font URLs.
- `fpdf2` can throw `Not enough horizontal space to render a single character` if `multi_cell()` is called with width `0` after indentation. Compute width explicitly as:
  - `pdf.w - pdf.l_margin - pdf.r_margin - indent`
- Bengali rendering depends on loading a proper Bengali-capable font. Default Latin fonts are not enough.

## Minimal verification snippet

```python
from pathlib import Path
for p in ['/tmp/out.md', '/tmp/out.pdf']:
    f = Path(p)
    print(f, f.exists(), f.stat().st_size if f.exists() else 0)
```

## When to prefer a better tool

If `pandoc` plus a Unicode-capable engine is available, prefer it for higher-fidelity layout. This fallback is best for simple assignment-style PDFs where readable Bengali output matters more than perfect typography.

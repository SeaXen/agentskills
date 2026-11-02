"""Brand extraction from a website and DTCG token export (no network)."""
from __future__ import annotations

import contextlib
import io
import json
import tempfile
from pathlib import Path

from support import check

import brand_extract
import tokens

FIXTURE_HTML = """<html><head><title>Acme Rockets | Home</title>
<meta property="og:image" content="/og.png">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="https://cdn.example.net/other.css">
<style>:root { --brand-primary: #ff6a00; --grey: #888888; }</style></head>
<body><header><a class="site-logo" href="/"><svg viewBox="0 0 10 10"></svg></a></header>
<img src="/img/acme-logo.png" alt="Acme"><p style="color: rgb(255, 106, 0)">x</p></body></html>
"""
FIXTURE_CSS = """@font-face { font-family: "Acme Sans"; src: url(a.woff2); }
body { font-family: "Acme Sans", Inter, sans-serif; color: #111; background: #fafafa; }
a { color: #ff6a00; } .btn { background: hsl(210 50% 40%); } .x { color: #ffffff; }
"""


def test_brand_wcag_contrast_uses_gamma_expansion() -> None:
    ratio = brand_extract.contrast_ratio("#777777", "#ffffff")
    check("WCAG contrast #777777 on white is 4.48:1", round(ratio, 2) == 4.48, f"got {ratio:.4f}")
    check("WCAG contrast black on white is 21:1",
          round(brand_extract.contrast_ratio("#000000", "#ffffff"), 2) == 21.0)


def test_brand_accent_darkens_until_it_passes_on_parchment() -> None:
    source = "#ff6a00"
    darkened, steps = brand_extract.ensure_contrast(source)
    ratio = brand_extract.contrast_ratio(darkened, brand_extract.PARCHMENT)
    check("light accent is darkened to reach 4.5:1 on parchment",
          steps > 0 and ratio >= 4.5
          and brand_extract.contrast_ratio(source, brand_extract.PARCHMENT) < 4.5,
          f"{source} -> {darkened} in {steps} steps, {ratio:.2f}:1")
    kept, kept_steps = brand_extract.ensure_contrast("#1b365d")
    check("passing accent is kept unchanged", kept == "#1b365d" and kept_steps == 0,
          f"got {kept} after {kept_steps} steps")


def test_brand_extract_parses_fixture() -> None:
    result = brand_extract.extract(FIXTURE_HTML, [FIXTURE_CSS], "https://acme.example/")
    colors = [c for c, _ in result["colors"]]
    check("brand-named custom property ranks first", colors[:1] == ["#ff6a00"], f"got {colors}")
    check("greys, near-white, and near-black are dropped",
          not {"#888888", "#ffffff", "#111111", "#fafafa"} & set(colors), f"got {colors}")
    check("hsl() colors are parsed", "#336699" in colors, f"got {colors}")
    check("fonts ranked, generics dropped",
          [f for f, _ in result["fonts"]][:1] == ["Acme Sans"]
          and "sans-serif" not in dict(result["fonts"]), f"got {result['fonts']}")
    check("site name comes from the title's first segment", result["name"] == "Acme Rockets",
          f"got {result['name']}")
    check("inline header svg and logo img are logo candidates, og:image is not",
          any("inline <svg> in <header>" in logo for logo in result["logos"])
          and "https://acme.example/img/acme-logo.png" in result["logos"]
          and "https://acme.example/og.png" not in result["logos"], f"got {result['logos']}")


def test_brand_extract_file_url_end_to_end() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        site = Path(tmp)
        (site / "index.html").write_text(FIXTURE_HTML, encoding="utf-8")
        (site / "style.css").write_text(FIXTURE_CSS, encoding="utf-8")
        out = site / "brand.md"
        with contextlib.redirect_stdout(io.StringIO()):
            rc = brand_extract.main([(site / "index.html").as_uri(), "-o", str(out)])
        draft = out.read_text(encoding="utf-8") if out.exists() else ""
    example = (brand_extract.EXAMPLE_PROFILE).read_text(encoding="utf-8")
    example_keys = [line.split(":")[0] for line in example.split("---")[1].splitlines()
                    if line and not line.startswith("#")]
    draft_keys = [line.split(":")[0] for line in draft.split("---")[1].splitlines()
                  if line and not line.startswith("#")] if draft.count("---") >= 2 else []
    check("brand_extract writes a draft with the example's frontmatter keys",
          rc == 0 and draft_keys == example_keys, f"rc={rc} keys={draft_keys}")
    check("draft fills company and a darkened brand_color, reads only same-origin CSS",
          'company: "Acme Rockets"' in draft and 'brand_color: "#B84C00"' in draft
          and "Acme Sans" in draft, draft[-900:])


def test_brand_extract_network_error_is_one_line() -> None:
    err = io.StringIO()
    with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
        rc = brand_extract.main(["file:///nonexistent-kami-brand/index.html"])
    lines = err.getvalue().strip().splitlines()
    check("fetch failure prints one ERROR line and exits 2",
          rc == 2 and len(lines) == 1 and lines[0].startswith("ERROR:"), f"rc={rc} {lines}")


def test_tokens_dtcg_export() -> None:
    canonical = json.loads(tokens.TOKENS_FILE.read_text(encoding="utf-8"))
    exported = tokens.dtcg_tokens()
    group = exported.get("color", {})
    check("DTCG export carries every token as $type color with its $value",
          len(group) == len(canonical)
          and group["parchment"] == {"$type": "color", "$value": "#f5f4ed"}
          and all(set(v) == {"$type", "$value"} and v["$type"] == "color" for v in group.values()),
          f"got {list(group)[:4]}")


def test_brand_extract_ignores_inline_noise_and_reads_font_vars() -> None:
    html = ('<html><head><style>:root{--font-size-1:13px;'
            '--font-sans:"Inter Variable",sans-serif;--color-accent:#5e6ad2}'
            'a{color:#5e6ad2}</style></head><body>'
            + '<span style="--accent:#e4f222">x</span>' * 6 + '</body></html>')
    result = brand_extract.extract(html, [], "https://acme.example/")
    check("stylesheet brand var beats repeated inline style colors",
          result["colors"][:1] and result["colors"][0][0] == "#5e6ad2", f"got {result['colors']}")
    check("font custom properties count, size vars do not",
          [f for f, _ in result["fonts"]] == ["Inter Variable"], f"got {result['fonts']}")
    check("stylesheets on a subdomain count as the same site, other domains do not",
          brand_extract._same_site("https://linear.app", "https://static.linear.app/a.css")
          and not brand_extract._same_site("https://stripe.com", "https://b.stripecdn.com/a.css"))

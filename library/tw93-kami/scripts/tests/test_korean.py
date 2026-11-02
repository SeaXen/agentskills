"""Korean rendering: word-level line breaks and CID-keyed CFF fonts that every reader draws."""
from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path

from support import REPO_ROOT, check, skip

from font_compat import is_cid_cff, use_truetype_fonts
from hangul import JOINER, MAX_WORD_UNITS, join_hangul_words

KR_OTF = REPO_ROOT / "assets" / "fonts" / "SourceHanSerifKR-Regular.otf"
SENTENCE = "김도윤 님은 실시간 로그 파이프라인을 Kafka와 Flink로 재구축해 데이터 지연을 45분에서 90초로 줄였습니다."


def test_hangul_joins_inside_words_only() -> None:
    out = join_hangul_words("<p>파이프라인을 재구축해</p>")
    check("hangul words are joined inside", f"파{JOINER}이{JOINER}프" in out, out)
    check("the space between words stays a break", f"을 재" in out, out)
    check("mixed words with hangul are joined whole", JOINER in join_hangul_words("<p>Kafka와</p>").split("와")[0])


def test_hangul_word_continues_across_inline_tags() -> None:
    out = join_hangul_words('<p>현재 <span class="hl">18개 팀</span>이 사용</p>')
    check("a particle after an inline tag joins its word", f"</span>{JOINER}이" in out, out)
    out = join_hangul_words("<p>사용<br>합니다</p>")
    check("a block or line break tag ends the word", f"<br>{JOINER}" not in out, out)


def test_hangul_skips_non_prose_and_keeps_entities() -> None:
    src = ("<html><head><title>제목</title><style>.a::before{content:'가나'}</style></head>"
           "<body><svg><text>그래프</text></svg><pre><code>변수명</code></pre><p>가&amp;나</p></body></html>")
    out = join_hangul_words(src)
    check("style, svg, code, and title text are untouched",
          "content:'가나'" in out and "<text>그래프</text>" in out and "<code>변수명</code>" in out
          and "<title>제목</title>" in out, out)
    check("an entity is never split", "&amp;" in out and f"&{JOINER}amp" not in out, out)


def test_hangul_long_words_stay_breakable() -> None:
    word = "가" * (MAX_WORD_UNITS + 1)
    check("a word over the cap keeps its break opportunities", JOINER not in join_hangul_words(f"<p>{word}</p>"))
    check("a document without hangul is returned unchanged",
          join_hangul_words("<p>plain text 中文</p>") == "<p>plain text 中文</p>")


def test_font_compat_rewrites_only_local_cid_fonts() -> None:
    if not KR_OTF.is_file():
        skip("CID-keyed CFF detection", f"{KR_OTF} missing")
        return
    check("Source Han Serif K otf is detected as CID-keyed CFF", is_cid_cff(KR_OTF))
    tsanger = REPO_ROOT / "assets" / "fonts" / "TsangerJinKai02-W04.ttf"
    if tsanger.is_file():
        check("a TrueType font is not treated as CID-keyed CFF", not is_cid_cff(tsanger))
    css = '@font-face { font-family: "X"; src: url("https://example.invalid/none.otf") format("opentype"); }'
    check("an unresolvable remote source is left alone", use_truetype_fonts(css, REPO_ROOT) == css)


def test_korean_render_is_visible_and_breaks_between_words() -> None:
    try:
        import fitz  # noqa: F401
        from optional_deps import require_pymupdf, require_weasyprint_html
        require_weasyprint_html()
        require_pymupdf()
        from render import render_pdf
    except Exception as exc:
        skip("Korean render path", str(exc), ci_required=True)
        return
    if not KR_OTF.is_file():
        skip("Korean render path", f"{KR_OTF} missing", ci_required=True)
        return
    import fitz

    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        old_cache = os.environ.get("XDG_CACHE_HOME")
        os.environ["XDG_CACHE_HOME"] = str(root / "cache")
        try:
            html = root / "ko.html"
            html.write_text(
                '<html lang="ko"><head><meta charset="utf-8"><style>'
                f'@font-face {{ font-family: "K"; src: url("{KR_OTF.as_uri()}") format("opentype"); }}'
                "@page { size: A5; margin: 12mm } p { font-family: K; font-size: 12pt; width: 58mm }"
                f"</style></head><body><p>{SENTENCE}</p></body></html>",
                encoding="utf-8")
            pdf = root / "ko.pdf"
            render_pdf(html, pdf)
            doc = fitz.open(str(pdf))
            page = doc[0]
            kinds = {f[1] for f in page.get_fonts()}
            lines = ["".join(s["text"] for s in ln["spans"])
                     for b in page.get_text("dict")["blocks"] for ln in b.get("lines", [])]
            words = set(SENTENCE.split())
            split = [ln for ln in lines if ln.strip() and not set(ln.split()) <= words]
            pix = page.get_pixmap(dpi=60, clip=fitz.Rect(0, 0, page.rect.width, page.rect.height / 2))
            ink = sum(1 for i in range(0, len(pix.samples), pix.n) if pix.samples[i] < 128)
            check("the Korean font is embedded as TrueType, not CID-keyed CFF", kinds == {"ttf"}, str(kinds))
            check("MuPDF draws the Korean glyphs", ink > 400, f"dark pixels {ink}")
            check("every rendered line ends on a word boundary", len(lines) > 2 and not split, str(lines))
            check("no word joiner reaches the PDF text layer", JOINER not in page.get_text())
        finally:
            if old_cache is None:
                os.environ.pop("XDG_CACHE_HOME", None)
            else:
                os.environ["XDG_CACHE_HOME"] = old_cache

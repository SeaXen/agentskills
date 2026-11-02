"""Labelled corpus for the PDF layout gates.

Each gate that reads `references/checks_thresholds.json` (orphans, density,
resume balance) has should-flag and should-pass HTML fixtures under
`corpus/<gate>/{flag,pass}/`, including one case just inside and one just
outside each threshold. Every fixture is rendered through the shared
`render.render_pdf` path and judged by the real gate entry point, so a
threshold edit shows up as fixtures changing sides. The per-gate confusion line
is printed on every run to make that delta visible.

The predicate seams (`_orphan_last_line`, `_density_bucket`,
`_resume_balance_issues`) keep their own synthetic tests in test_render.py;
this module covers the rendered end to end path those do not reach.
"""
from __future__ import annotations

import re
import tempfile
from pathlib import Path

from support import check, silently, skip

CORPUS = Path(__file__).resolve().parent / "corpus"
LABEL_RE = re.compile(r"\A<!-- (flag|pass): \S.*? -->\n")


def _gates():
    from checks import check_density, check_orphans, check_resume_balance
    return {
        "orphans": check_orphans,
        "density": check_density,
        "resume_balance": check_resume_balance,
    }


def _fixtures(gate: str) -> list[tuple[str, Path]]:
    return [
        (label, path)
        for label in ("flag", "pass")
        for path in sorted((CORPUS / gate / label).glob("*.html"))
    ]


def test_gate_corpus_fixtures_are_labelled() -> None:
    for gate in ("orphans", "density", "resume_balance"):
        fixtures = _fixtures(gate)
        labels = [label for label, _ in fixtures]
        check(f"corpus {gate} has 3+ flag and 3+ pass fixtures",
              labels.count("flag") >= 3 and labels.count("pass") >= 3,
              f"flag={labels.count('flag')} pass={labels.count('pass')}")
        unlabelled = [
            path.name for label, path in fixtures
            if (m := LABEL_RE.match(path.read_text(encoding="utf-8"))) is None
            or m.group(1) != label
        ]
        check(f"corpus {gate} fixtures state their label and reason on line 1",
              not unlabelled, f"unlabelled: {unlabelled}")


def test_gate_corpus_verdicts_match_labels() -> None:
    try:
        from render import render_pdf
        import weasyprint  # noqa: F401
        import pypdf  # noqa: F401
        import fitz  # noqa: F401
    except ImportError as exc:
        skip("gate corpus verdicts", f"render dependencies unavailable: {exc}", ci_required=True)
        return

    with tempfile.TemporaryDirectory() as tmp:
        for gate, fn in _gates().items():
            counts = {"flag": [0, 0], "pass": [0, 0]}  # label -> [flagged, total]
            for label, html in _fixtures(gate):
                pdf = Path(tmp) / gate / label / f"{html.stem}.pdf"
                render_pdf(html, pdf)
                rc = silently(fn, [str(pdf)])
                flagged = rc == 1
                counts[label][1] += 1
                counts[label][0] += int(flagged)
                check(f"corpus {gate}/{label}/{html.stem} is {'flagged' if label == 'flag' else 'passed'}",
                      rc in (0, 1) and flagged == (label == "flag"),
                      f"rc={rc}")
            print(f"CORPUS: {gate}: flag fixtures {counts['flag'][0]}/{counts['flag'][1]} flagged, "
                  f"pass fixtures {counts['pass'][0]}/{counts['pass'][1]} flagged")


def test_resume_thin_source_is_told_apart_from_layout() -> None:
    """Only a two-page shortfall that no layout can close is softened to a data gap."""
    try:
        from render import render_pdf
        from checks import resume_thin_source
        import weasyprint  # noqa: F401
        import fitz  # noqa: F401
    except ImportError as exc:
        skip("resume thin-source classification", f"render dependencies unavailable: {exc}", ci_required=True)
        return
    expected = {
        "thin-continuation-60-65": True,   # 125% of ink in total: short of material
        "p1-97": False,                    # an overfull page is a layout problem
        "one-page": False,                 # one page breaks the contract outright
        "p2-81": False,                    # enough ink, page 2 just short: fix the layout
    }
    with tempfile.TemporaryDirectory() as tmp:
        for name, thin in expected.items():
            html = CORPUS / "resume_balance" / "flag" / f"{name}.html"
            pdf = Path(tmp) / f"{name}.pdf"
            render_pdf(html, pdf)
            verdict = resume_thin_source(pdf)
            check(f"resume {name} is {'thin source' if thin else 'a layout failure'}",
                  bool(verdict) == thin, str(verdict))

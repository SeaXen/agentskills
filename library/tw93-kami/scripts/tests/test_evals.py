"""evals/score.py gates that read the HTML text rather than run a Kami check."""
from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

from support import REPO_ROOT, check

_SPEC = importlib.util.spec_from_file_location("eval_score", REPO_ROOT / "evals" / "score.py")
score = importlib.util.module_from_spec(_SPEC)
sys.modules["eval_score"] = score
_SPEC.loader.exec_module(score)

# Lines a filled long-doc-cn white paper wrote: supplied figures, shares and
# multiples derived from them, and definitional percentiles.
CLEAN = (
    "纯缓存命中 QPS 18.5 万，P99 延迟 4.2 毫秒；命中率 90% 混合 QPS 12.1 万，P99 11 毫秒；"
    "全部回源 2.3 万、48 毫秒。混合场景约为纯命中的 65%，P99 约 2.6 倍，下降约 35%（推算）。"
    "3 家客户峰值命中率 94%，只有 6% 的请求回源，回源流量下降 81%，请求合并减少 97%。"
    "P99 失效延迟 350 毫秒，即 99% 的失效在 350 毫秒内到达，仍有 1% 更慢。"
)


def test_invented_numbers_gate() -> None:
    supplied = score.SUPPLIED["long-doc-cn"]
    row: dict = {}
    score._invented(row, CLEAN, supplied)
    check("invented gate passes supplied, derived and definitional figures",
          row.get("invented") is True, str(row.get("stray")))
    for invented in ("多活切换耗时 30 秒", "双活 QPS 25 万", "P99 7 毫秒", "每月节省 2000 元",
                     "需要 6 台节点", "可用性 99.99%"):
        row = {}
        score._invented(row, CLEAN + invented, supplied)
        check(f"invented gate flags {invented}", row.get("invented") is False
              and len(row.get("stray", [])) == 1, str(row.get("stray")))


def test_invented_gate_ignores_chart_axes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        html = Path(tmp) / "whitepaper.html"
        html.write_text(f"<body><p>{CLEAN}</p><svg><text>20</text><text>万 QPS</text></svg></body>",
                        encoding="utf-8")
        row: dict = {}
        score._invented(row, score._html_text(html, drop_svg=True), score.SUPPLIED["long-doc-cn"])
        check("invented gate skips chart axis ticks inside svg", row.get("invented") is True,
              str(row.get("stray")))

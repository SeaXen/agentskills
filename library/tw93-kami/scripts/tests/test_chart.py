"""Data charts: spec to SVG geometry, data validation, and the drift gate."""
from __future__ import annotations

import html
import re

from support import check, silently, write_temp_html

from chart import (
    FONT_CN,
    FONT_EN,
    FONT_KO,
    ChartError,
    _shares,
    check_charts,
    compare_chart,
    find_charts,
    nice_scale,
    render_chart,
)
from shared import DIAGRAMS

BAR = {"type": "bar", "categories": ["A", "B"], "series": [{"name": "S", "values": [50, 100]}]}


def _raises(spec: dict) -> str:
    try:
        render_chart(spec)
    except ChartError as exc:
        return str(exc)
    return ""


def test_chart_types_render() -> None:
    specs = [
        BAR,
        {"type": "line", "categories": ["Q1", "Q2", "Q3"], "series": [{"name": "a", "values": [1, 2, 3]},
                                                                     {"name": "b", "values": [2, 1, 2]}]},
        {"type": "hbar", "items": [{"label": "x", "value": 3}, {"label": "y", "value": 1}]},
        {"type": "donut", "items": [{"label": "x", "value": 3}, {"label": "y", "value": 1}]},
        {"type": "candlestick", "points": [{"label": "d1", "open": 10, "high": 12, "low": 9, "close": 11}]},
        {"type": "waterfall", "items": [{"label": "s", "value": 10, "total": True}, {"label": "d", "value": -3},
                                        {"label": "e", "total": True}]},
    ]
    for spec in specs:
        svg = render_chart(spec)
        check(f"chart {spec['type']} renders a tagged svg",
              f'data-kami-chart="{spec["type"]}"' in svg and compare_chart(svg) is None)


def test_chart_bar_geometry() -> None:
    svg = render_chart(BAR)
    heights = [float(h) for h in re.findall(r'<rect x="[^"]+" y="[^"]+" width="[^"]+" height="([^"]+)" fill="#1B365D"', svg)]
    # Axis 0-100 over the 200-unit plot: 50 -> 100, 100 -> 200.
    check("bar heights are value / axis max x plot height", heights == [100.0, 200.0], str(heights))


def test_chart_nice_scale() -> None:
    check("nice scale 0-88 rounds to 0-100 step 20", nice_scale(0, 88, include_zero=True) == (0, 100, 20))
    check("nice scale 116-158 rounds to 110-160 step 10", nice_scale(116, 158, include_zero=False) == (110, 160, 10))
    lo, hi, _ = nice_scale(-40, 170, include_zero=True)
    check("nice scale keeps negatives on the axis", lo <= -40 and hi >= 170, f"{lo}..{hi}")


def test_chart_compact_size_narrows_the_canvas() -> None:
    full = render_chart(BAR)
    compact = render_chart({**BAR, "size": "compact"})
    width = lambda svg: float(re.search(r'viewBox="0 0 ([0-9.]+) ', svg).group(1))
    check("compact charts draw on a narrower canvas with the same type sizes",
          width(compact) < width(full) * 0.7 and 'font-size="12"' in compact)
    check("an unknown size is refused", "size must be" in _raises({**BAR, "size": "huge"}))


def test_chart_ticks_start_at_the_left_edge() -> None:
    svg = render_chart(BAR)
    xs = [float(x) for x in re.findall(r'<text x="([0-9.]+)"[^>]*text-anchor="end">', svg)]
    widest = max(xs)
    check("tick labels end close to the plot and leave no dead margin", 20 <= widest <= 40, str(widest))


def test_chart_axis_ticks_follow_step_precision() -> None:
    svg = render_chart({"type": "bar", "categories": ["a", "b"], "series": [{"values": [18.5, 2.3]}]})
    ticks = re.findall(r'text-anchor="end">([^<]+)<', svg)
    check("decimal data on a whole-number step keeps integer ticks", ticks == ["0", "5", "10", "15", "20"], str(ticks))
    svg = render_chart({"type": "line", "categories": ["a", "b"], "series": [{"values": [0.3, 1.2]}]})
    ticks = re.findall(r'text-anchor="end">([^<]+)<', svg)
    check("a fractional step keeps its decimal", ticks[:2] == ["0.0", "0.2"], str(ticks))


def test_chart_donut_shares_sum_to_100() -> None:
    check("largest remainder keeps three thirds at 100", sum(_shares([1, 1, 1], 0)) == 100)
    check("largest remainder at one decimal", round(sum(_shares([1, 1, 1], 1)), 1) == 100.0)


def test_chart_rejects_bad_data() -> None:
    check("waterfall total that is not the running sum is refused",
          "running sum" in _raises({"type": "waterfall", "items": [
              {"label": "s", "value": 10, "total": True}, {"label": "d", "value": 5},
              {"label": "e", "value": 14, "total": True}]}))
    check("candle whose low sits above the close is refused",
          "do not contain" in _raises({"type": "candlestick", "points": [
              {"label": "d", "open": 130, "high": 136, "low": 126, "close": 124}]}))
    check("donut over six items points at hbar",
          "hbar" in _raises({"type": "donut", "items": [{"label": str(i), "value": 1} for i in range(7)]}))
    check("series length must match categories",
          "values for" in _raises({"type": "bar", "categories": ["a", "b"], "series": [{"values": [1]}]}))
    check("unknown chart type is refused", "type must be" in _raises({"type": "pie"}))


def test_chart_font_follows_label_script() -> None:
    def font(labels: list[str]) -> str:
        svg = render_chart({"type": "hbar", "items": [{"label": l, "value": 1} for l in labels]})
        return html.unescape(re.search(r'font-family="([^"]+)"', svg).group(1))
    check("latin labels use the EN serif chain", font(["North", "South"]) == html.unescape(FONT_EN))
    check("han labels lead with a CJK serif", font(["华东", "华南"]) == html.unescape(FONT_CN))
    check("hangul labels lead with Source Han Serif KR", font(["서울", "부산"]) == html.unescape(FONT_KO)
          and "Source Han Serif KR" in FONT_KO)


def test_chart_gate_catches_drift() -> None:
    svg = render_chart(BAR)
    page = f"<html><body><figure>{svg}</figure></body></html>"
    path = write_temp_html(page, suffix=".html")
    check("gate passes a freshly generated chart", silently(check_charts, [str(path)]) == 0)

    restyled = page.replace("<svg viewBox", '<svg style="width:100%" viewBox', 1)
    path.write_text(restyled, encoding="utf-8")
    check("gate ignores restyling of the root tag", silently(check_charts, [str(path)]) == 0)

    edited_label = page.replace(">100<", ">120<", 1)
    check("tamper fixture edited_label actually changes the page", edited_label != page)
    path.write_text(edited_label, encoding="utf-8")
    check("gate fails a hand-edited value label", silently(check_charts, [str(path)]) == 1)

    edited_bar = page.replace('height="200"', 'height="220"', 1)
    check("tamper fixture edited_bar actually changes the page", edited_bar != page)
    path.write_text(edited_bar, encoding="utf-8")
    check("gate fails a hand-edited bar height", silently(check_charts, [str(path)]) == 1)

    dropped = re.sub(r"<rect x=[^>]*fill=\"#1B365D\"[^>]*/>", "", page, count=1)
    check("tamper fixture dropped actually changes the page", dropped != page)
    path.write_text(dropped, encoding="utf-8")
    check("gate fails a removed mark", silently(check_charts, [str(path)]) == 1)
    path.unlink()


def test_chart_diagram_templates_are_generated() -> None:
    for name in ("bar-chart", "line-chart", "donut-chart", "candlestick", "waterfall"):
        text = (DIAGRAMS / f"{name}.html").read_text(encoding="utf-8")
        charts = find_charts(text)
        check(f"{name}.html carries a generated chart that matches its spec",
              len(charts) == 1 and compare_chart(charts[0]) is None)
        check(f"{name}.html no longer teaches hand-edited coordinates", "DATA START" not in text)

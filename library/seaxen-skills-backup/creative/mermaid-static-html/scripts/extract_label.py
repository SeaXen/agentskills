#!/usr/bin/env python3
"""Mermaid label extraction helper.

Robustly extracts clean text from mermaid node declarations and edge labels,
handling all the common shape variants and edge cases.

Usage:
    from extract_label import extract_label, normalize_node_id, parse_node_decl

    # Strip delimiters from a label that already has its node ID removed
    clean = extract_label("[Amyloid]")        # "Amyloid"
    clean = extract_label("{{Hexagon}}")      # "Hexagon"
    clean = extract_label("((Bang shape))")   # "Bang shape"
    clean = extract_label("|edge label|")     # "edge label"

    # Parse a full node declaration (id + delimiters + label)
    node = parse_node_decl("A[Start]")        # {"id": "A", "label": "Start", "shape": "rect"}

    # Normalize node IDs that have special chars
    safe_id = normalize_node_id("A[Start]")   # "A_Start"
"""

import re


def extract_label(raw: str) -> str:
    """Strip mermaid shape delimiters from a label and return clean text.

    Handles:
      - Default: text
      - Rounded rect [text]
      - Circle (text)
      - Cloud )text(
      - Hexagon {{text}}  (strip 2 each end)
      - Bang ((text))     (strip 2 each end)
      - Trapezoid [/text/], [\text\]
      - Parallelogram [/text/]
      - Edge label |text|
      - Multi-line labels (joins lines with space)

    Returns the raw string with brackets stripped if recognized, otherwise
    returns the input unchanged.
    """
    if raw is None:
        return ""
    text = raw.strip()
    if not text:
        return ""

    # Multi-line: join lines
    if "\n" in text:
        text = " ".join(line.strip() for line in text.split("\n") if line.strip())

    # Edge label pipe-delimited
    if text.startswith("|") and text.endswith("|") and len(text) >= 2:
        return text[1:-1].strip()

    # Strip matching bracket pairs (1 or 2 chars on each side)
    pairs = [
        ("{{", "}}"),   # hexagon
        ("[[", "]]"),   # subroutine
        ("[(", ")]"),   # cylindrical
        ("((", "))"),   # double-circle / bang
        ("[/", "/]"),   # parallelogram alt
        ("[\\", "\\]"), # parallelogram alt
        ("[", "]"),     # rect
        ("(", ")"),     # round
        ("{", "}"),     # rhombus
        ("})", "({"),   # cloud (reversed)
        ("((", "))"),   # double-circle / bang (alt)
    ]
    for open_b, close_b in pairs:
        if text.startswith(open_b) and text.endswith(close_b):
            inner = text[len(open_b):-len(close_b)].strip()
            if inner:
                return inner

    # Malformed hexagon: only one closing brace (e.g. "{{Amyloid} Sarcoidosis}")
    if text.startswith("{{") and text.count("}") == 1:
        end = text.index("}")
        return text[2:end].strip()

    # Malformed bracket pair: only one of each (e.g. "[Label with ] inside")
    if text and text[0] in "([{" and text[-1] in ")]}":
        return text[1:-1].strip()

    return text


def normalize_node_id(raw: str) -> str:
    """Convert a mermaid node declaration into a safe Python identifier.

    Mermaid node IDs can be simple ("A") or shaped ("A[Label]"). Returns the
    bare ID portion with non-alphanumerics replaced.
    """
    if raw is None:
        return ""
    text = raw.strip()
    # If it starts with a delimiter, the ID is implicit (auto-assigned by mermaid)
    if text and text[0] in "([{":
        return f"node_{abs(hash(text)) % 100000}"
    # Otherwise extract the leading identifier
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)", text)
    if m:
        return m.group(1)
    return f"node_{abs(hash(text)) % 100000}"


# Pattern that captures a node declaration: optional id + opening delimiters + label + closing delimiters
_NODE_DECL_RE = re.compile(
    r"""^(
        (?P<id>[A-Za-z_][A-Za-z0-9_]*)?     # optional node ID
        \s*
        (?P<open>[\(\[\{]{1,2})             # 1 or 2 opening brackets
        \s*
        (?P<label>[^()\[\]{}\n]+?)          # label (no nested brackets, no newlines)
        \s*
        (?P<close>[\)\]\}]{1,2})            # 1 or 2 closing brackets
    )$""",
    re.VERBOSE,
)


def parse_node_decl(decl: str) -> dict | None:
    """Parse a single node declaration like 'A[Start]' or '{{Hexagon}}'.

    Returns {"id": str|None, "label": str, "shape": str, "delimiters": tuple}
    or None if unparseable.

    Shape names:
      - "default"    text
      - "rect"       [text]
      - "round"      (text)
      - "rhombus"    {text}
      - "hexagon"    {{text}}
      - "bang"       ((text))
      - "cylindrical" [(text)]
      - "subroutine" [[text]]
      - "parallelogram" [/text/] or [\\text\\]
    """
    if decl is None:
        return None
    text = decl.strip()
    if not text:
        return None

    m = _NODE_DECL_RE.match(text)
    if not m:
        # Try harder: malformed hexagon like '{{X}'
        if text.startswith("{{") and "}" in text[2:]:
            end = text.index("}", 2)
            return {
                "id": None,
                "label": text[2:end].strip(),
                "shape": "hexagon",
                "delimiters": ("{{", "}"),
            }
        # Try even harder: just brackets, ignore ID
        if text[0] in "([{" and text[-1] in ")]}":
            return {
                "id": None,
                "label": extract_label(text),
                "shape": "unknown",
                "delimiters": (text[0], text[-1]),
            }
        return None

    node_id = m.group("id")
    label = m.group("label").strip()
    open_d, close_d = m.group("open"), m.group("close")

    shape_map = {
        ("[", "]"): "rect",
        ("(", ")"): "round",
        ("{", "}"): "rhombus",
        ("{{", "}}"): "hexagon",
        ("((", "))"): "bang",
        ("[(", ")]"): "cylindrical",
        ("[[", "]]"): "subroutine",
    }
    shape = shape_map.get((open_d, close_d), "unknown")

    return {
        "id": node_id,
        "label": label,
        "shape": shape,
        "delimiters": (open_d, close_d),
    }


# ----- Verification fixtures -----

FIXTURES = [
    # (input, expected_label, description)
    ("Amyloid", "Amyloid", "default text"),
    ("[Amyloid]", "Amyloid", "rect"),
    ("(Amyloid)", "Amyloid", "round"),
    ("{Amyloid}", "Amyloid", "rhombus"),
    ("{{Hexagon Topic}}", "Hexagon Topic", "hexagon"),
    ("((Bang shape))", "Bang shape", "bang / double-circle"),
    ("|edge label|", "edge label", "edge label"),
    ("[Line 1\nLine 2]", "Line 1 Line 2", "multi-line node"),
    ("{{Missing", "Missing", "malformed hexagon (regex fallback)"),
    ("[Label with ] inside", "Label with ] inside", "loose brackets"),
    ("[/Parallel/]", "Parallel", "parallelogram"),
    ("", "", "empty string"),
]


def run_fixtures():
    """Run all fixtures and print pass/fail."""
    passed = 0
    failed = 0
    for raw, expected, desc in FIXTURES:
        got = extract_label(raw)
        ok = got == expected
        mark = "✓" if ok else "✗"
        if ok:
            passed += 1
        else:
            failed += 1
            print(f"{mark} {desc}: input={raw!r} expected={expected!r} got={got!r}")
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(0 if run_fixtures() else 1)
    # Demo
    print("extract_label examples:")
    for raw, _, desc in FIXTURES[:8]:
        print(f"  {raw!r:30} -> {extract_label(raw)!r:25} ({desc})")
    print("\nRun with --test to verify all fixtures")
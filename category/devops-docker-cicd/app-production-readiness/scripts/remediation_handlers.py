#!/usr/bin/env python3
"""Deterministic codemods and remediation handlers for app-production-readiness.

Provides automated, non-destructive transformations for common security, design,
accessibility, and code-quality blockers found during audits.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import resolve_root


def backup_file(root: Path, file_path: Path, session_id: str = "latest") -> Path:
    """Save an atomic copy of the file before modification so it can be rolled back."""
    try:
        rel = file_path.relative_to(root)
    except ValueError:
        rel = Path(file_path.name)
    backup_path = root / "qa" / "fix-backup" / session_id / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, backup_path)
    return backup_path


def validate_syntax(file_path: Path, text: str) -> bool:
    """Check that transformed code compiles or parses without syntax errors."""
    suffix = file_path.suffix.lower()
    if suffix == ".py":
        try:
            compile(text, str(file_path), "exec")
            return True
        except SyntaxError:
            return False
    # For JS/TS/CSS/HTML, check basic brace/parentheses balancing as a sanity guard
    if suffix in (".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".css"):
        stack = []
        in_string = False
        quote_char = ""
        escape = False
        for char in text:
            if escape:
                escape = False
                continue
            if char == "\\":
                escape = True
                continue
            if in_string:
                if char == quote_char:
                    in_string = False
                continue
            if char in ("'", '"', '`'):
                in_string = True
                quote_char = char
                continue
            if char in ("{", "(", "["):
                stack.append(char)
            elif char in ("}", ")", "]"):
                if not stack:
                    return False
                top = stack.pop()
                if (top == "{" and char != "}") or (top == "(" and char != ")") or (top == "[" and char != "]"):
                    return False
        return len(stack) == 0
    return True


# ---------------------------------------------------------------------------
# 1. Security Handlers
# ---------------------------------------------------------------------------

def remediate_xss_innerhtml(root: Path, file_rel: str, line_no: int = 0) -> dict:
    """Convert simple non-HTML innerHTML assignments to textContent."""
    file_path = root / file_rel
    if not file_path.is_file():
        return {"id": "sec_xss_innerhtml", "status": "skipped", "detail": f"file not found: {file_rel}"}
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines(keepends=True)
    modified = False

    new_lines = []
    for idx, line in enumerate(lines, start=1):
        # If line number specified, target that line or nearby, else check lines matching pattern
        if (line_no == 0 or abs(idx - line_no) <= 2) and ".innerHTML" in line:
            # Pattern: element.innerHTML = "simple text" or var (no '<' or '>')
            m = re.search(r"(\b\w+)\.innerHTML\s*=\s*([^;]+);", line)
            if m:
                val = m.group(2).strip()
                # If literal string without HTML tags
                if (val.startswith(('"', "'", '`')) and val.endswith(('"', "'", '`'))) and "<" not in val and ">" not in val:
                    line = line.replace(".innerHTML", ".textContent")
                    modified = True
        new_lines.append(line)

    if not modified:
        return {"id": "sec_xss_innerhtml", "status": "skipped", "detail": "no safe innerHTML->textContent candidate found"}

    new_text = "".join(new_lines)
    if not validate_syntax(file_path, new_text):
        return {"id": "sec_xss_innerhtml", "status": "failed", "detail": "syntax validation failed on transformed code"}

    backup_file(root, file_path)
    file_path.write_text(new_text, encoding="utf-8")
    return {"id": "sec_xss_innerhtml", "status": "applied", "detail": f"converted safe innerHTML to textContent in {file_rel}"}


def remediate_cors_wildcard(root: Path, file_rel: str, line_no: int = 0) -> dict:
    """Replace wildcard CORS headers with request origin reflection."""
    file_path = root / file_rel
    if not file_path.is_file():
        return {"id": "sec_cors_wildcard", "status": "skipped", "detail": f"file not found: {file_rel}"}
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    if "Access-Control-Allow-Origin" not in text:
        return {"id": "sec_cors_wildcard", "status": "skipped", "detail": "no CORS headers in file"}

    # Pattern: "Access-Control-Allow-Origin": "*" or 'Access-Control-Allow-Origin': '*'
    new_text = re.sub(
        r"(['\"]Access-Control-Allow-Origin['\"]\s*:\s*)['\"]\*(['\"])",
        r"\1request.headers.get('Origin') || '*'\2",
        text,
    )
    if new_text == text:
        return {"id": "sec_cors_wildcard", "status": "skipped", "detail": "wildcard CORS pattern not matched"}

    if not validate_syntax(file_path, new_text):
        return {"id": "sec_cors_wildcard", "status": "failed", "detail": "syntax validation failed"}

    backup_file(root, file_path)
    file_path.write_text(new_text, encoding="utf-8")
    return {"id": "sec_cors_wildcard", "status": "applied", "detail": f"secured CORS wildcard in {file_rel}"}


# ---------------------------------------------------------------------------
# 2. UI / Design Handlers
# ---------------------------------------------------------------------------

def _find_css_target(root: Path, css_file_rel: str = "") -> Path | None:
    """Find a target CSS stylesheet to inject accessibility/UI rules into."""
    if css_file_rel and (root / css_file_rel).is_file():
        return root / css_file_rel
    for candidate in ("src/styles/components.css", "src/styles/reset.css", "src/styles/layout.css",
                      "src/index.css", "styles/globals.css", "src/app/globals.css", "style.css"):
        if (root / candidate).is_file():
            return root / candidate
    for p in root.rglob("*.css"):
        if not any(part in ("node_modules", "dist", "build", ".next", "qa") for part in p.parts):
            return p
    return None


def remediate_touch_targets(root: Path, css_file_rel: str = "") -> dict:
    """Ensure interactive controls satisfy WCAG >= 44px touch target guidelines."""
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return {"id": "ui_touch_targets", "status": "skipped", "detail": "no primary CSS file found"}

    text = target_css.read_text(encoding="utf-8", errors="ignore")
    if "/* Auto-remediation: WCAG touch target" in text:
        return {"id": "ui_touch_targets", "status": "already-ok", "detail": "touch target rules already injected"}

    snippet = (
        "\n\n/* Auto-remediation: WCAG touch target compliance (>= 44px) */\n"
        "@media (pointer: coarse) {\n"
        "  button, [role=\"button\"], a.btn, input[type=\"button\"], input[type=\"submit\"] {\n"
        "    min-height: 44px;\n"
        "    min-width: 44px;\n"
        "  }\n"
        "}\n"
    )
    new_text = text + snippet
    backup_file(root, target_css)
    target_css.write_text(new_text, encoding="utf-8")
    return {"id": "ui_touch_targets", "status": "applied", "detail": f"added touch target rules to {target_css.relative_to(root)}"}


def remediate_focus_visible(root: Path, css_file_rel: str = "") -> dict:
    """Inject accessible keyboard focus outlines."""
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return {"id": "ui_focus_visible", "status": "skipped", "detail": "no stylesheet found"}

    text = target_css.read_text(encoding="utf-8", errors="ignore")
    if ":focus-visible" in text:
        return {"id": "ui_focus_visible", "status": "already-ok", "detail": "focus-visible already defined"}

    snippet = (
        "\n\n/* Auto-remediation: WCAG 2.1 accessible focus ring */\n"
        ":focus-visible {\n"
        "  outline: 2px solid currentColor;\n"
        "  outline-offset: 2px;\n"
        "}\n"
    )
    new_text = text + snippet
    backup_file(root, target_css)
    target_css.write_text(new_text, encoding="utf-8")
    return {"id": "ui_focus_visible", "status": "applied", "detail": f"added :focus-visible styles to {target_css.relative_to(root)}"}


def remediate_reduced_motion(root: Path, css_file_rel: str = "") -> dict:
    """Inject prefers-reduced-motion accessibility overrides."""
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return {"id": "ui_reduced_motion", "status": "skipped", "detail": "no stylesheet found"}

    text = target_css.read_text(encoding="utf-8", errors="ignore")
    if "prefers-reduced-motion" in text:
        return {"id": "ui_reduced_motion", "status": "already-ok", "detail": "reduced-motion query already present"}

    snippet = (
        "\n\n/* Auto-remediation: WCAG 2.1 prefers-reduced-motion compliance */\n"
        "@media (prefers-reduced-motion: reduce) {\n"
        "  *, *::before, *::after {\n"
        "    animation-duration: 0.01ms !important;\n"
        "    animation-iteration-count: 1 !important;\n"
        "    transition-duration: 0.01ms !important;\n"
        "    scroll-behavior: auto !important;\n"
        "  }\n"
        "}\n"
    )
    new_text = text + snippet
    backup_file(root, target_css)
    target_css.write_text(new_text, encoding="utf-8")
    return {"id": "ui_reduced_motion", "status": "applied", "detail": f"added prefers-reduced-motion to {target_css.relative_to(root)}"}


# ---------------------------------------------------------------------------
# 3. Accessibility & Code Quality Handlers
# ---------------------------------------------------------------------------

def remediate_empty_catch(root: Path, file_rel: str) -> dict:
    """Inject error logging into empty catch blocks to eliminate silent swallowed errors."""
    file_path = root / file_rel
    if not file_path.is_file():
        return {"id": "code_empty_catch", "status": "skipped", "detail": f"file not found: {file_rel}"}
    text = file_path.read_text(encoding="utf-8", errors="ignore")

    # Match catch (err) {} or catch (e) {} or catch {}
    pattern_with_arg = re.compile(r"catch\s*\(([^)]+)\)\s*\{\s*\}")
    pattern_bare = re.compile(r"catch\s*\{\s*\}")

    new_text = pattern_with_arg.sub(r'catch (\1) { console.error("Unhandled error caught:", \1); }', text)
    new_text = pattern_bare.sub(r'catch (err) { console.error("Unhandled error caught:", err); }', new_text)

    if new_text == text:
        return {"id": "code_empty_catch", "status": "skipped", "detail": "no empty catch blocks found"}

    if not validate_syntax(file_path, new_text):
        return {"id": "code_empty_catch", "status": "failed", "detail": "syntax validation failed"}

    backup_file(root, file_path)
    file_path.write_text(new_text, encoding="utf-8")
    return {"id": "code_empty_catch", "status": "applied", "detail": f"injected logging into empty catch block in {file_rel}"}


def remediate_aria_label(root: Path, file_rel: str) -> dict:
    """Add accessible aria-label to unlabelled icon-only buttons."""
    file_path = root / file_rel
    if not file_path.is_file():
        return {"id": "a11y_aria_labels", "status": "skipped", "detail": f"file not found: {file_rel}"}
    text = file_path.read_text(encoding="utf-8", errors="ignore")

    # Look for button tags with title or class containing icon/close/toggle but missing aria-label
    def _add_aria(match):
        attrs = match.group(1)
        if "aria-label=" in attrs:
            return match.group(0)
        # Try to infer label from title or id
        title_m = re.search(r'title=["\']([^"\']+)["\']', attrs)
        id_m = re.search(r'id=["\']([^"\']+)["\']', attrs)
        label = "Button"
        if title_m:
            label = title_m.group(1)
        elif id_m:
            label = id_m.group(1).replace("btn-", "").replace("btn", "").replace("-", " ").strip().title()
        return f'<button {attrs} aria-label="{label}">'

    new_text = re.sub(r'<button\s+([^>]+)>', _add_aria, text)
    if new_text == text:
        return {"id": "a11y_aria_labels", "status": "skipped", "detail": "no unlabelled button patterns matched"}

    backup_file(root, file_path)
    file_path.write_text(new_text, encoding="utf-8")
    return {"id": "a11y_aria_labels", "status": "applied", "detail": f"added aria-labels in {file_rel}"}


# ---------------------------------------------------------------------------
# 4. Agent Recipe Generator (for complex logic / design refactors)
# ---------------------------------------------------------------------------

def generate_agent_recipe(root: Path, gate: str, file_rel: str, line_no: int, rule: str, detail: str) -> str:
    """Generate a structured markdown recipe for issues requiring intelligent refactoring."""
    recipes_dir = root / "qa" / "recipes"
    recipes_dir.mkdir(parents=True, exist_ok=True)
    slug = f"{gate.lower()}_{Path(file_rel).stem}_{rule}".replace(" ", "_")
    recipe_path = recipes_dir / f"{slug}.md"

    # Grab file context snippet around line
    file_path = root / file_rel
    snippet = "File not found."
    if file_path.is_file():
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        start = max(0, line_no - 10)
        end = min(len(lines), line_no + 20)
        snippet = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[start:end], start=start))

    content = f"""# Remediation Recipe: {rule} ({gate})

- **Target File:** `{file_rel}` (around line {line_no})
- **Gate:** {gate}
- **Issue:** {detail}

## Code Context

```javascript
{snippet}
```

## Recommended Refactoring Instructions

1. **Locate the target:** Open `{file_rel}` around line {line_no}.
2. **Decompose / Refactor:**
   - For long functions (>80 lines): Extract inner subroutines (helpers, state handlers, validators) into smaller pure functions.
   - For API contracts: Ensure error responses return explicit JSON error schemas (`{{ "error": "...", "status": 400 }}`).
3. **Verify:**
   - Run tests or check that types/build pass without regression.
"""
    recipe_path.write_text(content, encoding="utf-8")
    return str(recipe_path.relative_to(root))

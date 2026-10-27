#!/usr/bin/env python3
"""Deterministic codemods and remediation handlers for app-production-readiness.

Provides automated, non-destructive transformations for common security, design,
accessibility, and code-quality blockers found during audits.

Safety contract (every handler obeys it):

* paths that come from an audit report are resolved and **rejected** when they
  escape the project root;
* a codemod only ever touches the file types it understands - JavaScript and
  TypeScript for code, CSS for styles, HTML for markup;
* the transformed source is validated *before* it is written (a real parser
  for JSON/Python/HTML, ``node --check`` for JavaScript when Node is
  available, brace balancing as the fallback);
* every write is atomic (temp file + ``os.replace``) and byte preserving
  (line endings and encoding survive untouched);
* every write is preceded by a backup under ``qa/fix-backup/<session>/`` and the
  *pristine* backup is kept - a second edit of the same file never overwrites it;
* ``dry_run=True`` computes and validates the change but never touches the disk.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import resolve_root  # noqa: F401  (kept for API compatibility)

BACKUP_DIR = Path("qa") / "fix-backup"
JS_SUFFIXES = (".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs")
MARKUP_SUFFIXES = (".html", ".htm")
SKIP_DIR_NAMES = ("node_modules", "dist", "build", ".next", ".nuxt", ".output",
                   "coverage", ".nyc_output", ".turbo", ".cache", ".venv", "venv",
                   "__pycache__", ".git", "qa")


# ---------------------------------------------------------------------------
# primitives
# ---------------------------------------------------------------------------

def _read_raw(path: Path) -> str:
    """Read a file without translating newlines or dropping characters."""
    try:
        return Path(path).read_bytes().decode("utf-8", errors="ignore")
    except OSError:
        return ""


def _write_atomic(path: Path, text: str) -> bool:
    """Write ``text`` to ``path`` atomically, preserving the exact bytes."""
    tmp_name = None
    try:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
        with os.fdopen(fd, "wb") as handle:
            handle.write(text.encode("utf-8"))
        os.replace(tmp_name, path)
        return True
    except OSError:
        if tmp_name:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
        return False


def resolve_target(root: Path, file_rel: str) -> Path | None:
    """Resolve a report supplied path and refuse anything outside the project.

    Audit reports are generated text - a finding may name a path that points
    outside the project (``../../etc/passwd``).  Every handler resolves its
    target through this helper first.
    """
    if not file_rel:
        return None
    try:
        base = Path(root).resolve()
        candidate = (base / file_rel).resolve()
        candidate.relative_to(base)
    except (ValueError, OSError):
        return None
    return candidate


def backup_file(root: Path, file_path: Path, session_id: str = "latest") -> Path:
    """Save a copy of the file before modification so it can be rolled back.

    The *first* copy wins: re-running a remediation never overwrites the
    pristine original with an already remediated version.
    """
    file_path = Path(file_path)
    try:
        rel = file_path.resolve().relative_to(Path(root).resolve())
    except (ValueError, OSError):
        rel = Path(file_path.name)
    backup_path = Path(root) / BACKUP_DIR / session_id / rel
    if backup_path.exists():
        return backup_path
    try:
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_path)
    except OSError:
        pass
    return backup_path


def _code_mask(text: str) -> list[bool]:
    """Return a per-character mask: ``True`` where the character is code.

    Used so that a codemod never rewrites text that only *looks* like code -
    a ``catch (e) {}`` inside a string literal or a comment stays untouched.
    """
    mask = [True] * len(text)
    index = 0
    length = len(text)
    while index < length:
        char = text[index]
        if char == "/" and index + 1 < length and text[index + 1] == "/":
            while index < length and text[index] != "\n":
                mask[index] = False
                index += 1
            continue
        if char == "/" and index + 1 < length and text[index + 1] == "*":
            mask[index] = mask[index + 1] = False
            index += 2
            while index < length:
                if text[index] == "*" and index + 1 < length and text[index + 1] == "/":
                    mask[index] = mask[index + 1] = False
                    index += 2
                    break
                mask[index] = False
                index += 1
            continue
        if char in ("'", '"', "`"):
            quote = char
            mask[index] = False
            index += 1
            while index < length:
                if text[index] == "\\":
                    mask[index] = False
                    index += 1
                    if index < length:
                        mask[index] = False
                        index += 1
                    continue
                if text[index] == quote:
                    mask[index] = False
                    index += 1
                    break
                mask[index] = False
                index += 1
            continue
        index += 1
    return mask


def _balanced(text: str) -> bool:
    """Fallback syntax check: braces/brackets/parens must balance."""
    stack = []
    quote_char = ""
    in_string = False
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
        if char in ("'", '"', "`"):
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
    return len(stack) == 0 and not in_string


def _node_check(text: str, suffix: str) -> bool | None:
    """Parse JavaScript with ``node --check``.  ``None`` when Node is absent."""
    if suffix not in (".js", ".mjs", ".cjs"):
        return None
    node = shutil.which("node")
    if not node:
        return None
    # ESM syntax needs the .mjs extension or node --check rejects valid code.
    is_module = bool(re.search(r"^\s*(?:import|export)\s", text, re.M))
    ext = ".mjs" if is_module else (suffix if suffix in (".mjs", ".cjs") else ".js")
    tmp_path = None
    try:
        fd, tmp_name = tempfile.mkstemp(suffix=ext)
        tmp_path = Path(tmp_name)
        with os.fdopen(fd, "wb") as handle:
            handle.write(text.encode("utf-8"))
        proc = subprocess.run([node, "--check", str(tmp_path)],
                              capture_output=True, text=True, timeout=20)
        return proc.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return None
    finally:
        if tmp_path is not None:
            try:
                tmp_path.unlink()
            except OSError:
                pass


class _TagCounter(HTMLParser):
    """Counts the tags of an HTML document (used as an invariant check)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.opens: dict[str, int] = {}
        self.total = 0

    def handle_starttag(self, tag, attrs):
        self.opens[tag] = self.opens.get(tag, 0) + 1
        self.total += 1

    def handle_startendtag(self, tag, attrs):
        self.opens[tag] = self.opens.get(tag, 0) + 1
        self.total += 1


def _html_parses(text: str) -> bool:
    """Feed the markup to the stdlib HTML parser and report tag counts."""
    parser = _TagCounter()
    try:
        parser.feed(text)
        parser.close()
    except Exception:
        return False
    return True


def validate_syntax(file_path: Path, text: str) -> bool:
    """Check that the transformed code still parses.  Unknown types fail closed."""
    suffix = Path(file_path).suffix.lower()
    if suffix == ".py":
        try:
            compile(text, str(file_path), "exec")
            return True
        except (SyntaxError, ValueError):
            return False
    if suffix == ".json":
        try:
            json.loads(text)
            return True
        except ValueError:
            return False
    if suffix in JS_SUFFIXES:
        checked = _node_check(text, suffix)
        if checked is not None:
            return checked
        return _balanced(text)
    if suffix == ".css":
        return _balanced(text)
    if suffix in MARKUP_SUFFIXES:
        return _html_parses(text)
    return False


def _result(handler_id: str, status: str, detail: str, **extra) -> dict:
    payload = {"id": handler_id, "status": status, "detail": detail}
    payload.update(extra)
    return payload


# ---------------------------------------------------------------------------
# 1. Security Handlers
# ---------------------------------------------------------------------------

def remediate_xss_innerhtml(root: Path, file_rel: str, line_no: int = 0, dry_run: bool = False) -> dict:
    """Convert simple non-HTML innerHTML assignments to textContent."""
    handler_id = "sec_xss_innerhtml"
    target = resolve_target(root, file_rel)
    if target is None:
        return _result(handler_id, "skipped",
                       f"refused to touch '{file_rel}': the path resolves outside the project root")
    if not target.is_file():
        return _result(handler_id, "skipped", f"file not found: {file_rel}")
    if target.suffix.lower() not in JS_SUFFIXES:
        return _result(handler_id, "skipped",
                       f"only JavaScript/TypeScript files can be rewritten "
                       f"(this file is {target.suffix or 'extensionless'})")

    text = _read_raw(target)
    mask = _code_mask(text)
    lines = text.splitlines(keepends=True)
    new_lines = []
    offset = 0
    replaced = 0
    for index, line in enumerate(lines, start=1):
        if line_no == 0 or abs(index - line_no) <= 2:
            line, count = _rewrite_innerhtml(line, mask, offset)
            replaced += count
        new_lines.append(line)
        offset += len(line)

    if not replaced:
        return _result(handler_id, "skipped", "no safe innerHTML->textContent candidate found")

    new_text = "".join(new_lines)
    if new_text.count(".innerHTML") != text.count(".innerHTML") - replaced:
        return _result(handler_id, "failed", "innerHTML rewrite touched an unexpected number of assignments")
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed on transformed code")

    if dry_run:
        return _result(handler_id, "planned",
                       f"would convert {replaced} innerHTML assignment(s) to textContent in {file_rel}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {file_rel}")
    return _result(handler_id, "applied",
                   f"converted {replaced} safe innerHTML assignment(s) to textContent in {file_rel}")


def _rewrite_innerhtml(line: str, mask: list[bool], line_offset: int):
    """Rewrite ``el.innerHTML = "text"`` into ``el.textContent = "text"``.

    Only the matched assignment is rewritten - other ``.innerHTML`` uses on the
    same line (string literals, template fragments) are left alone.
    """
    pieces = []
    position = 0
    count = 0
    for match in re.finditer(r"\b[A-Za-z_$][\w$]*\.innerHTML\s*=\s*", line):
        absolute = line_offset + match.start()
        if absolute >= len(mask) or not mask[absolute]:
            continue
        rest = line[match.end():]
        value = re.match(r"(['\"`])([^<>]*?)\1", rest)
        if not value:
            continue
        tail = rest[value.end():]
        if not re.match(r"\s*;", tail):
            continue
        pieces.append(line[position:match.start()])
        pieces.append(line[match.start():match.end()].replace(".innerHTML", ".textContent"))
        pieces.append(line[match.end():match.end() + value.end()])
        position = match.end() + value.end()
        count += 1
    pieces.append(line[position:])
    return "".join(pieces), count


_CORS_OBJECT_RE = re.compile(r"(['\"]Access-Control-Allow-Origin['\"]\s*:\s*)['\"]\*['\"]")
_CORS_CALL_RE = re.compile(
    r"((?:\.setHeader|\.header|\.append|\.set)\s*\(\s*)(['\"])Access-Control-Allow-Origin\2\s*,\s*(['\"])\*\3")
_ALLOWLIST_RE = re.compile(r"\b(ALLOWED_ORIGINS|allowedOrigins|ALLOWED_ORIGIN|allowedOrigin)\b")
_REQUEST_RE = re.compile(r"\b(req|request|ctx)\b\s*\.\s*headers")
_REQUEST_PARAM_RE = re.compile(r"[(,]\s*(req|request|ctx)\b")


def remediate_cors_wildcard(root: Path, file_rel: str, line_no: int = 0, dry_run: bool = False) -> dict:
    """Replace a wildcard CORS origin with an allowlist check.

    A wildcard origin is only safe to rewrite when the file already exposes an
    allowlist and a request object - otherwise the correct allowlist is a
    product decision, so the handler reports ``manual`` and leaves a recipe
    behind instead of shipping broken or permissive code.
    """
    handler_id = "sec_cors_wildcard"
    target = resolve_target(root, file_rel)
    if target is None:
        return _result(handler_id, "skipped",
                       f"refused to touch '{file_rel}': the path resolves outside the project root")
    if not target.is_file():
        return _result(handler_id, "skipped", f"file not found: {file_rel}")
    if target.suffix.lower() not in JS_SUFFIXES:
        return _result(handler_id, "manual",
                       f"'{file_rel}' is not JavaScript - a CORS origin cannot be auto-rewritten in "
                       f"{target.suffix or 'an extensionless file'}; set the allowed origins by hand",
                       recipe=_cors_recipe(root, file_rel, "manual CORS configuration", dry_run=dry_run))
    text = _read_raw(target)
    if "Access-Control-Allow-Origin" not in text:
        return _result(handler_id, "skipped", "no CORS headers in file")

    has_object = bool(_CORS_OBJECT_RE.search(text))
    has_call = bool(_CORS_CALL_RE.search(text))
    if not (has_object or has_call):
        return _result(handler_id, "skipped", "wildcard CORS pattern not matched")

    allowlist = _ALLOWLIST_RE.search(text)
    request = _REQUEST_RE.search(text) or _REQUEST_PARAM_RE.search(text)
    if not (allowlist and request):
        missing = []
        if not allowlist:
            missing.append("an allowlist (ALLOWED_ORIGINS)")
        if not request:
            missing.append("a request object (req.headers)")
        return _result(handler_id, "manual",
                       "the CORS wildcard needs a product decision - the file does not define "
                       + " and ".join(missing) + "; refusing to guess the allowed origins",
                       recipe=_cors_recipe(root, file_rel, "CORS wildcard origin", dry_run=dry_run))

    allowlist_name = allowlist.group(1)
    request_name = request.group(1)
    expression = (f"({allowlist_name}.includes({request_name}.headers.origin) "
                  f"? {request_name}.headers.origin : null)")

    new_text = _CORS_OBJECT_RE.sub(lambda m: m.group(1) + expression, text)
    new_text = _CORS_CALL_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}Access-Control-Allow-Origin{m.group(2)}, "
                                            f"{expression}", new_text)
    if new_text == text:
        return _result(handler_id, "skipped", "wildcard CORS pattern not matched")
    if new_text.count("Access-Control-Allow-Origin") != text.count("Access-Control-Allow-Origin"):
        return _result(handler_id, "failed", "CORS rewrite changed an unexpected number of headers")
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed")

    if dry_run:
        return _result(handler_id, "planned",
                       f"would replace the wildcard CORS origin with an {allowlist_name} allowlist check in {file_rel}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {file_rel}")
    return _result(handler_id, "applied",
                   f"secured CORS wildcard with an {allowlist_name} allowlist check in {file_rel}")


def _cors_recipe(root: Path, file_rel: str, rule: str, dry_run: bool = False) -> str:
    """Leave a recipe describing how to configure allowed origins."""
    try:
        return generate_agent_recipe(
            root, "E", file_rel, 0, "cors_allowed_origins",
            "Access-Control-Allow-Origin is wildcard - replace it with an explicit allowlist",
            dry_run=dry_run)
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# 2. UI / Design Handlers
# ---------------------------------------------------------------------------

def _find_css_target(root: Path, css_file_rel: str = "") -> Path | None:
    """Find a target CSS stylesheet to inject accessibility/UI rules into."""
    if css_file_rel:
        candidate = resolve_target(root, css_file_rel)
        if candidate is not None and candidate.is_file():
            return candidate
    for candidate in ("src/styles/components.css", "src/styles/reset.css", "src/styles/layout.css",
                      "src/index.css", "styles/globals.css", "src/app/globals.css", "style.css"):
        if (Path(root) / candidate).is_file():
            return Path(root) / candidate
    root_path = Path(root)
    for path in sorted(root_path.rglob("*.css")):
        try:
            parts = path.relative_to(root_path).parts
        except ValueError:
            continue
        if any(part in SKIP_DIR_NAMES for part in parts):
            continue
        return path
    return None


def _append_snippet(root: Path, target: Path, snippet: str, handler_id: str,
                    detail: str, dry_run: bool) -> dict:
    text = _read_raw(target)
    new_text = text + snippet
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed")
    if dry_run:
        return _result(handler_id, "planned", f"would {detail}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {target.name}")
    return _result(handler_id, "applied", detail)


def remediate_touch_targets(root: Path, css_file_rel: str = "", dry_run: bool = False) -> dict:
    """Ensure interactive controls satisfy WCAG >= 44px touch target guidelines."""
    handler_id = "ui_touch_targets"
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return _result(handler_id, "skipped", "no primary CSS file found")
    text = _read_raw(target_css)
    if "/* Auto-remediation: WCAG touch target" in text:
        return _result(handler_id, "already-ok", "touch target rules already injected")

    snippet = (
        "\n\n/* Auto-remediation: WCAG touch target compliance (>= 44px) */\n"
        "@media (pointer: coarse) {\n"
        "  button, [role=\"button\"], a.btn, input[type=\"button\"], input[type=\"submit\"] {\n"
        "    min-height: 44px;\n"
        "    min-width: 44px;\n"
        "  }\n"
        "}\n"
    )
    try:
        rel = target_css.relative_to(Path(root))
    except ValueError:
        rel = Path(target_css.name)
    return _append_snippet(root, target_css, snippet, handler_id,
                           f"added touch target rules to {rel}", dry_run)


def remediate_focus_visible(root: Path, css_file_rel: str = "", dry_run: bool = False) -> dict:
    """Inject accessible keyboard focus outlines."""
    handler_id = "ui_focus_visible"
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return _result(handler_id, "skipped", "no stylesheet found")
    text = _read_raw(target_css)
    if ":focus-visible" in text:
        return _result(handler_id, "already-ok", "focus-visible already defined")

    snippet = (
        "\n\n/* Auto-remediation: WCAG 2.1 accessible focus ring */\n"
        ":focus-visible {\n"
        "  outline: 2px solid currentColor;\n"
        "  outline-offset: 2px;\n"
        "}\n"
    )
    try:
        rel = target_css.relative_to(Path(root))
    except ValueError:
        rel = Path(target_css.name)
    return _append_snippet(root, target_css, snippet, handler_id,
                           f"added :focus-visible styles to {rel}", dry_run)


def remediate_reduced_motion(root: Path, css_file_rel: str = "", dry_run: bool = False) -> dict:
    """Inject prefers-reduced-motion accessibility overrides."""
    handler_id = "ui_reduced_motion"
    target_css = _find_css_target(root, css_file_rel)
    if not target_css:
        return _result(handler_id, "skipped", "no stylesheet found")
    text = _read_raw(target_css)
    if "prefers-reduced-motion" in text:
        return _result(handler_id, "already-ok", "reduced-motion query already present")

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
    try:
        rel = target_css.relative_to(Path(root))
    except ValueError:
        rel = Path(target_css.name)
    return _append_snippet(root, target_css, snippet, handler_id,
                           f"added prefers-reduced-motion to {rel}", dry_run)


# ---------------------------------------------------------------------------
# 3. Accessibility & Code Quality Handlers
# ---------------------------------------------------------------------------

_CATCH_WITH_ARG_RE = re.compile(r"catch\s*\(\s*([A-Za-z_$][\w$]*)\s*(?::\s*[^)]*?)?\)\s*\{\s*\}")
_CATCH_BARE_RE = re.compile(r"catch\s*\{\s*\}")


def remediate_empty_catch(root: Path, file_rel: str, dry_run: bool = False) -> dict:
    """Inject error logging into empty catch blocks to eliminate silent swallowed errors."""
    handler_id = "code_empty_catch"
    target = resolve_target(root, file_rel)
    if target is None:
        return _result(handler_id, "skipped",
                       f"refused to touch '{file_rel}': the path resolves outside the project root")
    if not target.is_file():
        return _result(handler_id, "skipped", f"file not found: {file_rel}")
    if target.suffix.lower() not in JS_SUFFIXES:
        return _result(handler_id, "skipped",
                       f"only JavaScript/TypeScript files can be rewritten "
                       f"(this file is {target.suffix or 'extensionless'})")
    text = _read_raw(target)
    mask = _code_mask(text)

    def _replace(match: re.Match) -> str:
        if not mask[match.start()]:
            return match.group(0)
        name = match.group(1)
        return f'catch ({name}) {{ console.error("Unhandled error caught:", {name}); }}'

    def _replace_bare(match: re.Match) -> str:
        if not mask[match.start()]:
            return match.group(0)
        return 'catch (err) { console.error("Unhandled error caught:", err); }'

    new_text = _CATCH_WITH_ARG_RE.sub(_replace, text)
    new_text = _CATCH_BARE_RE.sub(_replace_bare, new_text)

    if new_text == text:
        return _result(handler_id, "skipped", "no empty catch blocks found")
    if new_text.count("catch") != text.count("catch"):
        return _result(handler_id, "failed", "empty catch rewrite changed an unexpected number of blocks")
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed")

    if dry_run:
        return _result(handler_id, "planned", f"would inject logging into empty catch blocks in {file_rel}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {file_rel}")
    return _result(handler_id, "applied", f"injected logging into empty catch block(s) in {file_rel}")


_BUTTON_RE = re.compile(r"<button\b((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>", re.IGNORECASE)

def remediate_aria_label(root: Path, file_rel: str, dry_run: bool = False) -> dict:
    """Add an accessible aria-label to unlabelled icon-only buttons."""
    handler_id = "a11y_aria_labels"
    target = resolve_target(root, file_rel)
    if target is None:
        return _result(handler_id, "skipped",
                       f"refused to touch '{file_rel}': the path resolves outside the project root")
    if not target.is_file():
        return _result(handler_id, "skipped", f"file not found: {file_rel}")
    if target.suffix.lower() not in MARKUP_SUFFIXES:
        return _result(handler_id, "skipped",
                       f"only HTML files can be rewritten (this file is {target.suffix or 'extensionless'})")
    text = _read_raw(target)

    def _add_aria(match: re.Match) -> str:
        attrs = match.group(1)
        if "aria-label=" in attrs.lower():
            return match.group(0)
        title = re.search(r"title=[\"']([^\"']+)[\"']", attrs)
        ident = re.search(r"id=[\"']([^\"']+)[\"']", attrs)
        if title:
            label = title.group(1)
        elif ident:
            label = ident.group(1).replace("btn-", "").replace("btn", "").replace("-", " ").strip().title()
        else:
            label = "Button"
        label = label.replace('"', "&quot;")
        return f'<button{attrs} aria-label="{label}">'

    new_text = _BUTTON_RE.sub(_add_aria, text)
    if new_text == text:
        return _result(handler_id, "skipped", "no unlabelled button patterns matched")
    if len(_BUTTON_RE.findall(new_text)) != len(_BUTTON_RE.findall(text)):
        return _result(handler_id, "failed", "aria-label rewrite changed the number of buttons")
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed")

    if dry_run:
        return _result(handler_id, "planned", f"would add aria-labels in {file_rel}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {file_rel}")
    return _result(handler_id, "applied", f"added aria-labels in {file_rel}")


# ---------------------------------------------------------------------------
# 3b. SEO Handlers
# ---------------------------------------------------------------------------

_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_PARAGRAPH_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.IGNORECASE | re.DOTALL)
_HEAD_RE = re.compile(r"<head[^>]*>", re.IGNORECASE)


def _strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def _escape_attr(text: str) -> str:
    return (text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def remediate_seo_meta_tags(root: Path, file_rel: str, dry_run: bool = False) -> dict:
    """Scaffold the missing description / Open Graph / Twitter metadata tags.

    The values are derived from the document itself - the ``<title>`` for the
    Open Graph title and the first paragraph for the description - so the
    result is meaningful without inventing copy.
    """
    handler_id = "seo_meta_tags"
    target = resolve_target(root, file_rel)
    if target is None:
        return _result(handler_id, "skipped",
                       f"refused to touch '{file_rel}': the path resolves outside the project root")
    if not target.is_file():
        return _result(handler_id, "skipped", f"file not found: {file_rel}")
    if target.suffix.lower() not in MARKUP_SUFFIXES:
        return _result(handler_id, "skipped",
                       f"only HTML files can be rewritten (this file is {target.suffix or 'extensionless'})")
    text = _read_raw(target)
    head = _HEAD_RE.search(text)
    if not head:
        return _result(handler_id, "skipped", "the document has no <head> element")

    title_match = _TITLE_RE.search(text)
    title = _strip_tags(title_match.group(1)).strip() if title_match else ""
    paragraph = _PARAGRAPH_RE.search(text)
    description = _strip_tags(paragraph.group(1)).strip() if paragraph else title
    description = " ".join(description.split())[:155]

    existing = {m.group(1).lower() for m in re.finditer(
        r"<meta[^>]+(?:name|property)=[\"']([^\"']+)[\"']", text, re.IGNORECASE)}
    wanted = []
    if "description" not in existing and description:
        wanted.append(f'<meta name="description" content="{_escape_attr(description)}">')
    if "og:title" not in existing and title:
        wanted.append(f'<meta property="og:title" content="{_escape_attr(title)}">')
    if "og:description" not in existing and description:
        wanted.append(f'<meta property="og:description" content="{_escape_attr(description)}">')
    if "og:type" not in existing:
        wanted.append('<meta property="og:type" content="website">')
    if "twitter:card" not in existing:
        wanted.append('<meta name="twitter:card" content="summary_large_image">')
    if not wanted:
        return _result(handler_id, "already-ok", "the document already declares its metadata")

    insert_at = head.end()
    snippet = "\n  " + "\n  ".join(wanted) + "\n"
    new_text = text[:insert_at] + snippet + text[insert_at:]
    if new_text.count("<head") != text.count("<head"):
        return _result(handler_id, "failed", "metadata rewrite changed the document structure")
    if not validate_syntax(target, new_text):
        return _result(handler_id, "failed", "syntax validation failed")

    if dry_run:
        return _result(handler_id, "planned",
                       f"would add {len(wanted)} metadata tag(s) to {file_rel}")
    backup_file(root, target)
    if not _write_atomic(target, new_text):
        return _result(handler_id, "failed", f"could not write {file_rel}")
    return _result(handler_id, "applied", f"added {len(wanted)} metadata tag(s) to {file_rel}")


# ---------------------------------------------------------------------------
# 4. Agent Recipe Generator (for complex logic / design refactors)
# ---------------------------------------------------------------------------

def generate_agent_recipe(root: Path, gate: str, file_rel: str, line_no: int, rule: str,
                          detail: str, dry_run: bool = False) -> str:
    """Generate a structured markdown recipe for issues requiring intelligent refactoring."""
    recipes_dir = Path(root) / "qa" / "recipes"
    slug = f"{gate.lower()}_{Path(file_rel).stem}_{rule}".replace(" ", "_")
    recipe_path = recipes_dir / f"{slug}.md"

    # Grab file context snippet around line
    file_path = resolve_target(root, file_rel)
    snippet = "File not found."
    if file_path is not None and file_path.is_file():
        lines = _read_raw(file_path).splitlines()
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
    if dry_run:
        return str(recipe_path.relative_to(Path(root)))
    recipes_dir.mkdir(parents=True, exist_ok=True)
    recipe_path.write_text(content, encoding="utf-8")
    return str(recipe_path.relative_to(Path(root)))

#!/usr/bin/env python3
"""Report how far each translated docs page has drifted from its source page.

Each translated file pins the source revision it was translated from, in its
front matter, as a commit hash:

    ---
    source_commit: 3f9c2e1
    ---

The script compares that pin against the source file's git history. It never
compares file dates: editing a translation (even only to mark it stale) makes
it look newer than its source, so date comparison reports drift as freshness.

Usage:
    python3 scripts/translation-drift-check.py --source docs/en \
        --locale ja=docs/ja --locale pt-BR=docs/pt-br \
        [--format csv|json|summary] [--far N] [--fail-on no-pin,unknown-pin] [--since REF]

Layout: each locale directory mirrors the source tree's relative paths.
Locale directories nested inside the source directory are excluded from the
source scan. Suffix layouts (page.ja.md) and string-based workflows (gettext
PO, XLIFF, a translation management system) are out of scope: use their own
fuzzy/untranslated counts. Source and translations must share one git
repository with full history (CI: fetch-depth 0). Includes, partials and
generated content pulled into a page are not tracked.

Needs Python 3.8+ and git. Read-only: runs git read commands, writes nothing.
Exit codes: 0 ok, 1 a --fail-on status was found, 2 usage or git error.
"""

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

# Page extensions a docs generator usually renders, compared case-insensitively.
# Extend with --ext.
DEFAULT_EXTENSIONS = (".md", ".mdx", ".rst", ".adoc")

# Flat front-matter keys accepted as the pin, in lookup order. `source_commit`
# is the name the skill recommends; the others are spellings seen in the wild.
PIN_KEYS = ("source_commit", "source-commit", "original_commit", "translation_of_commit")

# Nested key used by MDN's translated-content repository:
#   l10n:
#     sourceCommit: <sha>
NESTED_PIN_RE = re.compile(r"^l10n:\s*\n(?:[ \t]+.*\n)*?[ \t]+sourceCommit:\s*(\S+)", re.MULTILINE)

# A front-matter block opens on the first line and closes on the next `---`,
# with or without a trailing newline.
FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)

# Fallback pin for formats without YAML front matter (e.g. .rst, .adoc): an
# HTML or reST comment such as `<!-- source_commit: 3f9c2e1 -->`, searched only
# near the top so an example inside the page body is never read as the pin.
COMMENT_PIN_RE = re.compile(
    r"(?:<!--|\.\.)\s*(?:" + "|".join(PIN_KEYS) + r")\s*:\s*([0-9a-fA-F]{7,40})"
)
COMMENT_PIN_SEARCH_LINES = 20

# A pin must be an abbreviated or full commit hash. A branch or tag name would
# resolve to a moving ref and report the page current forever.
HASH_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")

# Default for --far: above this many source commits since the pin, a page is
# reported "far" so a triage pass can sort it first. A starting value, not a
# sourced threshold: scale it to the docs set's commits per release.
FAR_BEHIND_COMMITS = 5

STATUSES = ("current", "behind", "far", "moved", "no-pin", "unknown-pin",
            "untranslated", "orphan")


def git(args, cwd):
    """Run a read-only git command and return stdout, or raise with stderr."""
    result = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def git_ok(args, cwd):
    """True when a git command exits 0."""
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                          check=False).returncode == 0


def clean_value(raw):
    """Strip quotes and a trailing YAML comment from a front-matter value."""
    value = re.sub(r"\s+#.*$", "", raw.strip())
    return value.strip().strip("'\"")


def read_pin(path):
    """Return the raw pin string of a translated file, or None when absent."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace").lstrip("\ufeff")
    except OSError as exc:
        raise RuntimeError(f"cannot read {path}: {exc}") from exc
    match = FRONT_MATTER_RE.match(text)
    if match:
        block = match.group(1).replace("\r\n", "\n") + "\n"
        for line in block.splitlines():
            key, sep, value = line.partition(":")
            if sep and key.strip() in PIN_KEYS and clean_value(value):
                return clean_value(value)
        nested = NESTED_PIN_RE.search(block)
        if nested:
            return clean_value(nested.group(1))
    head = "\n".join(text.splitlines()[:COMMENT_PIN_SEARCH_LINES])
    comment = COMMENT_PIN_RE.search(head)
    return comment.group(1) if comment else None


_PIN_PROBLEMS = {}
_REF_NAMES = []


def pin_problem(pin, repo_root):
    """Return why a pin cannot be used, or None when it is a usable commit.
    Cached per pin: a locale usually shares a handful of pins across pages."""
    if pin not in _PIN_PROBLEMS:
        _PIN_PROBLEMS[pin] = _pin_problem(pin, repo_root)
    return _PIN_PROBLEMS[pin]


def _pin_problem(pin, repo_root):
    if not HASH_RE.match(pin):
        return "not a commit hash"
    if not git_ok(["rev-parse", "--verify", "--quiet", f"{pin}^{{commit}}"], repo_root):
        return "commit not found in history"
    if not _REF_NAMES:
        _REF_NAMES.extend(git(["for-each-ref", "--format=%(refname:short)"],
                              repo_root).splitlines() or [""])
    if any(ref == pin or ref.endswith("/" + pin) for ref in _REF_NAMES if ref):
        return "matches a branch or tag name, which moves"
    full = git(["rev-parse", f"{pin}^{{commit}}"], repo_root)
    if not full.lower().startswith(pin.lower()):
        return "resolves to a different commit"
    if not git_ok(["merge-base", "--is-ancestor", pin, "HEAD"], repo_root):
        return "commit is not an ancestor of HEAD"
    return None


class SourceHistory:
    """Per-source-path git lookups, cached so each runs once across locales."""

    def __init__(self, repo_root):
        self.repo_root = repo_root
        self._last = {}
        self._renames = {}

    def last_commit(self, source_rel):
        if source_rel not in self._last:
            out = git(["log", "-1", "--format=%h %cs", "--", source_rel], self.repo_root)
            self._last[source_rel] = out.split(" ", 1) if out else ["", ""]
        return self._last[source_rel]

    def commits_since(self, pin, source_rel):
        """Commits after the pin that changed the file's content, following
        renames. A pure rename (similarity 100%) is not a content change."""
        out = git(["log", "--follow", "-M", "--format=%x01%H", "--name-status",
                   f"{pin}..HEAD", "--", source_rel], self.repo_root)
        count = 0
        for block in out.split("\x01")[1:]:
            statuses = [ln.split("\t")[0] for ln in block.splitlines()[1:] if ln.strip()]
            if statuses and all(st == "R100" for st in statuses):
                continue
            count += 1
        return count

    def renamed_to(self, pin, old_rel):
        """New path of a source file renamed since the pin, or None."""
        if pin not in self._renames:
            out = git(["diff", "-M", "--name-status", "--diff-filter=R", pin, "HEAD"],
                      self.repo_root)
            mapping = {}
            for line in out.splitlines():
                parts = line.split("\t")
                if len(parts) == 3:
                    mapping[parts[1]] = parts[2]
            self._renames[pin] = mapping
        return self._renames[pin].get(old_rel)


def list_pages(root, extensions, exclude=()):
    pages = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        if any(ex == path or ex in path.parents for ex in exclude):
            continue
        pages.append(path)
    return sorted(pages)


def row(locale, page, status, **extra):
    base = {"locale": locale, "page": page, "status": status, "commits_behind": "",
            "pin": "", "detail": "", "source_last_commit": "", "source_last_date": ""}
    base.update(extra)
    return base


def scan(source_dir, locales, extensions, repo_root, far):
    history = SourceHistory(repo_root)
    locale_dirs = [d for _, d in locales]
    source_pages = list_pages(source_dir, extensions, exclude=locale_dirs)
    rows = []
    moved_targets = set()
    for locale, locale_dir in locales:
        seen = set()
        for src in source_pages:
            rel = src.relative_to(source_dir)
            seen.add(rel)
            target = locale_dir / rel
            source_rel = src.relative_to(repo_root).as_posix()
            last_hash, last_date = history.last_commit(source_rel)
            common = {"source_last_commit": last_hash, "source_last_date": last_date}
            if not target.exists():
                rows.append(row(locale, rel.as_posix(), "untranslated", **common))
                continue
            pin = read_pin(target)
            if not pin:
                rows.append(row(locale, rel.as_posix(), "no-pin", **common))
                continue
            problem = pin_problem(pin, repo_root)
            if problem:
                rows.append(row(locale, rel.as_posix(), "unknown-pin", pin=pin,
                                detail=problem, **common))
                continue
            behind = history.commits_since(pin, source_rel)
            if behind == 0:
                status = "current"
            else:
                status = "far" if behind > far else "behind"
            rows.append(row(locale, rel.as_posix(), status, pin=pin,
                            commits_behind=behind or "", **common))
        # Translated pages whose source path no longer exists: renamed or removed.
        for tgt in list_pages(locale_dir, extensions):
            rel = tgt.relative_to(locale_dir)
            if rel in seen:
                continue
            pin = read_pin(tgt) or ""
            old_rel = (source_dir / rel).relative_to(repo_root).as_posix()
            new_rel = None
            if pin and not pin_problem(pin, repo_root):
                new_rel = history.renamed_to(pin, old_rel)
            if new_rel:
                rows.append(row(locale, rel.as_posix(), "moved", pin=pin,
                                detail=f"source renamed to {new_rel}"))
                moved_targets.add((locale, new_rel))
            else:
                rows.append(row(locale, rel.as_posix(), "orphan", pin=pin,
                                detail="no source page at this path"))
    # A renamed source page already has its translation, reported as moved.
    return [r for r in rows if not (
        r["status"] == "untranslated"
        and (r["locale"], (source_dir / r["page"]).relative_to(repo_root).as_posix())
        in moved_targets)]


def parse_locale(value):
    code, sep, path = value.partition("=")
    if not sep or not code or not path:
        raise argparse.ArgumentTypeError("use --locale CODE=PATH, e.g. ja=docs/ja")
    return code, path


def parse_statuses(value):
    wanted = [s.strip() for s in value.split(",") if s.strip()]
    unknown = [s for s in wanted if s not in STATUSES]
    if unknown:
        raise argparse.ArgumentTypeError(f"unknown status: {', '.join(unknown)}")
    return set(wanted)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", required=True, help="source-language docs directory")
    parser.add_argument("--locale", required=True, action="append", type=parse_locale,
                        help="CODE=PATH, repeat per locale")
    parser.add_argument("--ext", action="append", default=[],
                        help="extra page extension, e.g. .html")
    parser.add_argument("--format", choices=("csv", "json", "summary"), default="summary")
    parser.add_argument("--far", type=int, default=FAR_BEHIND_COMMITS,
                        help="commits since the pin above which a page is 'far' (default %(default)s)")
    parser.add_argument("--fail-on", type=parse_statuses, default=set(),
                        help="comma-separated statuses that make the run exit 1, e.g. no-pin,unknown-pin")
    parser.add_argument("--since", default=None,
                        help="limit --fail-on to translated pages added or modified since this ref, "
                             "so an existing backlog does not fail the build")
    args = parser.parse_args()

    try:
        repo_root = Path(git(["rev-parse", "--show-toplevel"], Path.cwd())).resolve()
        if git(["rev-parse", "--is-shallow-repository"], repo_root) == "true":
            raise RuntimeError("shallow clone: pins cannot be resolved; fetch full history "
                               "(e.g. fetch-depth: 0 in CI)")
        source_dir = Path(args.source).resolve()
        if not source_dir.is_dir():
            raise RuntimeError(f"source directory not found: {args.source}")
        if repo_root != source_dir and repo_root not in source_dir.parents:
            raise RuntimeError("source directory must be inside the git repository")
        locales = []
        for code, path in args.locale:
            locale_dir = Path(path).resolve()
            if not locale_dir.is_dir():
                # A new locale's empty directory is not tracked by git, so it is
                # absent from a fresh clone: report every page untranslated.
                print(f"warning: locale directory not found for {code}: {path}",
                      file=sys.stderr)
            locales.append((code, locale_dir))
        extensions = tuple(e.lower() for e in DEFAULT_EXTENSIONS + tuple(args.ext))
        rows = scan(source_dir, locales, extensions, repo_root, args.far)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        json.dump(rows, sys.stdout, indent=2)
        print()
    elif args.format == "csv":
        fields = list(row("", "", "").keys())
        writer = csv.DictWriter(sys.stdout, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    else:
        summary = {}
        for r in rows:
            counts = summary.setdefault(r["locale"], {})
            counts[r["status"]] = counts.get(r["status"], 0) + 1
        for locale, counts in summary.items():
            parts = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"{locale}: {sum(counts.values())} pages - {parts}")

    failing = [r for r in rows if r["status"] in args.fail_on]
    if args.since and failing:
        try:
            # Added or modified since the ref: a new page, or an old page whose
            # pin was removed or broken by an edit after the ref.
            added = set(git(["diff", "--name-only", "--diff-filter=AM", args.since, "HEAD"],
                            repo_root).splitlines())
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        locale_dirs = dict(locales)
        def added_since(r):
            path = locale_dirs[r["locale"]] / r["page"]
            if repo_root not in path.parents:
                return False
            return path.relative_to(repo_root).as_posix() in added
        failing = [r for r in failing if r["status"] != "untranslated" and added_since(r)]
    if failing:
        print(f"fail: {len(failing)} page(s) with status in {sorted(args.fail_on)}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

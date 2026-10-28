"""Fingerprint-bound human sign-off records.

Some questions cannot be answered by a script:

* "is the privacy policy lawful and complete?"      (Gate Q)
* "are these business rules the intended ones?"      (Gate N)
* "does this design look good?"                      (Gate C)

A sign-off record answers exactly one of those questions, from a named
human, on a date, and it is **bound to the content it approved**: the
record carries a fingerprint of the files it reviewed.  Edit the rules or
the policy and the fingerprint no longer matches, so the approval is
invalid until somebody signs again.  That is what stops "signed off last
month" from silently blessing a different artefact.

Record shape (JSON)::

    {
      "reviewer": "Jane Doe",
      "date": "2026-01-31",
      "verdict": "approved",
      "notes": "rules match the product spec v3",
      "scope": "checkout flow",
      "fingerprint": "9f2c...32 hex chars",
      "subject": ["qa/scenarios.json", "docs/rules.md"],
      "tool": "app-production-readiness/signoff"
    }

CLI usage is provided by the gate scripts that own a question
(``--record-signoff --reviewer ... --verdict ...``); this module is the
shared plumbing they use.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime
from pathlib import Path

__all__ = [
    "SIGNOFF_DIR",
    "signoff_path",
    "fingerprint",
    "read_signoff",
    "validate_signoff",
    "build_signoff",
    "write_signoff",
    "signoff_args",
    "resolve_signoff",
]

SIGNOFF_DIR = ("qa", "signoff")
TOOL = "app-production-readiness/signoff"
VALID_VERDICTS = ("approved", "rejected")


# --------------------------------------------------------------------------
# paths
# --------------------------------------------------------------------------
def signoff_path(root: Path, name: str, override: str | None = None) -> Path:
    """Return the path of the sign-off record for ``name`` under ``root``.

    ``name`` is a file name such as ``business-rules.json``.  ``override``
    (a path supplied on the command line) wins when it is set.
    """
    if override:
        p = Path(override)
        return p if p.is_absolute() else (Path(root) / p)
    return Path(root).joinpath(*SIGNOFF_DIR) / name


# --------------------------------------------------------------------------
# fingerprint
# --------------------------------------------------------------------------
def fingerprint(paths, extra: str | None = None, root: Path | None = None) -> str:
    """Fingerprint a set of files (plus an optional extra marker string).

    The fingerprint is a sha256 over ``relpath:contenthash`` pairs sorted by
    path, so it is stable across machines and independent of mtimes.  A
    missing file still contributes a marker, so deleting a rules file also
    invalidates an approval.
    """
    items = []
    for p in sorted({Path(x) for x in (paths or [])}, key=lambda q: q.as_posix()):
        try:
            data = p.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
        except OSError:
            digest = "missing"
        try:
            rel = p.relative_to(root).as_posix() if root else p.name
        except ValueError:
            rel = p.as_posix()
        items.append(f"{rel}:{digest}")
    blob = "|".join(items)
    if extra:
        blob += f"|extra:{extra}"
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:32]


# --------------------------------------------------------------------------
# read / validate
# --------------------------------------------------------------------------
def read_signoff(path: Path) -> dict | None:
    """Read a sign-off record, or None when it is missing/unreadable."""
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError:
        return None
    try:
        data = json.loads(raw)
    except (ValueError, TypeError):
        return None
    return data if isinstance(data, dict) else None


def validate_signoff(signoff, expected_fingerprint: str, now: str | None = None) -> list[str]:
    """Return the reasons the sign-off is **not** valid (empty = valid).

    Checks: object shape, named reviewer, verdict, date sanity, and that the
    fingerprint still matches the content it approved.
    """
    reasons: list[str] = []
    if not isinstance(signoff, dict):
        return ["sign-off record is missing or is not a JSON object"]
    reviewer = (signoff.get("reviewer") or "").strip()
    if not reviewer:
        reasons.append("sign-off has no named reviewer")
    verdict = (signoff.get("verdict") or "").strip().lower()
    if verdict not in VALID_VERDICTS:
        reasons.append(f"sign-off verdict {verdict!r} is not one of "
                       f"{', '.join(VALID_VERDICTS)}")
    raw_date = (signoff.get("date") or "").strip()
    if not raw_date:
        reasons.append("sign-off has no date")
    else:
        try:
            parsed = datetime.strptime(raw_date, "%Y-%m-%d").date()
        except ValueError:
            reasons.append(f"sign-off date {raw_date!r} is not an ISO-8601 date")
        else:
            today = date.today() if now is None else datetime.strptime(now, "%Y-%m-%d").date()
            if parsed > today:
                reasons.append(f"sign-off date {raw_date!r} is in the future")
    got = (signoff.get("fingerprint") or "").strip()
    if not got:
        reasons.append("sign-off has no fingerprint")
    elif expected_fingerprint and got != expected_fingerprint:
        reasons.append("sign-off fingerprint does not match the current content "
                       "(the reviewed rules/policy changed after it was approved)")
    return reasons


# --------------------------------------------------------------------------
# build / write
# --------------------------------------------------------------------------
def build_signoff(reviewer: str, verdict: str, notes: str, expected_fingerprint: str,
                  scope: str | None = None, subject=None,
                  extra: dict | None = None) -> dict:
    """Build a sign-off record for the current content."""
    record = {
        "reviewer": (reviewer or "").strip(),
        "date": date.today().isoformat(),
        "verdict": (verdict or "").strip().lower() or "approved",
        "notes": (notes or "").strip(),
        "scope": (scope or "").strip(),
        "fingerprint": expected_fingerprint,
        "subject": sorted({Path(x).as_posix() for x in (subject or [])}) or None,
        "tool": TOOL,
    }
    if extra:
        record.update(extra)
    return record


def write_signoff(path: Path, payload: dict) -> bool:
    """Write a sign-off record (JSON, indented).  Returns True on success."""
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return True
    except OSError:
        return False


# --------------------------------------------------------------------------
# CLI plumbing
# --------------------------------------------------------------------------
def signoff_args(argv, prefix: str = "") -> dict:
    """Parse the shared sign-off CLI flags out of ``argv``.

    Supported flags::

        --signoff PATH        read/write the record at PATH
        --record-signoff      write a new record and exit the read path
        --reviewer NAME       who signs off
        --verdict V           approved | rejected
        --notes TEXT          free text
        --scope TEXT          what exactly was reviewed
        --<prefix>-ref TEXT   extra reference (e.g. --rules-ref)

    Unknown flags are ignored, so this composes with any other parser.
    """
    argv = list(argv or [])
    ref_flag = f"--{prefix}-ref" if prefix else "--ref"
    opts = {"path": None, "record": False, "reviewer": "", "verdict": "",
            "notes": "", "scope": "", "ref": ""}
    i = 0
    while i < len(argv):
        a = argv[i]
        nxt = argv[i + 1] if i + 1 < len(argv) else None

        def take(name):
            nonlocal i
            if nxt is not None:
                opts[name] = nxt
                i += 1

        if a == "--signoff" and nxt is not None:
            take("path")
        elif a == "--record-signoff":
            opts["record"] = True
        elif a == "--reviewer" and nxt is not None:
            take("reviewer")
        elif a == "--verdict" and nxt is not None:
            take("verdict")
        elif a == "--notes" and nxt is not None:
            take("notes")
        elif a == "--scope" and nxt is not None:
            take("scope")
        elif a == ref_flag and nxt is not None:
            take("ref")
        elif a.endswith(("-ref", "-basis")) and a.startswith("-") and nxt is not None:
            take("ref")
        i += 1
    return opts


def resolve_signoff(root: Path, name: str, opts: dict, expected_fingerprint: str,
                    subject=None, extra: dict | None = None) -> dict:
    """Read (or record) a sign-off and validate it.

    Returns a dict with the keys ``path``, ``record`` (the stored record or
    None), ``reasons`` (list; empty means valid) and ``fingerprint``.
    """
    path = signoff_path(root, name, opts.get("path"))
    record = None
    reasons: list[str] = []

    if opts.get("record"):
        built = build_signoff(opts.get("reviewer", ""), opts.get("verdict", "approved"),
                              opts.get("notes", ""), expected_fingerprint,
                              opts.get("scope"), subject, extra)
        if not write_signoff(path, built):
            reasons.append(f"could not write the sign-off record to {path}")

    record = read_signoff(path)
    if record is None:
        reasons.append(f"no sign-off record at {path}")
    else:
        reasons.extend(validate_signoff(record, expected_fingerprint))

    return {"path": str(path), "record": record, "reasons": reasons,
            "fingerprint": expected_fingerprint}

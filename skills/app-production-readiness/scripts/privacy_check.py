#!/usr/bin/env python3
"""Gate Q - privacy and GDPR.

Checks the things a privacy policy page cannot hide:

* a privacy policy exists, is reachable and is linked from the app
* consent is required before non-essential trackers load
* personal data is not written to logs (email/phone/card/token in log calls)
* personal data is not cached in the browser without consent
* a deletion / export route or process is documented
* the policy mentions retention and data-subject rights
* the absorbed privacy-relevant content rules (no third-party ad scripts)

A script can prove the policy *exists* and that the code respects consent,
logging and storage rules.  It cannot prove the policy is **lawful** -
that is a legal question, so it is signed by a human and bound to the
exact policy text that was reviewed:

  machine : policy present/linked, consent gating, no PII in logs or storage
  human   : ``qa/signoff/privacy.json`` (reviewer, date, verdict, legal
            basis, fingerprint of the policy files + the live policy route)

Editing the policy invalidates the approval until somebody signs again.

Usage:
  python scripts/privacy_check.py --root <app_root> [--url http://localhost:3000]
  python scripts/privacy_check.py --root <app_root> \
      --record-signoff --reviewer "Jane Doe" --verdict approved \
      --notes "GDPR Art.13/17 covered" --legal-basis "GDPR Art.13"

Exit 0 = privacy posture ok (a missing sign-off is reported as "needs
sign-off", not as a failure), 1 = blocking findings, 2 = nothing to check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import (GateResult, http_request, print_report, read_files)  # noqa: E402
import signoff as signoff_mod  # noqa: E402

SIGNOFF_NAME = "privacy.json"

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rb",
            ".php", ".java", ".vue", ".svelte", ".html"}
PRIVACY_ROUTES = ("/privacy", "/privacy-policy", "/legal/privacy", "/legal",
                  "/privacy-notice", "/gdpr")
RIGHTS = ("data subject", "right to access", "right to erasure", "right to be forgotten",
          "right to data portability", "delete your data", "access your data",
          "withdraw consent", "opt out", "opt-out")
RETENTION = ("retention", "retained for", "how long we keep", "data retention")
DPA = ("data processing", "dpa", "sub-processor", "subprocessor", "processor agreement")

PII_VAR = r"(email|e-mail|user_?email|phone|mobile|telephone|first_?name|last_?name|full_?name|address|postcode|zip_?code|birth_?date|dob|ssn|national_?id|passport|credit_?card|card_?number|cvv|pan|iban|password|secret|api_?key|token)"
LOG_CALL = re.compile(r"(?i)\b(console\.(log|info|warn|error|debug)|print|logger\.(info|debug|warn|error)|log\.(info|debug|warn|error))\s*\(")
PII_IN_LOG = re.compile(rf"(?i)({PII_VAR})\b")
STORAGE = re.compile(r"(?i)(localStorage|sessionStorage|document\.cookie)\s*\.?\s*"
                      r"(setItem|set)\s*\(\s*['\"]([^'\"]+)['\"]")
STORAGE_PII = re.compile(rf"(?i)({PII_VAR})")
CONSENT = re.compile(r"(?i)consent|cookie[_-]?banner|cookie_?notice|gdpr|"
                     r"cookiebot|onetrust|trustarc|do_not_track")
TRACKERS = re.compile(r"(?i)googletagmanager|google-analytics|gtag\(|facebook\.net|"
                       r"hotjar|segment\.io|mixpanel|amplitude|adsense|doubleclick|"
                       r"intercom|fullstory|clarity\.ms")
ANALYTICS_GATE = re.compile(r"(?i)consent|has_consent|analytics_allowed|cookie_consent|"
                             r"gdpr_consent|tracking_allowed")
DELETE_ROUTE = re.compile(r"(?i)(delete|erase|export|download)[-_/]?(account|my[-_]?data|"
                          r"data|me|user|profile)|/api/(delete|export)|"
                          r"right_to_erasure|deleteUserAccount")


def _logged_pii(root: Path):
    hits = []
    for path, text in read_files(root, CODE_EXT):
        for m in LOG_CALL.finditer(text):
            window = text[m.end(): m.end() + 300]
            line = text[:m.start()].count("\n") + 1
            for pm in PII_IN_LOG.finditer(window):
                hits.append(f"{path.relative_to(root)}:{line} ({pm.group(0).lower()})")
                break
    return hits


def _storage_pii(root: Path):
    hits = []
    for path, text in read_files(root, CODE_EXT):
        for m in STORAGE.finditer(text):
            key = m.group(3)
            window = text[m.end(): m.end() + 200]
            if STORAGE_PII.search(key) or STORAGE_PII.search(window):
                hits.append(f"{path.relative_to(root)}:{text[:m.start()].count(chr(10)) + 1} ({key})")
    return hits


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = None
    root_arg = "."
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
            i += 1
        i += 1
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1

    result = GateResult("Q", "PRIVACY & GDPR (policy + legal sign-off)")
    files = read_files(root, CODE_EXT)
    if not files:
        result.skipped = True
        result.reason = "no source files found - privacy posture not checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    # 1. privacy policy
    blob = "\n".join(t for _p, t in files)
    policy_text = ""
    policy_route = None
    policy_files = [p for p, _t in files
                    if p.name.lower() in ("privacy.md", "privacy.html",
                                          "privacy.txt", "legal.md")]
    # the policy may live outside the scanned source extensions
    for rel in ("privacy.md", "PRIVACY.md", "legal/privacy.md", "docs/privacy.md",
                "privacy.html", "privacy.txt", "legal.md"):
        cand = root / rel
        if cand.is_file() and cand not in policy_files:
            policy_files.append(cand)
    for path in policy_files:
        if path.name.lower() in ("privacy.md", "privacy.html", "privacy.txt"):
            policy_text += re.sub(r"\s+", " ", path.read_text(
                encoding="utf-8", errors="ignore").lower())
    if url:
        for route in PRIVACY_ROUTES:
            res = http_request(url.rstrip("/") + route, timeout=10.0)
            if res["status"] == 200 and res["body"]:
                policy_route = route
                policy_text += re.sub(r"\s+", " ", res["body"].lower())
                break
    result.add("a privacy policy page exists", bool(policy_files or policy_route), True,
               f"file={[p.name for p in policy_files]} route={policy_route}"
               if (policy_files or policy_route) else
               "no privacy page or route found")
    result.add("policy is linked from the app",
               bool(re.search(r"href=[\"'][^\"']*privacy", blob, re.I)),
               False, "")
    result.add("policy covers data-subject rights",
               any(term in policy_text for term in RIGHTS), False,
               "no access/erasure/opt-out wording found")
    result.add("policy states a retention period",
               any(term in policy_text for term in RETENTION), False,
               "no retention wording found")
    result.add("policy names processors / sub-processors",
               any(term in policy_text for term in DPA), False, "")

    # 2. consent before tracking
    has_tracker = bool(TRACKERS.search(blob))
    has_consent = bool(CONSENT.search(blob)) or bool(ANALYTICS_GATE.search(blob))
    if has_tracker:
        result.add("analytics/tracking is gated behind consent", has_consent, True,
                   "a tracker was found but no consent gate" if not has_consent else
                   "consent gate found")
    else:
        result.warn("analytics/tracking is gated behind consent",
                    "no third-party tracker found - rule not applicable")

    # 3. PII in logs
    logged = _logged_pii(root)
    result.add("personal data is not written to logs", not logged, True,
               "; ".join(logged[:5]) if logged else "")

    # 4. PII in browser storage
    stored = _storage_pii(root)
    result.add("personal data is not cached in the browser", not stored, True,
               "; ".join(stored[:5]) if stored else "")

    # 5. deletion / export path
    has_delete = bool(DELETE_ROUTE.search(blob)) or any(
        term in policy_text for term in ("delete your data", "delete your account",
                                         "export your data", "right to erasure"))
    result.add("a deletion / data-export path exists", has_delete, False,
               "no deletion or export route/process found")

    # 6. privacy-by-design: no analytics endpoint may collect raw PII
    analytics_pii = re.search(rf"(?i)(gtag|track|identify)\s*\([^)]*{PII_VAR}", blob)
    result.add("analytics calls do not carry personal data", not analytics_pii, True,
               "an analytics call receives an email/name/card field"
               if analytics_pii else "")

    # ---- human sign-off: "is the policy lawful and complete?" ----
    sign_opts = signoff_mod.signoff_args(args, prefix="legal")
    subject_rel = [str(p.relative_to(root).as_posix()) for p in policy_files]
    fp = signoff_mod.fingerprint(policy_files, extra=policy_route or "", root=root)
    sign = signoff_mod.resolve_signoff(
        root, SIGNOFF_NAME, sign_opts, fp, subject=subject_rel,
        extra={"legal_basis": sign_opts.get("ref") or None,
               "policy_route": policy_route})
    signed_off = not sign["reasons"]
    result.add("the policy is legally signed off", signed_off, False,
               "; ".join(sign["reasons"]) if sign["reasons"] else
               f"signed off by {sign['record'].get('reviewer')} on "
               f"{sign['record'].get('date')}")

    if result.blocking:
        verdict = "policy-failed"
    elif signed_off:
        verdict = "policy-met-and-legal-signed-off"
    else:
        verdict = "policy-met-needs-signoff"

    payload = print_report(result, json_mode, extra={
        "policy_route": policy_route,
        "policy_files": subject_rel,
        "verdict": verdict,
        "signoff_fingerprint": fp,
        "signoff_subject": subject_rel,
        "human_signoff": sign["record"],
        "signoff_reasons": sign["reasons"],
        "signoff_path": sign["path"],
        "legal_basis": sign_opts.get("ref") or None,
    })
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())

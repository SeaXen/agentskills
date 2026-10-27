#!/usr/bin/env python3
"""Gate T - payment and email flows.

Two flows that are easy to fake in a demo and expensive to get wrong.

**Payments**
* card data must never be collected by your own code (no raw PAN fields, no
  card numbers in the DOM, a hosted provider element instead)
* webhooks must verify their signature - an unverified webhook is a free
  "mark my order as paid" endpoint
* money must be handled in integer minor units and with an explicit currency
* idempotency keys must be used on create calls
* payment secrets must come from the environment, never from the source

**Email**
* a transactional provider must be configured (Resend/SendGrid/Postmark/
  SES/Nodemailer/SMTP)
* send failures must be handled, not swallowed
* marketing mail needs an unsubscribe / List-Unsubscribe header
* user input must not be concatenated into a mail body (header injection)
* no hardcoded API keys

Usage:
  python scripts/payment_email_check.py --root <app_root> [--json]

Exit 0 = flows are safe, 1 = blocking findings, 2 = nothing to check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files  # noqa: E402

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rb",
            ".php", ".java", ".kt", ".vue", ".svelte"}
MAIL_EXT = {".html", ".txt", ".mjml", ".hbs", ".ejs", ".pug"}

CARD_PROVIDERS = ("stripe", "paypal", "adyen", "braintree", "square", "razorpay",
                   "paddle", "lemonsqueezy", "checkout.com", "klarna", "wepay")
MAIL_PROVIDERS = ("resend", "sendgrid", "postmark", "nodemailer", "ses", "smtp",
                  "mailgun", "sendmail", "mailersend", "brevo", "postal")
CARD_PROVIDER_RE = re.compile(r"\b(" + "|".join(re.escape(p) for p in CARD_PROVIDERS) + r")\b", re.I)
MAIL_PROVIDER_RE = re.compile(r"\b(" + "|".join(re.escape(p) for p in MAIL_PROVIDERS) + r")\b", re.I)

CARD_FIELD = re.compile(r"(?i)<input[^>]*(name|id)\s*=\s*['\"][^'\"]*"
                        r"(card_?number|cardnumber|cc_?number|ccnumber|cvv|cvc|"
                        r"security_?code)[^'\"]*['\"]")
PAN_LITERAL = re.compile(r"(?i)(card_?number|pan|cc_?num)\s*[:=]\s*['\"]\d{12,}")
WEBHOOK = re.compile(r"(?i)webhook")
SIGNATURE_VERIFY = re.compile(
    r"(?i)constructEvent|verify_header|verifySignature|signatures\[|"
    r"stripe\.webhooks|verify\s*\(\s*payload|hmac|signature")
IDEMPOTENCY = re.compile(r"(?i)idempotency_?key|Idempotency-Key|idempotencyKey")
MINOR_UNITS = re.compile(r"(?i)(amount|price|total)\s*[:=]\s*(\d+)\s*\*\s*100|"
                         r"Math\.round\([^)]*\*\s*100|minor_?units|in_?cents")
CURRENCY = re.compile(r"(?i)\bcurrency\b")
HARD_KEY = re.compile(r"(?i)(sk_(live|test)_[A-Za-z0-9]{10,}|pk_live_[A-Za-z0-9]{10,}|"
                      r"SG\.[A-Za-z0-9]{10,}|AC[A-Fa-f0-9]{32})")
MAIL_SEND = re.compile(r"(?i)\.send(Mail|Message)?\s*\(|send_email|sendMail\s*\(")
MAIL_ERROR = re.compile(r"(?i)catch|except|try\s*\{|rescue|on\(['\"]error")
UNSUBSCRIBE = re.compile(r"(?i)unsubscribe|List-Unsubscribe|opt_?out|退订")
HEADER_INJECTION = re.compile(r"(?i)(subject|html|text)\s*[:=]\s*[`\"']?\s*\+?\s*"
                               r"(email|name|user\.|body\.|message\.)")
EMAIL_TEMPLATE = re.compile(r"(?i)(<html|<body|plain[-_ ]?text|text/html|"
                             r"template|mjml)", re.M)


def _files(root):
    return read_files(root, CODE_EXT)


def analyse_payments(root, blob, files, markup=()):
    findings = []
    has_provider = bool(CARD_PROVIDER_RE.search(blob))
    card_fields = [str(p.relative_to(root)) for p, t in files if CARD_FIELD.search(t)]
    card_fields += [str(p.relative_to(root)) for p, t in markup if CARD_FIELD.search(t)]
    if card_fields:
        findings.append(("HIGH", "card data is collected by your own form",
                        f"raw card inputs in {card_fields[:3]}"))
    pan = []
    for p, t in files:
        for m in PAN_LITERAL.finditer(t):
            pan.append(f"{p.relative_to(root)}:{t[:m.start()].count(chr(10)) + 1}")
    if pan:
        findings.append(("HIGH", "a card number literal is present in the source",
                         ", ".join(pan[:3])))
    if has_provider:
        if WEBHOOK.search(blob):
            if not SIGNATURE_VERIFY.search(blob):
                findings.append(("HIGH", "webhook handler does not verify its signature",
                                 "an unverified webhook lets anyone mark an order paid"))
        else:
            findings.append(("LOW", "no webhook handler found",
                             "if you take payments, a verified webhook is required"))
        if not CURRENCY.search(blob):
            findings.append(("MEDIUM", "no explicit currency on the payment",
                             "amounts without a currency are ambiguous"))
        if not MINOR_UNITS.search(blob):
            findings.append(("LOW", "amounts are not handled in minor units",
                             "use integer cents to avoid float rounding"))
        if not IDEMPOTENCY.search(blob):
            findings.append(("MEDIUM", "no idempotency key on the payment call",
                             "a retried charge can double-bill a customer"))
    else:
        findings.append(("INFO", "no payment provider detected",
                         "payment checks did not apply"))
    for p, t in files:
        for m in HARD_KEY.finditer(t):
            findings.append(("HIGH", "hardcoded payment/email credential",
                             f"{p.relative_to(root)}"))
            break
    return findings


def analyse_email(root, blob, files):
    findings = []
    has_provider = bool(MAIL_PROVIDER_RE.search(blob))
    if not has_provider:
        findings.append(("INFO", "no transactional email provider detected",
                         "email checks did not apply"))
        return findings
    sends = [p for p, t in files if MAIL_SEND.search(t)]
    if not sends:
        findings.append(("MEDIUM", "email provider imported but never used",
                         "no send call found"))
    for p, t in files:
        for m in MAIL_SEND.finditer(t):
            window = t[m.end(): m.end() + 400]
            if not MAIL_ERROR.search(window):
                findings.append(("MEDIUM", "email send without error handling",
                                 f"{p.relative_to(root)}:{t[:m.start()].count(chr(10)) + 1}"))
                break
    if HEADER_INJECTION.search(blob):
        findings.append(("MEDIUM", "user input concatenated into a mail header/body",
                         "header injection / content spoofing risk"))
    marketing = re.search(r"(?i)newsletter|marketing|campaign|unsubscribe", blob)
    if marketing and not UNSUBSCRIBE.search(blob):
        findings.append(("HIGH", "marketing mail without an unsubscribe option",
                         "required by CAN-SPAM / GDPR"))
    templates = [p for p, t in read_files(root, MAIL_EXT)]
    if not templates:
        findings.append(("LOW", "no mail templates found",
                         "templates keep content out of the code"))
    for p, t in files:
        for m in HARD_KEY.finditer(t):
            findings.append(("HIGH", "hardcoded email provider key",
                             f"{p.relative_to(root)}"))
            break
    return findings


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    root_arg = "."
    i = 0
    while i < len(args):
        if args[i] == "--root" and i + 1 < len(args):
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

    result = GateResult("T", "PAYMENT & EMAIL FLOWS")
    files = _files(root)
    markup = read_files(root, {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"})
    if not files and not markup:
        result.skipped = True
        result.reason = "no source files found - payment/email flows not checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2
    blob = "\n".join(t for _p, t in files)

    payments = analyse_payments(root, blob, files, markup)
    emails = analyse_email(root, blob, files)
    for severity, check, detail in payments + emails:
        if severity in ("HIGH", "CRITICAL"):
            result.fail(check, detail, severity)
        elif severity == "MEDIUM":
            result.fail(check, detail, "MEDIUM")
        else:
            result.warn(check, detail)

    payload = print_report(result, json_mode, extra={
        "payment_findings": [{"severity": s, "check": c, "detail": d}
                             for s, c, d in payments],
        "email_findings": [{"severity": s, "check": c, "detail": d}
                           for s, c, d in emails],
    })
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())

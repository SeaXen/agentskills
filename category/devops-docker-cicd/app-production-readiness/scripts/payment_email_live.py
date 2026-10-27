#!/usr/bin/env python3
"""Deep mode for Gate T: a real payment round-trip and a real email round-trip.

``payment_email_check.py`` reads the code and guesses.  This script talks to
the providers, but only ever in *test* mode:

* **Stripe** - creates a PaymentIntent through the Stripe API with a
  ``sk_test_`` key.  A live key (``sk_live_``/``rk_live_``) is refused: the
  script must never move real money.
* **Email** - sends one message through the Resend API to the address in
  ``QA_TEST_EMAIL`` (or ``RESEND_TEST_TO``).  Without a test recipient
  address the email channel is skipped, never faked.

Exit codes follow the skill-wide contract:

* ``0`` - every attempted channel succeeded
* ``1`` - a channel that was attempted failed
* ``2`` - no channel could be attempted (no test credentials).  A skip is
  never reported as a pass.

Artefact: ``qa/payment-email-live.json``.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, http_request, print_report  # noqa: E402

STRIPE_URL = "https://api.stripe.com/v1/payment_intents"
RESEND_URL = "https://api.resend.com/emails"
LIVE_PREFIXES = ("sk_live_", "rk_live_", "sk_live", "rk_live")


# --------------------------------------------------------------------------
# providers
# --------------------------------------------------------------------------

def stripe_intent(api_key: str, amount: int = 100, currency: str = "usd") -> dict:
    """Create a PaymentIntent in test mode."""
    body = urllib.parse.urlencode({
        "amount": str(amount),
        "currency": currency,
        "payment_method_types[]": "card",
        "description": "app-production-readiness smoke test",
    }).encode("utf-8")
    res = http_request(
        STRIPE_URL, method="POST", body=body, timeout=30,
        headers={"Authorization": f"Bearer {api_key}",
                 "Content-Type": "application/x-www-form-urlencoded"})
    data = res.get("json") or {}
    return {
        "channel": "stripe",
        "ok": bool(res.get("ok")) and res.get("status") in (200, 201),
        "status": res.get("status"),
        "id": data.get("id", ""),
        "amount": data.get("amount"),
        "currency": data.get("currency"),
        "status_field": data.get("status", ""),
        "error": res.get("error", "") or (data.get("error") or {}).get("message", "")
        if isinstance(data.get("error"), dict) else res.get("error", ""),
        "body_head": (res.get("body") or "")[:300],
    }


def resend_email(api_key: str, to: str, sender: str, subject: str = "app-production-readiness test") -> dict:
    """Send one real email through Resend."""
    payload = {
        "from": sender,
        "to": [to],
        "subject": subject,
        "text": "This is an automated production-readiness smoke test email. "
                "No action is required.",
    }
    res = http_request(
        RESEND_URL, method="POST",
        body=json.dumps(payload).encode("utf-8"), timeout=30,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    data = res.get("json") or {}
    return {
        "channel": "email",
        "ok": bool(res.get("ok")) and res.get("status") == 200,
        "status": res.get("status"),
        "id": data.get("id", ""),
        "to": to,
        "error": res.get("error", ""),
        "body_head": (res.get("body") or "")[:300],
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root_str, want_json, _ = parse_cli(argv)
    root = resolve_root(root_str)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}")
        return 1

    amount = 100
    currency = "usd"
    to_addr = os.environ.get("QA_TEST_EMAIL") or os.environ.get("RESEND_TEST_TO")
    sender = os.environ.get("QA_MAIL_FROM") or os.environ.get("RESEND_FROM")
    stripe_key = os.environ.get("STRIPE_SECRET_KEY") or os.environ.get("STRIPE_TEST_KEY")
    email_key = os.environ.get("RESEND_API_KEY") or os.environ.get("MAIL_API_KEY")

    i = 0
    while i < len(argv):
        if argv[i] == "--amount" and i + 1 < len(argv):
            try:
                amount = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif argv[i] == "--to" and i + 1 < len(argv):
            to_addr = argv[i + 1]
            i += 1
        elif argv[i] == "--from" and i + 1 < len(argv):
            sender = argv[i + 1]
            i += 1
        i += 1

    result = GateResult("T", "PAYMENT + EMAIL LIVE ROUND-TRIP")
    channels = []
    notes = []
    live_refused = False

    if stripe_key and stripe_key.startswith(LIVE_PREFIXES):
        live_refused = True
        result.add("the Stripe key is a test key", False,
                   detail="refusing to touch a live Stripe key")
        notes.append("STRIPE_SECRET_KEY looks like a live key - the payment "
                     "channel was refused on purpose")
    elif stripe_key:
        channels.append(stripe_intent(stripe_key, amount, currency))
    else:
        notes.append("STRIPE_SECRET_KEY is not set - the payment channel was not exercised")

    if email_key and to_addr:
        channels.append(resend_email(email_key, to_addr, sender or "onboarding@resend.dev"))
    elif email_key:
        notes.append("QA_TEST_EMAIL is not set - the email channel was not exercised "
                     "(a real recipient address is required)")
    else:
        notes.append("RESEND_API_KEY is not set - the email channel was not exercised")

    if not channels:
        for note in notes:
            result.notes.append(note)
        if live_refused:
            # A refused live key is a blocking problem, not a skip.
            payload = print_report(result, want_json, extra={"channels": []})
            _write(root, payload, want_json)
            emit([], payload, want_json)
            return 1
        result.skipped = True
        result.reason = "no test credentials were available - nothing was sent"
        payload = print_report(result, want_json, extra={"channels": []})
        _write(root, payload, want_json)
        emit([], payload, want_json)
        return 2

    for chan in channels:
        if chan["channel"] == "stripe":
            result.add("a test PaymentIntent is created and confirmed by Stripe",
                       chan["ok"],
                       detail=(f"pi id={chan.get('id')} status={chan.get('status_field')}"
                               if chan["ok"] else f"HTTP {chan.get('status')} {chan.get('error')}"))
        else:
            result.add("a test email is accepted by the provider",
                       chan["ok"],
                       detail=(f"message id={chan.get('id')} to={chan.get('to')}"
                               if chan["ok"] else f"HTTP {chan.get('status')} {chan.get('error')}"))
    for note in notes:
        result.notes.append(note)

    payload = print_report(result, want_json, extra={"channels": channels})
    _write(root, payload, want_json)
    emit([], payload, want_json)
    return 1 if result.blocking else 0


def _write(root: Path, payload, want_json) -> None:
    try:
        out_dir = root / "qa"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "payment-email-live.json").write_text(
            json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    raise SystemExit(main())

**No, don't resend the whole issue.** Send a short correction email now, and fix the author credit in the web archive only.

## Why a full resend is the wrong call

The issue's corrections rules rank errors by the harm to readers, not by how embarrassing they are. Your two mistakes fall in different tiers:

| Error | Tier | Action |
|---|---|---|
| Wrong author credit (Ines Okonjo instead of Tomasz Vey) | Wrong author credit | Fix the web archive. No resend. |
| `pip install kestrel-cli==3.1.0` in the "upgrade now" tip | Advice that weakens security (a vulnerable version recommended) | Send a short correction email now, with the right version in its first sentence. Fix the archive. |

A resend with an apology on top fails on three counts:
- **It buries the fix.** The security point sits under an apology and a full issue the readers have already seen. Many will skim and delete it.
- **It reads as spam.** 9,400 people get a duplicate.
- **The vulnerable command still reaches inboxes first.** It matters most to the readers who already ran it. They need to hear "check your version and upgrade" in the first line, not find it in a re-sent issue.

The correction costs one extra email, which is justified because readers who follow the original advice are exposed. The author mix-up doesn't justify an email on its own.

## What to do, in order

1. **Fix the web archive.** Change the command to 3.1.2 and the credit to Tomasz Vey. Do this before sending, so any link in the correction lands on the right text.
2. **Fix any other copy of the issue.** That means RSS, social posts and a cross-posted blog, if you have them.
3. **Send the correction below** to all 9,400 subscribers, today.
4. **Message Ines and Tomasz directly.** Tomasz was uncredited and Ines was credited for work she didn't write. This is outside the newsletter, but it's the quick fix for the credit error.

## The correction email

**Subject** (44 characters): `Correction: use kestrel-cli 3.1.2, not 3.1.0`

**Preview text** (95 characters): `Upgrade to 3.1.2: yesterday's tip pinned 3.1.0, which has a path traversal bug. Details inside.`

**Body**

> Upgrade to Kestrel CLI 3.1.2: yesterday's "upgrade now" tip told you to install 3.1.0, and that version has a path traversal vulnerability.
>
> To fix it, run:
>
> ```
> pip install -U "kestrel-cli>=3.1.2"
> ```
>
> To see what you have installed, run `pip show kestrel-cli`. If the version reads 3.1.0 [AFFECTED RANGE: confirm whether 3.1.1 is also affected], upgrade as above.
>
> The bug is tracked as [CVE-XXXX-XXXXX: path traversal in Kestrel CLI 3.1.0](ADVISORY-URL) and is fixed in 3.1.2. The web archive now shows the correct command.
>
> Sorry for the error. It was ours.
>
> *(Optional, one line:)* We also credited the caching deep-dive to the wrong author. Tomasz Vey wrote it. The archive is fixed.
>
> Found another error? Reply to this email.
>
> [Archive] · [Unsubscribe] · [sender address]

The command lines stay under 40 characters, and the code is a single live-text line. If your tool takes raw HTML, use the inline-styled `<pre>` pattern from the rendering reference.

I made the author line optional because the rules say a wrong credit alone gets an archive fix, not a send. I'd lean toward leaving it out, so the email carries one message. If you keep it, put it last, as above.

**Plain-text part**

```
CORRECTION: use kestrel-cli 3.1.2, not 3.1.0

Upgrade to Kestrel CLI 3.1.2. Yesterday's
"upgrade now" tip told you to install
3.1.0, and that version has a path
traversal vulnerability.

To fix it, run:

    pip install -U "kestrel-cli>=3.1.2"

To see what you have installed, run:

    pip show kestrel-cli

If the version reads 3.1.0 [AFFECTED RANGE:
confirm], upgrade as above.

CVE-XXXX-XXXXX: path traversal in
Kestrel CLI 3.1.0
ADVISORY-URL (full URL)

The web archive now shows the correct
command. Sorry for the error. It was ours.

Found another error? Reply to this email.

Archive: ARCHIVE-URL (full URL)
Unsubscribe: UNSUBSCRIBE-URL (full URL)
```

## Pre-send report

| Check | Status |
|---|---|
| Right version in the first sentence | pass |
| One ask (upgrade) and one primary link (advisory) | pass |
| Subject 44 characters, names the fix; preview 95 characters with the news in the first 35 | pass |
| Tone-pass words ("just", "simply", "easy", hype) | pass |
| Code is live text, lines under 40 characters | pass |
| Advisory URL and CVE ID | **blocked**: I have neither. Don't send without a real advisory link. |
| Affected range | **blocked**: you told me 3.1.0 is affected and 3.1.2 is the fix. Say whether 3.1.1 is affected before you write "3.1.0 only". |
| 3.1.2 as the target | **blocked**: confirm it's still the right version to name and that no newer release changes the advice. The `>=` pin tolerates a newer one. |
| Statements about the bug | pass: I wrote only "path traversal, fixed in 3.1.2". Add nothing about exploitability or impact unless the advisory states it. |
| Test send in light and dark mode (Gmail, Apple Mail on a phone, classic Outlook) | **blocked**: only you can send it. |
| Links resolve through the click-tracking domain | **blocked**: check this in the test send. |
| Archive page fixed and matches the send | **blocked**: do this first. |

Two decisions are outside the newsletter. Check with your security owner whether 3.1.0 should be yanked from PyPI, and whether the advisory text needs to go out on other channels.

I'd also tell your manager that the fix for the 3.1.0 advice is a separate message from the credit fix, and that the first goes out today.
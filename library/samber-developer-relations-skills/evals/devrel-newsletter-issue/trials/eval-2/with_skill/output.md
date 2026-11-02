I haven't written the verification code, because this skill bars me from writing security-sensitive code. I also don't have Harrowgate's real signing scheme, so anything I wrote would be a guess. The tip is drafted below with a slot for your code.

## Why I'm not writing the code

- **Signature checks are a stated exception.** The newsletter skill says to use your tested code verbatim, or link to the docs page that holds it. A wrong excerpt in a security tip lands in the worst row of the corrections table. That row means an immediate correction email to every reader, and readers copy this code into production.
- **I'd be guessing at the scheme.** I don't know your header names, your signed-string format (`timestamp.body` or something else), the hash, the tolerance window, or the encoding. A generic HMAC example that differs from Harrowgate's would fail for anyone who pasted it.

Please paste one of these:
1. The tested Python from your docs, SDK or internal tests. This is the best option.
2. The docs page that already holds it. I'll write the tip around a link.

## Draft tip, ready for the code

**Tip of the month: verify webhook signatures before you trust a payload**

Every Harrowgate webhook is signed so you can confirm it came from us and wasn't replayed. [One sentence stating what Harrowgate actually signs and in which header. I need this from your docs.] Reject any request that fails the signature check or arrives outside the timestamp tolerance, and compare signatures in constant time.

[Excerpt: up to 5 lines of the verification, as live text. Pasted from your code.]

[Full verification, about 28 lines: link text "full Python example on GitHub" or "webhook signature docs", pointing to your hosted file.]

*If you quote a tolerance window such as "5 minutes", the number must come from your docs.*

## Your Carbon image

I'd advise against it, for these reasons:
- **Images are blocked by default** in some clients, so some readers see an empty box where the code should be.
- **Readers can't copy it.** For a tip people will paste into production, that defeats the purpose.
- **Screen readers can't read it.**
- **It shrinks on phones.** About 28 lines at Carbon's default width scales down to unreadable in a template column around 600px wide.
- **The Dracula background** is dark, so dark-mode inversion can change its contrast.

My recommendation is the 5-line live-text excerpt plus a link to the full file. That costs about the same effort and works everywhere.

If you keep the image, ship it with these safeguards:
- **Alt text** that describes what the code does, not "code screenshot". For example: *"Python function that rebuilds the signed string from the timestamp and raw body, compares it to the signature header in constant time, and rejects requests outside the tolerance window."* Adjust it to match the final code.
- **A text link to the code** directly beneath it, as shown in the Mailchimp block below.
- **Image width of 600px or less**, with the Carbon export at 2x so it stays sharp.

## Mailchimp block (custom HTML)

Image version, with the text link underneath:

```html
<h2 style="margin:0 0 8px 0;font-size:20px;">Tip of the month: verify webhook signatures</h2>
<p style="margin:0 0 12px 0;font-size:16px;">[Intro sentence from your docs.]</p>
<img src="[CARBON_IMAGE_URL]" width="560" alt="[Alt text as above]" style="display:block;max-width:100%;height:auto;">
<p style="margin:8px 0 16px 0;font-size:16px;"><a href="[FULL_CODE_URL]" style="text-decoration:underline;">Copy the full Python example on GitHub</a></p>
```

If you take the live-text route instead, use this pattern for the 5-line excerpt:

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">
  <tr>
    <td style="padding:12px 14px;background-color:#f4f4f5;border:1px solid #d4d4d8;">
      <pre style="margin:0;color:#1f2328;font-family:Consolas,Menlo,Monaco,'Courier New',monospace;font-size:13px;line-height:1.45;white-space:pre-wrap;word-break:break-word;">[excerpt, lines of 40 characters or fewer]</pre>
    </td>
  </tr>
</table>
```

Python can't be re-wrapped safely, so keep the excerpt short rather than reflowing it.

## Plain-text part

```
TIP OF THE MONTH: VERIFY WEBHOOK SIGNATURES
[Intro sentence.]

Full Python example:
[FULL_CODE_URL]
```

If you use the image, the plain-text part has no code at all, so the link line is required.

## Pre-send report

| Check | Status |
|---|---|
| Verification code | **Blocked.** I need your tested code or docs link. |
| Intro claim (what is signed, which header) | **Blocked.** It must come from your docs. |
| Full file hosted (GitHub, gist or docs) | **Blocked.** Needed for the link. |
| Alt text on the image, plus a text link | Pass (template). |
| Test send in Gmail, Apple Mail on a phone, and classic Outlook, in light and dark mode | **Blocked.** The Dracula image is the thing to check in dark mode. |
| Code runnable or labelled as an excerpt | **Blocked** until the code arrives. |

## Open questions

1. Can you paste the tested code or the docs link?
2. Do you keep the image, or switch to the excerpt plus link?
3. Is this tip standalone, or one section of a larger issue? If it's part of an issue, the one-ask rule applies. Is "copy the code" the ask?
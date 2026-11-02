# Tip of the month: verify webhook signatures

## ⚠️ Check before you ship

I don't have Harrowgate's real signing spec, so this uses the common scheme: HMAC-SHA256 over `"{timestamp}.{raw_body}"`, hex-encoded, with the timestamp and signature sent in headers. Check these against your API docs and change them if they differ:

- The header names. I use `X-Harrowgate-Signature` and `X-Harrowgate-Timestamp` in the copy below.
- The signed string format.
- Hex versus base64 encoding.
- Whether the timestamp is in seconds or milliseconds.
- Whether the signature header carries a prefix such as `sha256=`.

## 1. Code for Carbon (29 lines)

Paste this into Carbon as is.

```python
import hashlib
import hmac
import time

TOLERANCE_SECONDS = 300  # 5 min: absorbs clock skew, limits the replay window


class InvalidSignature(Exception):
    pass


def verify_webhook(secret, raw_body, signature, timestamp):
    """Raise InvalidSignature unless the request is authentic and fresh."""
    try:
        sent_at = int(timestamp)
    except ValueError:
        raise InvalidSignature("malformed timestamp")

    # Freshness first: stops replays of a captured, validly signed request
    if abs(time.time() - sent_at) > TOLERANCE_SECONDS:
        raise InvalidSignature("timestamp outside tolerance")

    # Sign timestamp + body together so the timestamp can't be swapped
    signed_payload = f"{timestamp}.".encode() + raw_body
    expected = hmac.new(secret.encode(), signed_payload, hashlib.sha256).hexdigest()

    # Constant-time compare: == leaks timing information
    if not hmac.compare_digest(expected.encode(), signature.encode()):
        raise InvalidSignature("signature mismatch")
```

## 2. Carbon settings

- **Theme:** Dracula
- **Language:** Python
- **Window controls:** on, or off for a cleaner look
- **Drop shadow:** off. It adds dead pixels that shrink the code at email width.
- **Padding:** 24 to 32 px
- **Line numbers:** off
- **Font size:** 14 px, which stays readable once scaled to about 560 px wide
- **Width:** about 700 px, so no line wraps
- **Export:** PNG at 2x, for retina screens. Under about 200 KB is ideal.

## 3. Newsletter section

Copy and HTML for the Mailchimp custom template. Upload the PNG to Content Studio and replace `IMAGE_URL`.

```html
<!-- Tip of the month -->
<tr>
  <td style="padding:24px 20px 8px 20px;font-family:Helvetica,Arial,sans-serif;">
    <p style="margin:0 0 4px 0;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#6b7280;">Tip of the month</p>
    <h2 style="margin:0 0 12px 0;font-size:22px;line-height:28px;color:#111827;">Verify every webhook before you trust it</h2>
    <p style="margin:0 0 16px 0;font-size:16px;line-height:24px;color:#374151;">
      Anyone who finds your webhook URL can POST to it. Check the signature and the timestamp before you act on an event.
      Three details matter:
    </p>
    <ul style="margin:0 0 16px 20px;padding:0;font-size:16px;line-height:24px;color:#374151;">
      <li>Sign the <strong>raw request body</strong>. Re-serialized JSON won't match.</li>
      <li>Reject timestamps outside a <strong>5-minute window</strong> to block replays.</li>
      <li>Compare with <code>hmac.compare_digest</code>, never <code>==</code>.</li>
    </ul>
  </td>
</tr>
<tr>
  <td align="center" style="padding:0 20px 16px 20px;">
    <img src="IMAGE_URL" width="560" alt="Python function verify_webhook: parses the timestamp, rejects it if older than 300 seconds, computes HMAC-SHA256 over timestamp, a dot, and the raw body, then compares with hmac.compare_digest and raises InvalidSignature on mismatch."
         style="display:block;width:100%;max-width:560px;height:auto;border:0;border-radius:8px;">
  </td>
</tr>
<tr>
  <td style="padding:0 20px 24px 20px;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;color:#6b7280;">
    Pass the raw bytes (in Flask, <code>request.get_data()</code>) and the two headers to <code>verify_webhook</code>. Return a 400 on <code>InvalidSignature</code>.
    <a href="DOCS_URL" style="color:#6d28d9;">Full webhook docs</a>
  </td>
</tr>
```

## 4. Email notes

- **Alt text:** many clients block images by default, so the alt text carries the gist. The bullets above also work without the image.
- **Copying:** readers can't copy code from an image. Put the code in a gist or your docs and point `DOCS_URL` at it.
- **Dark mode:** Dracula's dark background looks fine in both modes. The `border-radius` keeps the edges soft on a white email.
- **Preview:** send a Mailchimp preview to Gmail and Outlook before the real send. Outlook ignores `border-radius` and `max-width` on images, which is why the explicit `width="560"` is there.
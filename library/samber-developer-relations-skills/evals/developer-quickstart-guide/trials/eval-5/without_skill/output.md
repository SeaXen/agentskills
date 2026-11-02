Here's the tidied version of those two steps:

## Installing the client

Install the Quillpost client library from npm:

```bash
npm install quillpost
```

## Configuring your credentials

Grab your API key from **Settings > API** and store it as an environment variable — don't hardcode it in your source:

```bash
export QUILLPOST_API_KEY="qp_live_xxxxxxxxxx"
```

Then create the client:

```javascript
const qp = new Quillpost(process.env.QUILLPOST_API_KEY);
```

---

What I fixed and why:

1. **`npm install` was missing the package name** — as written, it doesn't actually install anything. Added `quillpost` (swap for the real published package name if different).
2. **The credentials example hardcoded a live-looking key (`qp_live_9fT2xA`) directly in the snippet.** Docs that show a real key shape invite readers to copy-paste a real secret straight into committed source. Switched to an environment variable, which is also the safer pattern to teach by example.
3. Dropped the inline `1  2` line-number artifacts from the code block (they'd get copy-pasted verbatim if left in) and turned the "your key is in Settings > API" comment into prose above the snippet, so the code block itself is clean and runnable as-is.

Separately, not part of the two steps you flagged: the closing line under "Sending your first email" has a double period ("dashboard..") and dumps six links in one run-on sentence — worth breaking into a short bulleted "Next steps" list if you want that section tidied too, just say the word.
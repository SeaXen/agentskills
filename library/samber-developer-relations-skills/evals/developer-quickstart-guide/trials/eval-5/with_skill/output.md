Two steps tidied, ready to paste. Defects found first, then fix.

**Installing the client** — gerund heading, no package name, `$` prompt left in.
**Configuring your credentials** — gerund heading, line numbers in code block, comment inside block, key shown is live-mode (`qp_live_`) and looks like a real paste-able value, credential path not linked.

```markdown
## 1. Install the client library

    npm install @quillpost/client@2

## 2. Configure your API key

Create `send.js` and add your key (find it under **Settings → API**, or [create one directly](<QUILLPOST_KEYS_URL>)):

    const qp = new Quillpost("<YOUR_API_KEY>");

Quillpost doesn't validate the key until you call the API — a bad key surfaces as an auth error on send, not here.
```

Assumptions to swap before publishing:
1. `@quillpost/client@2` — placeholder package name + version. Use real npm name and current major.
2. `<QUILLPOST_KEYS_URL>` — placeholder link. Point at the actual key-creation page.
3. If Quillpost has a sandbox/test-mode key (like `qp_test_...`), use that here instead of a live key — removes the "pasted a real key into a doc" risk entirely. Flagging, not assuming it exists.

Not touched, since out of scope, but worth knowing: "Sending your first email" heading is also gerund form, and the closing line lists 6 next steps (template caps at 3) — happy to fix both if wanted.

Next: swap the two placeholders above, then cold-run steps 1–2 on a clean machine to confirm.
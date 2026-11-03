# Worked example — bd.airtel.com/en/sim-services

## Result
- Page HTML (264 KB) had **0** `$ACTION_ID_`, **0** `<form`, **0** `action=`, **0** bare 40-hex matches.
- RSC payload (`RSC: 1`, 163 KB) had no action-id bindings.
- Action manifest `/_next/static/app-build-manifest.js` → **404**.
- Downloaded **47** chunks from `/_next/static/chunks/*.js`.

## Key findings
1. **The sim-services page is STATIC.** Its "Buy now / Apply now" CTAs are `<a href>` image links — no Server Action is wired to this route. So there is NO action ID *for that page*.
2. The live site's global action IDs (from the shared bundle) are 14 IDs of **42 hex chars**. User-provided sample `60e0f63a693b083fb961b661e6fd775e6ca25dc4ba` matched entry #2 (`order`/`otp` flow) — proved we hit the right bundle.
3. **42-char trap:** a strict `[0-9a-f]{40}` regex returns NOTHING. Next.js 14+ ships 42-char IDs. Use `{40,44}`.
4. **`)` before `(` trap:** the call is `(0,s.createServerReference)("7f...",...)`. Regex must be `createServerReference\)\("..."`.
5. **False positives from bare hex:** grep `-oE '[0-9a-f]{40}'` on the bundle returns the RFC 3526 DH prime (`ffffffff...c90fdaa22168c234c4c6628b...`) and concatenated blobs. Always anchor on `createServerReference)("`.

## Labelled IDs (context keywords)
```
60e0f63a693b083fb961b661e6fd775e6ca25dc4ba   order, otp      <- user's sample
7f9a541f879002d7f1f5934c484146a5e602ed2e89   login, social
7fdfddeb496b92d341ebbe06d0afed8a94b8a57b71   socialLogin
7fb6c9e8cd0683cd308db241eee1fa4bb2318c1a28   otp, social
7f9a64fede8ab301c6ebf8383a832285819172fb9c   registration, order
7fd3193ebc6e9c15b3bd6ecf14083449490bc7687e   resendOtp, search
7ffd8661a467005c5ac19e7480f8382d7ffecdf1be   validateMsisdn
7f1e671af5a899764ff65fffaa6d70070caaea5626   getBalance
7f302f9ff293c65d2167054641e4f8999638e26bba   gSsearchConfigurations
7fda76af896daa297790895b0d641dacf7a9f3afe0  (unnamed) search
7f34ae9a665deb8849efe58a7901017f49f521af4b   order, search
7f1cd1d0715f05fd98dbe928bc7f5c88b79cf1bfe0   (unnamed)
7f9a7e1b88c9656559beef8d0f8d378e269249f6ab   (unnamed)
602e2226aefdeca19c1e1dddb77ad6d784baafc160   (unnamed)
```

## Lesson for future sessions
When asked for "the action ID on <URL>", first confirm the page actually wires a form/action. If it's static, report that clearly and, if useful, provide the site's global action IDs — but explicitly state none belong to that specific route. The user corrected this exact miss ("maybe search / scan number [that URL] help").

Do these 5 steps in order. About 1 to 2 hours for SSO, 1 to 2 hours for docs embed. I could not use web search here, so I wrote the setting names from memory. Check each against `meta.discourse.org` before you ship.

**Verdict on Discord: do not switch.** The reasons are at the end.

## Part 1: Log in with Tally account

Pick one method. Tally app is the identity provider. Discourse is the client.

**Option A: OIDC.** Use it if Tally already speaks OpenID Connect.
1. Open Admin, Settings, search `openid`. Enable the bundled `discourse-openid-connect` plugin.
2. Set the discovery URL, client ID, and client secret from your Tally IdP.
3. Register callback `https://forum.tallyhq.com/auth/oidc/callback` at the IdP.

**Option B: DiscourseConnect.** Use it if Tally has no OIDC. Tally backend signs requests.
1. In Admin, Settings, set `discourse_connect_url` to a Tally endpoint, for example `https://app.tallyhq.com/discourse/sso`.
2. Set `discourse_connect_secret` to a random 32+ character value. Store it in a secrets manager, not in the repo.
3. Set `enable_discourse_connect` to true last. Keep an admin session open in another browser. A wrong config can lock you out. Fallback: set `DISCOURSE_ENABLE_DISCOURSE_CONNECT=false` in `app.yml` and rebuild, or use the rails console.
4. Build the Tally endpoint:
   - Receive `sso` (base64 payload) and `sig`.
   - Compute HMAC-SHA256 of `sso` with the secret. Compare to `sig` in constant time.
   - Decode `sso`. Read `nonce` and `return_sso_url`.
   - Reject any `return_sso_url` outside `forum.tallyhq.com`.
   - Force Tally login if no session exists.
   - Build a new payload: `nonce`, `external_id`, `email`, `username`, `name`. Base64-encode it. Sign it. Redirect to `return_sso_url?sso=...&sig=...`.

Rules that prevent bugs:
- `external_id` = Tally's immutable user ID. Never use email. Emails change.
- Send `email` only when Tally has verified it. Discourse trusts it. An unverified email allows account takeover.
- Set `require_activation=true` if you cannot guarantee verified email.
- Set `logout_redirect` to the Tally logout URL so logout is not half done.
- Enable `discourse_connect_overrides_username`, `_email`, and `_name` so Tally stays the source of truth.
- Test with two accounts, one with an email change.
- Optional: sync Tally plan to a Discourse group with the `add_groups` parameter. This gives paid users a private category.

## Part 2: Related threads inside docs pages

Discourse "embedding" shows comments for one page. It does not show related threads. You want related threads, so use the API.

**Recommended: server-side or build-time fetch.** Works with any docs framework.
1. Tag threads by docs area, for example `billing`, `api-webhooks`. One tag per docs section.
2. Fetch on the docs server, or at build time with a short cache (5 to 15 minutes):
   - By tag: `GET https://forum.tallyhq.com/tag/billing/l/latest.json`
   - By text: `GET https://forum.tallyhq.com/search.json?q=webhook retry order:latest`
3. Render title, reply count, and link, 3 to 5 items. Add a "Ask in the forum" button that opens `/new-topic?category=...&tags=billing`.
4. Fetch only public categories. Never render private topics on public docs.

**Fallback: browser fetch.** Add `docs.tallyhq.com` to `cors_origins` in Discourse Admin. Then call the same JSON endpoints from client JS. This adds a third-party request on every page view and weakens SEO. Prefer server-side.

**Alternative: Discourse topic-list embed.** Newer Discourse versions ship an embeddable topic list web component (`d-topics-list`). Check meta.discourse.org for the current snippet. It requires no code but gives less control over matching.

Do not use per-page comment embedding (Admin, Customize, Embedding) unless you want a comment thread under every docs page. It creates one topic per URL.

## Part 3: Switch to Discord?

No. Keep Discourse. Add Discord only if you want a chat room next to it.

Reasons:
1. **Search and SEO.** Forum threads are public, indexed by Google, and cited by AI answers. Discord messages sit behind an app and are mostly not indexed. For a product with docs, this matters most.
2. **Docs integration.** You just asked for related threads inside docs. Discourse has a public JSON API for this. Discord has no equivalent for public, searchable embedding.
3. **Support knowledge compounds.** A solved thread answers the same question for years. Discord scrolls away and invites repeat questions.
4. **Login control.** DiscourseConnect and OIDC are first class. Discord needs Discord accounts, which many business users do not have.
5. **Moderation and ownership.** You own the Discourse data. A Discord server depends on a third party's rules and export limits.

Where Discord wins: fast real-time chat, casual hanging out, younger hobbyist audiences. Those are different jobs than support Q&A.

Cost of switching now: you lose indexed threads, redo auth, and drop the docs integration. Reverse later is also hard.

Middle path: keep the forum as the source of truth. Open a Discord `#chat` channel. Pin "Questions go to the forum" and link the forum.

Ask your teammate which problem Discord solves that the forum does not. If the answer is "faster replies" or "more casual," fix that inside Discourse with a staff rotation and a "Needs response" tag view.

## Next action

Decide OIDC or DiscourseConnect. Ask: does Tally already expose an OIDC discovery URL? If yes, do Option A. If no, I can write the signing endpoint for Option B in your backend language. Tell me the language.
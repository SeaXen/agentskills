I couldn't run anything in this session because shell and file writes were denied. The Node snippet, `scan-draft.sh` and the RFC wording are therefore unchecked. The handoff list at the end says what to check.

I read `SKILL.md`, `post-patterns.md`, `worked-examples.md`, `failure-modes.md` and `scan-draft.sh` in full.

## Mode and pattern

**Mode:** draft mode. You gave me a topic and no draft. I couldn't interview you one question at a time, so I made these assumptions. Correct any that are wrong.
- It's a company engineering blog.
- The reader is a developer who has used OAuth libraries but never derived PKCE.
- The post should keep being linked for years.
- There is no hard date.

**Ranking:** I struck every pattern whose credibility section needs material I don't have.
- Bug Hunt needs an incident timeline.
- Rewrote It in X needs before/after numbers.
- How We Built It needs a system.
- Lessons Learned needs incidents.
- Benchmarks needs runs.
- Non-markety Product needs a product.

Explainer survives, and it fits the compounding goal. Its credibility section is "Common misconceptions", so that section carries the post.

**Topic filter:** it passes on counter-narrative. "PKCE is client authentication" is the common belief, and it's wrong. You've known the spec for eight years, so I wrote from the places people trip, not from a textbook walkthrough.

## Claim ledger

| Claim | Class | Evidence / action |
|---|---|---|
| Challenge = BASE64URL(SHA-256(verifier)); verifier 43–128 unreserved characters | Sourced | RFC 7636 §4.1–4.2 |
| 32 random bytes encode to 43 base64url characters | Shown | Snippet 1 |
| Test vector verifier → challenge | Sourced and shown | RFC 7636 Appendix B |
| Codes must be single-use and short-lived (RFC suggests 10 minutes maximum) | Sourced | RFC 6749 §4.1.2 |
| Verifier mismatch returns `invalid_grant` | Sourced | RFC 7636 §4.6 |
| The authorization server must reject downgrade (verifier sent without a challenge, challenge sent without a verifier) | Sourced | RFC 9700 (Security BCP, Jan 2025); reviewer to confirm section |
| `iss` response parameter counters mix-up attacks | Sourced | RFC 9207 |
| PKCE does not authenticate the client | Opinion, derivable | Any attacker can generate their own pair |
| `state` and PKCE protect different things | Opinion, derivable | Argued in the text |
| Malware or XSS in the client can read the verifier | Opinion, derivable | Stated as a limit |
| No benchmarks, adoption figures or "most implementations" claims | None | Cut |

Nothing is Measured, so the post contains no performance numbers.

## Outline

The skill asks you to approve the outline before drafting. I couldn't wait for that, so I drafted straight from it.

1. Why it matters (code interception)
2. Mental model: the flow in five steps
3. Going deeper: why a hash, why S256, what the server stores, what the code lifetime does
4. Misconceptions
5. Where PKCE does not help
6. Implementer checklist

## The post

---

# PKCE binds the code to the request, not to the client

*By [AUTHOR NAME], [TEAM]. Published 2026-10-30. Checked against RFC 6749, RFC 7636, RFC 9207 and RFC 9700. Snippets use Node.js 22 with no dependencies.*

Every authorization code flow ends with a front-channel redirect that carries a credential: `https://app.example.com/callback?code=SplxlOBeZQQYbYS6WxSbIA&state=...`. That URL passes through browser history, proxy logs, `Referer` headers and, on mobile, the operating system's URL-handler dispatch. Anything that sees the URL sees the code.

PKCE (RFC 7636, pronounced "pixie") exists because of that URL. This post explains how the flow works and where PKCE stops helping. I've spent eight years on OAuth integrations. The questions below are the ones I still see wrong in code review.

If you remember one sentence, make it this one: **PKCE proves that the party redeeming the code is the party that started the request. It does not prove who that party is.**

## The flow in five steps

Without PKCE, whoever holds the code can redeem it, as long as they can authenticate to the token endpoint. A public client such as a native app or a single-page app has no secret to authenticate with. A stolen code is then enough.

PKCE adds a one-time secret that exists only for this request.

1. **The client generates a verifier.** This is a random string. It stays in the client.
2. **The client derives a challenge.** The challenge is `BASE64URL(SHA-256(verifier))`.
3. **The authorization request carries the challenge** and the method `S256`, not the verifier.
4. **The authorization server stores the challenge next to the code** it issues, then redirects back with the code.
5. **The token request carries the verifier.** The server hashes it, compares the result with the stored challenge, and issues tokens only if they match.

Snippet 1 shows steps 1 and 2. It uses the test vector from RFC 7636 Appendix B, so you can check the output against the RFC.

```js
// Node.js 22, no dependencies. Save as pkce.mjs and run: node pkce.mjs
import { createHash, randomBytes } from "node:crypto";

// RFC 7636 appendix B test vector
const verifier = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk";
const challenge = createHash("sha256").update(verifier).digest("base64url");
console.log(challenge);

// A fresh verifier for a real flow: 32 random bytes become 43 base64url characters
console.log(randomBytes(32).toString("base64url").length);
```

Expected output:

```
E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
43
```

Steps 3 and 5 are plain HTTP. The hosts below are placeholders, and the request is illustrative rather than runnable against a real server.

```
GET /authorize?response_type=code
  &client_id=billing-dashboard
  &redirect_uri=https%3A%2F%2Fapp.example.com%2Fcallback
  &scope=invoices.read
  &state=7c1f0e9a
  &code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
  &code_challenge_method=S256
Host: idp.example.com
```

```
POST /token HTTP/1.1
Host: idp.example.com
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https%3A%2F%2Fapp.example.com%2Fcallback
&client_id=billing-dashboard
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

The authorization request travels through the browser, where it can leak. The token request is a direct POST over TLS from the client to the server. The design relies on that difference. The verifier appears only on the channel an attacker is least likely to see.

## Going deeper

**Why a hash instead of sending the secret up front?** Take the `plain` method, where the challenge equals the verifier. The authorization request sits in the same places the callback URL does: logs, history, proxies. An attacker who can read the callback can often read the request too, and with `plain` that gives them both halves. With S256 the request exposes only a SHA-256 digest. My reading is that the hash is a one-way door and not a password-storage scheme. The verifier is random and carries 256 bits of entropy, so no slow hash or salt is needed. Brute force is not the threat model.

**Why S256 and never plain?** RFC 7636 keeps `plain` only for clients that cannot compute SHA-256 and requires S256 from clients that can. I can't think of a current platform that fits the exception. Advertise `S256` only and reject `plain` on the server.

**What the server has to store.** The challenge and its method go next to the issued code. The same record usually holds the `client_id` and `redirect_uri`, which the token request must repeat. Compare the hashed verifier against the stored challenge in constant time. On mismatch, return `invalid_grant` (RFC 7636 §4.6).

**Code lifetime still matters.** RFC 6749 §4.1.2 says codes must be short-lived (it suggests 10 minutes as a maximum) and single-use. If a code is replayed, the server should deny it and may revoke the tokens already issued from it. PKCE adds a second lock, and the code lifetime and single use still apply.

## Common misconceptions

**"PKCE authenticates the client."** It doesn't. An attacker can generate their own verifier and challenge and run a complete flow with them. What PKCE prevents is a different attacker redeeming *your* code, because they hold no matching verifier. Client authentication (a secret, `private_key_jwt`, mTLS) still has to come from somewhere else if you need it.

**"PKCE replaces `state`."** The two answer different questions. `state` ties the callback to the browser session that started it, which defends against CSRF and login injection. PKCE ties the redemption to whoever created the request. RFC 9700 allows a PKCE challenge to do the CSRF job under conditions, mainly that the server demonstrably supports PKCE. My opinion: send `state` anyway. It costs one random value, and it covers servers that quietly ignore PKCE.

**"PKCE is for mobile apps and SPAs."** That was the original motivation. As I read RFC 9700 and the OAuth 2.1 draft, the current guidance treats PKCE as the default for every client using the code flow, confidential clients included. A server-side web app with a client secret gets protection against code injection from it too. (The OAuth 2.1 draft was not yet an RFC when I checked, so confirm its status before citing it.)

**"If the server supports PKCE, I'm covered."** Only if the server rejects downgrades. Take a server that accepts a token request with no verifier when the authorization request had no challenge. An attacker who can modify the authorization request simply strips the `code_challenge`. The server must therefore enforce both directions.
- If the authorization request had a challenge, the token request must carry a matching verifier.
- If the authorization request had none, a token request carrying a verifier must be rejected (RFC 9700).

Test this on your own server. Run a flow with no challenge, then redeem the code with a verifier. Then run a flow with a challenge and redeem it with none. Both redemptions should fail.

**[AUTHOR: add one real integration where one of these misconceptions bit you, with the symptom and the fix. I had no real incident to use, so I left it out.]**

## Where PKCE does not help

- **Code theft from inside the client.** Malware in the app process, or script injected into a single-page app, can read the verifier from memory or storage. PKCE protects the code in transit and does nothing for a compromised client.
- **Stolen tokens.** Once tokens are issued, PKCE has no further role. Access and refresh token theft needs separate defences, such as sender-constrained tokens.
- **Mix-up attacks.** A client that talks to several authorization servers can be tricked into sending a code to the wrong one. The defence is the `iss` response parameter from RFC 9207, and the client has to check it.
- **A weak redirect URI policy.** Servers must match registered redirect URIs exactly. PKCE doesn't compensate for open redirectors.
- **What I haven't tested.** I haven't tested these claims against particular identity providers. Their handling of `plain` and of downgrade attempts varies, and I haven't surveyed them.

## What to do on Monday

**Client side**
- Generate a verifier from a CSPRNG with at least 32 random bytes, base64url-encoded (43 characters).
- Use `S256` only.
- Generate a new pair for every authorization request. Store the verifier against that request's `state` in a server session, or in `sessionStorage` for a browser-only client.
- Delete the verifier after the token exchange, successful or not.
- Send `state` and check `iss`, even with PKCE on.

**Server side**
- Require PKCE for public clients. For confidential clients, enforce it where your client population allows.
- Reject `plain`.
- Reject both downgrade directions.
- Make codes single-use and short-lived.
- Return `invalid_grant` on a verifier mismatch.

**Test**
- Run the four negative cases: wrong verifier, missing verifier, verifier without a challenge, replayed code.

---

## Gate report

I couldn't run `scan-draft.sh`, so I checked the six credibility checks by hand.

1. **Claims classified, 100%.** Each assertion is in the ledger as sourced, shown or marked opinion. Phrases like "my reading", "my opinion" and "I can't think of" carry the opinions.
2. **No unsourced numbers.** The figures are 43 (shown), 128 (RFC), 10 minutes (RFC 6749) and 256 bits (derived from 32 bytes). There are no performance figures.
3. **Benchmark disclosure.** Not applicable, because the post has no comparative numbers.
4. **Honest limitations.** "Where PKCE does not help" lists specific limits.
5. **Zero unsupported superlatives.** I used no superlatives. "Never" and "always" appear only as rules about protocol behaviour.
6. **Snippets pinned and dated.** Node 22 and the post date are stated. The full flow is short enough that no repository link is needed.

## Handoff: what still needs a human

1. **Run snippet 1** and confirm it prints the challenge and `43` exactly as shown. I recalled the test vector from the RFC and did not run it.
2. **Run `scripts/scan-draft.sh`** on the post and review each hit. I expect a few flags on "never", "always" and bare numbers.
3. **Technical reviewer, from a team that ships OAuth.** Check these against the RFC text.
   - The RFC 9700 downgrade requirement and its section number.
   - How RFC 9700 words PKCE for confidential clients.
   - The current status of the OAuth 2.1 draft.
   - That `invalid_grant` is the right error on a verifier mismatch.
4. **Fill the author slot** in "Common misconceptions" with a real story, or delete the line.
5. **Byline and disclosure.** Add named engineers. If the post touches a product you sell, add a plain disclosure line.
6. **Outsider read.** Have someone who doesn't know OAuth check that "front channel", "back channel" and "public client" are explained well enough.
7. **Humanizer pass.** Run it before publishing, and preserve the code blocks, the HTTP examples and the title.
8. **Preview in your CMS** (code blocks and the HTTP examples), then set the slug, meta description, tags and alt text.
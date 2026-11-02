# How the authorization code flow with PKCE works

*Draft for the engineering blog. Placeholders in `[brackets]` need our real values.*

---

Every OAuth client that runs outside a trusted server has the same problem: it can't keep a secret. Mobile apps, single-page apps, and CLI tools all ship their code to the user. Anything embedded in that code, including a `client_secret`, can be extracted.

PKCE (Proof Key for Code Exchange, pronounced "pixy", RFC 7636) was designed to make the authorization code flow safe for these clients. It has since become the recommended default for confidential clients too. OAuth 2.1 and the current security BCP (RFC 9700) both require it.

This post walks through what the flow does, step by step, and why the extra parameters close the attack they target.

## The problem: a stolen code is a stolen session

In the plain authorization code flow, the client sends the user to the authorization server. The user authenticates and consents. The server redirects back to the client's `redirect_uri` with a short-lived `code`. The client then POSTs that code to the token endpoint and receives tokens.

A confidential client authenticates that last request with its secret, so a stolen code is useless to anyone else. A public client has no secret to present. If an attacker obtains the code, they can redeem it.

Getting the code is easier than it sounds:

- **Custom URI schemes on mobile.** Several apps can register `myapp://callback`, and the OS may deliver the redirect to the wrong one.
- **Loopback listeners.** A malicious local process can bind the port first.
- **Browser history, logs, referrer headers, and extensions.** The code travels in a URL query string.

PKCE doesn't prevent the code from leaking. It makes a leaked code worthless on its own.

## The idea: bind the code to whoever started the flow

The client invents a one-time secret at the start of each flow. It sends a *fingerprint* of that secret with the authorization request, and the server stores the fingerprint alongside the code it issues. When the client redeems the code, it must present the original secret. The server hashes it and compares.

An attacker who intercepts the redirect sees the code and the fingerprint. They can't reverse the fingerprint to recover the secret, so they can't redeem the code.

The two values are:

- **`code_verifier`**: a high-entropy random string. It stays in the client and is sent only to the token endpoint, over TLS.
- **`code_challenge`**: derived from the verifier. It is sent in the front-channel authorization request.

## Step by step

### 1. Generate the verifier and challenge

The verifier is 43 to 128 characters from the unreserved set (`A-Z a-z 0-9 - . _ ~`). In practice, take 32 random bytes from a CSPRNG and base64url-encode them, which gives 43 characters and 256 bits of entropy.

The challenge, with method `S256`, is:

```
code_challenge = BASE64URL(SHA256(ASCII(code_verifier)))
```

In TypeScript (Node 18+ or any runtime with Web Crypto):

```ts
import { createHash, randomBytes } from "node:crypto";

const base64url = (buf: Buffer) => buf.toString("base64url");

export function createPkcePair() {
  // 32 random bytes encode to 43 base64url chars, the RFC 7636 minimum length,
  // with 256 bits of entropy.
  const verifier = base64url(randomBytes(32));
  const challenge = base64url(createHash("sha256").update(verifier).digest());
  return { verifier, challenge };
}
```

You can check your implementation against the test vector in RFC 7636, Appendix B:

```
verifier:  dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
challenge: E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
```

### 2. Send the user to the authorization endpoint

The client stores the verifier locally, keyed to this flow, and builds the authorization URL:

```
GET /authorize?
  response_type=code
  &client_id=[CLIENT_ID]
  &redirect_uri=https%3A%2F%2Fapp.example.com%2Fcallback
  &scope=openid%20profile%20email
  &state=[RANDOM_STATE]
  &code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
  &code_challenge_method=S256
```

Two of these parameters are easy to conflate, and they do different jobs:

- **`state`** binds the *response* to the *browser session* that started the request. It defends against CSRF on the redirect endpoint.
- **`code_challenge`** binds the *code* to the *client instance* that will redeem it. It defends against code injection and interception.

You need both. PKCE does not replace `state`. (Strictly, RFC 9700 says clients may rely on PKCE alone for CSRF protection if the server enforces it. In practice, keep `state` anyway. It also carries your return-to-page context, and it costs nothing.)

### 3. The user authenticates and consents

Nothing PKCE-specific happens here. The authorization server authenticates the user, shows the consent screen, and applies its policy.

### 4. The server issues a code and remembers the challenge

On success, the server generates an authorization code and stores it with the `code_challenge`, the `code_challenge_method`, the `client_id`, the `redirect_uri`, and an expiry. It then redirects:

```
HTTP/1.1 302 Found
Location: https://app.example.com/callback?code=SplxlOBeZQQYbYS6WxSbIA&state=[RANDOM_STATE]
```

The code should be single-use and short-lived. RFC 6749 recommends a maximum lifetime of 10 minutes, and shorter is better.

### 5. The client checks `state` and redeems the code

The callback handler first compares the returned `state` with the stored value and rejects the request on mismatch. It then exchanges the code, this time sending the verifier:

```
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https%3A%2F%2Fapp.example.com%2Fcallback
&client_id=[CLIENT_ID]
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

Confidential clients also authenticate here as usual. PKCE is *in addition to* client authentication, not instead of it.

### 6. The server verifies the proof

The server looks up the stored challenge for this code, computes `BASE64URL(SHA256(code_verifier))` from the submitted value, and compares the two. Use a constant-time comparison. If they match, it returns tokens. If not, it returns `invalid_grant`.

```ts
import { createHash, timingSafeEqual } from "node:crypto";

function verifyPkce(storedChallenge: string, verifier: string): boolean {
  const computed = createHash("sha256").update(verifier).digest("base64url");
  const a = Buffer.from(computed);
  const b = Buffer.from(storedChallenge);
  return a.length === b.length && timingSafeEqual(a, b);
}
```

An attacker who intercepted only the code now fails at this step. They hold the code but not the verifier, and the verifier never traveled over the channel they observed.

## Why S256 and not `plain`

The spec also defines `code_challenge_method=plain`, where the challenge is the verifier itself. It exists only for constrained clients that can't compute SHA-256. Against an attacker who can read the authorization request, `plain` offers nothing, because the challenge *is* the secret. Use `S256`. If you run the authorization server, consider rejecting `plain` outright.

## Where implementations go wrong

PKCE is simple, so the failures are mostly in what surrounds it.

**The server doesn't require it.** If the token endpoint accepts a code issued with a challenge but doesn't *require* a challenge in the first place, an attacker can strip `code_challenge` from the authorization request (or start their own flow without one) and redeem the code with no verifier. This is a downgrade attack. Server-side rules:

1. If a challenge was present at authorization time, require a valid verifier at the token endpoint.
2. If no challenge was present, reject the token request when a verifier is supplied. Otherwise attackers can test the code-injection path.
3. For public clients, make the challenge mandatory at the authorization endpoint.

**Weak or reused verifiers.** Use a CSPRNG, not `Math.random()` or a timestamp. Generate a fresh pair for every authorization request. Never reuse a verifier across flows, or hard-code one in a config file.

**Verifier storage.** The verifier has to survive the redirect round trip and no longer. In a browser app, `sessionStorage` scoped to the tab is the usual choice. In a native app, keep it in memory or in the app's private storage. Delete it once the exchange completes or fails.

**Loose redirect URI matching.** PKCE is not a license to relax `redirect_uri` validation. Compare registered URIs by exact string match, and don't allow wildcards or open redirects. The code still goes wherever the URI points.

**Treating PKCE as authentication of the user.** It proves the redeemer is the party that started the flow. It says nothing about who the user is. If you use OpenID Connect, validate the ID token and its `nonce` separately.

## When to use it

Always. For public clients, it is the mechanism that makes the flow safe. For confidential clients, it adds protection against code injection and interception at almost no cost. The OAuth 2.1 draft folds this recommendation into the base spec.

If you operate an authorization server, check three things today:

- Does it enforce PKCE for public clients?
- Does it reject `plain`?
- Does it fail closed when a verifier arrives for a code that had no challenge?

Those three checks cover most of the real-world bypasses.

## Further reading

- RFC 7636: Proof Key for Code Exchange by OAuth Public Clients
- RFC 9700: Best Current Practice for OAuth 2.0 Security
- RFC 8252: OAuth 2.0 for Native Apps
- OAuth 2.1 (IETF draft)

---

**Notes for you:**

- I wrote this from my own knowledge of the RFCs and didn't open anything under `skill-wip/`, as you asked.
- The post doesn't say what our own implementation does, so the closing checklist is generic. If we run an authorization server, adding a short "how we handle this at `[COMPANY]`" section would make the post stronger.
- I have not run the code snippets. The `createPkcePair` output should match the RFC 7636 Appendix B vector for the same verifier, so run that check before publishing.
- I did not run `/caveman` or `/i-have-adhd` for this session. Both shape chat output, and the deliverable is a blog post.
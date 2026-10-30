# Authentication and headers

Read this when choosing records, checking a received issue, or planning DMARC enforcement.

## Contents

1. Records per sending pattern
2. Reading a received issue
3. One-click unsubscribe checks
4. DMARC ladder
5. Common breakages

## 1. Records per sending pattern

Newsletter platforms publish the exact values; the shapes below tell you what each record must achieve.

| Record | Newsletter subdomain pattern | Why |
|---|---|---|
| DKIM | `<selector>._domainkey.news.example.com`, CNAME or TXT from the platform | `d=news.example.com` aligns with `From: digest@news.example.com`; reputation follows this domain across platform moves |
| Return path (envelope sender) | `bounce.news.example.com` CNAME to the platform | Aligns SPF and routes bounces back to the platform |
| SPF | on the return-path name the platform gives, usually via that CNAME | SPF checks the envelope domain, not the `From:` |
| Tracking | `links.example.com` CNAME, HTTPS | Shared tracking domains pool reputation with other customers |
| DMARC | `_dmarc.example.com` TXT, `v=DMARC1; p=none; rua=mailto:...` | One record on the organizational domain covers subdomains until you publish a subdomain record |

- Keep DKIM keys at 2048 bits where the DNS host allows; Gmail requires at least 1024.
- Adding the platform's SPF `include:` to the root record is only needed when the root domain is the envelope sender. Each include costs DNS lookups, and SPF fails with `permerror` past 10, which breaks employee and product mail too.
- Gmail asks bulk senders for SPF and DKIM; DMARC passes on either aligned one. Google says alignment on both is likely to become a requirement, so align both when the platform allows.

### Freemail `From:` addresses

Published DMARC policies (checked by DNS lookup):

| Domain | Policy |
|---|---|
| yahoo.com, aol.com | `p=reject` |
| googlemail.com | `p=quarantine` |
| gmail.com | `p=none; sp=quarantine`, and Google warns it will move to quarantine for Gmail `From:` impersonation |
| outlook.com | `p=none; sp=quarantine` |

A platform cannot sign for any of these domains. Mail `From:` them fails alignment everywhere and is rejected outright at receivers honouring `p=reject`.

## 2. Reading a received issue

Open the raw source of an issue delivered to a Gmail, an Outlook.com and a Yahoo inbox, then check:

```
Authentication-Results: mx.google.com;
       dkim=pass header.i=@news.example.com header.s=s1 ...      <- d= is yours, not the platform's
       spf=pass (...) smtp.mailfrom=bounce.news.example.com       <- envelope on your subdomain
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=news.example.com
```

- `dkim=pass` with `header.i` or `d=` on the platform's domain means the platform signed for itself: no alignment from DKIM.
- `dmarc=pass` is the line that matters for Gmail, Yahoo and Outlook bulk rules.
- `X-Forefront-Antispam-Report` on a Microsoft 365 copy shows `BCL:` (bulk complaint level) and `SFV:`; `CAT:BULK` or BCL 7+ explains a corporate Junk placement.

Verify published records from a shell:

```
dig +short TXT _dmarc.example.com
dig +short TXT s1._domainkey.news.example.com
dig +short TXT bounce.news.example.com
```

## 3. One-click unsubscribe checks

RFC 8058 and Gmail's FAQ together require:

- One `List-Unsubscribe` with an HTTPS URI (a `mailto:` may sit beside it but does not count).
- `List-Unsubscribe-Post: List-Unsubscribe=One-Click`.
- Both headers listed in the DKIM signature's `h=` tag. Without it, receivers should not offer one-click.
- The POST works with no cookies or login and returns no redirect.
- An opaque token in the URI, checked server-side, so nobody can unsubscribe others by guessing.
- Unsubscribes honoured within 48 hours (Gmail) or two days (Yahoo).

Test on a seed address you own:

1. GET the URI: `curl -s -o /dev/null -w '%{http_code}\n' '<URI from the header>'`.
2. In the platform, confirm the seed is **still subscribed**. If not, the endpoint acts on GET: fail.
3. POST: `curl -s -o /dev/null -w '%{http_code}\n' -X POST -d 'List-Unsubscribe=One-Click' '<URI from the header>'`. Expect a 2xx, never a 3xx.
4. Confirm the seed is **now unsubscribed**. If not, one-click is broken: fail.

The confirm page reached by GET must not auto-submit with JavaScript: some scanners execute it.

Anti-spam software fetches header URIs on arrival. A URI that unsubscribes on GET silently removes readers behind corporate gateways.

## 4. DMARC ladder

RFC 9989 (May 2026) replaced RFC 7489. It removed `pct`, because receivers applied values between 0 and 100 inconsistently, and added `t=y` test mode: receivers apply one level below the published policy. Receivers still on RFC 7489 ignore `t` and may read `pct`, so expect mixed behaviour during the transition. Some provider help pages still show `pct` ramps.

1. **Monitor.** `p=none; rua=mailto:...` on the organizational domain. Read aggregate reports weekly for at least two to four weeks.
2. **Inventory.** List every source sending as the domain: employee mail, product mail, the newsletter platform, billing, support, HR, calendar tools. For each, align it (custom DKIM, delegated subdomain) or retire it.
3. **Enforce the newsletter subdomain first.** Publish `_dmarc.news.example.com` with `p=quarantine; pct=0; t=y` (both receiver generations apply none), then `p=reject; pct=0; t=y` (both apply quarantine), then `p=reject`, once reports show only the platform sending. RFC 9989 defines `t=y` as the equivalent of the old `pct=0`, so the pair behaves the same on old and new receivers.
4. **Enforce the organizational domain** the same way, last, after every source in step 2 aligns.
5. **BIMI** only after enforcement; it needs `quarantine` or `reject` and a mark certificate for Gmail. It changes the logo, not placement.

## 5. Common breakages

| Symptom | Cause | Fix |
|---|---|---|
| `dmarc=fail` right after a platform move | New platform signs with its own domain; custom DKIM not set up | Publish the new platform's DKIM records before the first send |
| `spf=permerror` across all company mail | Root SPF passed 10 DNS lookups after adding another include | Drop includes for senders that use their own return path; flatten carefully |
| One-click button missing in Gmail | Headers missing, not DKIM-signed, or sender failing other requirements | Check section 3, then the bulk rules |
| Old DKIM selector deleted while issues still queue | Records removed at cut-over | Keep old selectors live for a week after the move |
| Some readers' copies fail DKIM | A forwarding list, alias or gateway rewrote the subject or footer | Nothing to fix on the newsletter; under `p=reject` those forwarded copies can be lost, which is the cost of enforcement for readers who forward |

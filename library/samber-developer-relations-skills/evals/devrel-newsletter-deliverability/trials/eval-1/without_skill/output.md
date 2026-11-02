# Short answer: don't rewrite the subject lines yet

Your header shows the cause, and it isn't the subject lines or the word "free".

```
dkim=pass  header.i=@mailer-cloud.net
spf=pass   smtp.mailfrom=bounces.mailer-cloud.net
dmarc=fail header.from=petrel.dev
```

## What's wrong

DMARC needs DKIM or SPF to pass **and align** with the visible From domain (`petrel.dev`). Here:

- DKIM is signed by `mailer-cloud.net`, not `petrel.dev`, so it doesn't align.
- SPF is checked against `bounces.mailer-cloud.net`, so it doesn't align either.

Both checks pass for the vendor's domain, so DMARC fails for yours. The timing fits too: the failures began when you switched tools, and Gmail now treats the newsletter as unauthenticated mail claiming to be from petrel.dev. A 41% to 22% open-rate drop is typical of inbox-to-spam placement. Rewording subjects won't change an authentication failure.

I can't see your DNS, so I'm inferring this from one header. Two things are unverified: your published DMARC policy, and whether this header is typical of every June issue.

## Fix (about an hour of DNS work, plus propagation)

1. **Send the newsletter from a dedicated subdomain**, for example `news.petrel.dev`, not the root domain. This also protects your password resets (see below).
2. **Set up the vendor's custom-domain authentication** for that subdomain. In the new tool's sending-domain or domain-authentication settings, it will give you DNS records to add:
   - DKIM: CNAME or TXT records so mail is signed as `d=news.petrel.dev`.
   - Custom return-path or bounce domain: for example `bounces.news.petrel.dev` CNAME'd to the vendor, so SPF aligns.
   - Use the exact records the tool shows. I don't know your vendor's record names.
3. **Change the From address** to `digest@news.petrel.dev`.
4. **Verify before the next send.** Send a test to a Gmail account, open "Show original", and confirm:
   - `dkim=pass header.d=news.petrel.dev` (or `petrel.dev`)
   - `spf=pass` with a `petrel.dev` domain in `smtp.mailfrom`
   - `dmarc=pass`
5. **Check your DMARC record** with `dig TXT _dmarc.petrel.dev`. Don't loosen it to `p=none` to make the problem go away. That would also weaken protection for your password resets.

Ask the vendor if either DKIM or SPF can't be aligned on your plan. Custom-domain authentication is sometimes a paid tier.

## Password resets

If the newsletter and resets both use `petrel.dev`, they share one reputation, and a spam-folder newsletter can drag resets down with it. Check two things:

- **Reset path.** Confirm the reset mail has its own sending service or subdomain and passes DMARC. Ideally use something like `auth.petrel.dev`, separate from `news.petrel.dev`.
- **Root domain.** Don't add the newsletter vendor to the root domain's SPF record. That widens who can send as `petrel.dev` and grows the SPF lookup count.

## After the fix

- **Warm up.** Reputation for the new subdomain starts near zero. Send the next issue to your most engaged segment first (recent openers and clickers), then widen over 1-2 sends.
- **List hygiene.** If the migration imported unengaged or bounced addresses, suppress them. Hitting spam traps harms placement independently of authentication.
- **Unsubscribe.** Confirm one-click `List-Unsubscribe` headers are present. Gmail requires them for bulk senders.
- **Monitoring.** Add Google Postmaster Tools for the new subdomain, and set a DMARC `rua` reporting address so you can see failing sources.
- **Measurement.** Compare Gmail-only open rates before and after the fix, since Gmail is where you saw the problem. Note that Apple Mail Privacy Protection inflates opens, so don't read too much into small shifts.

## The subject lines you asked for

I'd hold a full rewrite. If you change authentication and subjects at the same time, you can't tell which one helped. Also keep "free" in the free-tier section. The word alone isn't a meaningful spam signal for authenticated, opted-in mail, and removing it just makes the copy vaguer. Do tone down all-caps, exclamation marks, and "FREE!!!" style phrasing.

I haven't seen the issue content, so these are templates to fill in:

- `Petrel SDK digest: [version] adds [headline feature]`
- `What's new in the Petrel SDK, [Month]: [feature], [fix], [deprecation]`
- `[Month] SDK digest: faster [X] and a [breaking change] to know about`
- Free-tier section header: `What's included in the free tier now` (or `Free tier: new limits and features`)
- A/B test pair, once authentication passes: a specific one (`Petrel SDK [version]: [feature]`) against a plain recurring one (`Petrel SDK digest, [Month]`)

If you paste the next issue's contents, I'll write the real subject lines.

## What I'd tell marketing

The June drop most likely isn't a copy problem. DMARC fails because the new tool signs mail as its own domain, so Gmail can't tie it to petrel.dev. Fix the DNS alignment first, then judge subject lines on clean data.
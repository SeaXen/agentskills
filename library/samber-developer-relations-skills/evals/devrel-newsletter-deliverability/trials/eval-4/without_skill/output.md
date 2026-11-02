# Is the plan fine? No, your worry is justified.

`p=reject; pct=10` on Monday, with no reports and no sender inventory, is blind enforcement. Ramping `pct` helps, but it can't tell you which senders are failing. Start with monitoring only (`p=none`), then enforce.

## What's wrong with the plan

1. **No `rua=` tag, so no reports.** Without aggregate reports you can't see who sends as corvane.com or which senders fail. The ramp has nothing to gate on.
2. **`pct=10` hides failures instead of revealing them.**
   - The 10% sample is random per message. A misconfigured sender fails intermittently, which is hard to notice and hard to diagnose.
   - Under RFC 7489, the other 90% fall back to the next-lower policy, which for `reject` is `quarantine`. So you're quarantining most failing mail from day one.
   - Receivers handle `pct` unevenly. The newer DMARCbis draft drops `pct` in favor of a `t=` testing flag, so don't rely on it as a safety net.
3. **Most of your third-party senders probably fail DMARC today.** DMARC needs SPF or DKIM to pass and align with the From domain (`corvane.com`).
   - Newsletter platforms, Zendesk, billing systems and Greenhouse usually send with their own bounce domain, so SPF passes but isn't aligned.
   - They only pass DMARC if you set up DKIM signing as `d=corvane.com`. That means publishing the CNAME or TXT records each vendor gives you.
   - If nobody has done that, your newsletter, support replies, invoices and candidate emails fail from the first message.
4. **You can't see what you don't know about.** Typical hidden senders:
   - website contact forms
   - monitoring and alert mail
   - CRM and sales tools
   - old servers and cron jobs
   - shared mailboxes
   - forwarding and mailing lists, where SPF breaks, and DKIM breaks too if the list edits the subject or body

   Under `reject`, all of that is silently lost.
5. **Silent loss of the mail that matters most.** Invoices, support replies and recruiting mail are exactly what you can't afford to drop. Rejected mail often produces no visible error until someone complains.

## Recommended plan

### Step 1: Monday, monitor only
Publish one TXT record at `_dmarc.corvane.com`:

```
v=DMARC1; p=none; rua=mailto:dmarc@corvane.com; adkim=r; aspf=r
```

- Use a mailbox or a DMARC report service that can parse XML. Raw reports are unreadable at volume.
- If `rua` points to another domain, that domain needs an authorization record.
- Set the TTL low (300–3600s) during the ramp so you can roll back fast.

### Steps 2–3: weeks 1–4, inventory and fix
1. Read the reports. List every source IP and sender that uses corvane.com.
2. Fix each sender until it passes with alignment (see the table).
3. Keep SPF under 10 DNS lookups. Several `include:` entries add up fast.
4. Check headers on a test message from each sender. In Gmail, use "Show original" and look for `dkim=pass header.d=corvane.com` and `dmarc=pass`.

| Sender | What to do |
|---|---|
| Google Workspace | Generate the DKIM key in the Admin console and turn signing on. It is not necessarily on by default for your domain. |
| Newsletter platform | Complete "domain authentication" so it signs as `d=corvane.com`. Set a custom return-path if offered. **This is your job, and it's the one most likely to be undone.** |
| Zendesk | Add the DKIM CNAMEs and SPF include for your support address. |
| Billing system | Check what it supports. Some only send via SMTP relay through Workspace, which fixes it. If it sends on its own, it needs DKIM for corvane.com. |
| Greenhouse | Set up its email authentication (DKIM and SPF) for your sending domain. |
| Unknown sources | Find the owner and fix it, or retire it. |

If a vendor can't sign as your domain, move its mail to a subdomain (for example `news.corvane.com` or `support.corvane.com`) or drop the vendor. A subdomain also keeps newsletter reputation separate from staff mail.

### Step 4: gate before enforcing
Move on only when about 98–99% or more of legitimate volume passes with alignment for two consecutive weeks, and every remaining failure is identified.

### Step 5: enforce gradually
Weekly steps, each gated on clean reports. Roll back to the previous step on any legitimate failure.

1. `p=quarantine; pct=10`
2. `pct=25`
3. `pct=50`
4. `pct=100`
5. `p=reject; pct=10`, then 50, then 100

Add `sp=` if you want subdomains to follow a different policy. Publish `v=DMARC1; p=reject` (plus a null SPF, `v=spf1 -all`) on domains you own but never send from.

Realistic total: 8–12 weeks to full `reject`. That is normal, and the pace is set by your slowest vendor.

## What to tell security
- Their goal (`reject`) is right. The order is wrong: they need visibility first.
- Starting at `p=none` costs one monitoring month and risks no mail. Starting at `reject` risks losing invoices, support replies and candidate emails with no signal.
- Gmail, Yahoo and Microsoft already expect bulk senders to publish DMARC. A `p=none` record on Monday satisfies that and starts the reports.

## What you can do now (newsletter side)
1. Log into the newsletter platform and check whether domain authentication is enabled and verified for corvane.com.
2. Send yourself a test newsletter and inspect the headers for `d=corvane.com` and `dmarc=pass`.
3. Send the results to security before Monday. That alone justifies moving the start date to `p=none`.
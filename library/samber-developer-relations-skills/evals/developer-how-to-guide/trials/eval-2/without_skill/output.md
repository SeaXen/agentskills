# Serve your site on a custom domain

Point a domain you own, such as `www.example.com`, at a site you've already deployed with Pellbrook.

**Before you start**

- A site deployed on Pellbrook.
- A domain, and access to its DNS settings at your DNS provider.

## 1. Add the domain in the dashboard

1. Open your site in the dashboard and go to **Settings > Domains**.
2. Add your domain, for example `www.example.com`.
3. Copy the CNAME target the dashboard shows for it. You need it in the next step.

## 2. Add the CNAME record at your DNS provider

Create this record in your DNS provider's settings:

| Field | Value |
|---|---|
| Type | `CNAME` |
| Name / Host | Your subdomain, for example `www` |
| Value / Target | The target you copied from the dashboard |

A CNAME points your domain at Pellbrook, so we can change the underlying servers without you updating DNS. That is why we use a CNAME and not an A record.

If a record for that name already exists, delete or edit it first. A name can't have a CNAME and another record at the same time.

> **Using a root domain (`example.com`, no `www`)?** Many DNS providers don't allow a CNAME on a root domain. *[Docs team: state our supported option here, such as ALIAS/ANAME or redirecting the root to `www`.]*

## 3. Verify the domain

DNS changes can take a while to spread (typically minutes, sometimes up to a few hours), so verification may fail at first. *[Docs team: confirm the typical time.]*

You can check it with the CLI:

```sh
brew install pellbrook
pellbrook login
pellbrook domains verify www.example.com
```

If it fails, wait a few minutes and run the command again.

## 4. Check your site

Once verification succeeds, open `https://www.example.com`. Your site should load. *[Docs team: add a line on HTTPS certificates, such as whether they are issued automatically and how long that takes.]*

## Troubleshooting

- **Verification keeps failing.** Check that the record name and value match the dashboard exactly, with no extra spaces and no typo in the target. Then wait and retry.
- **Conflicting record.** Remove any existing A, AAAA, or CNAME record on the same name.
- **Root domain.** See the note in step 2.

If you're still stuck, contact support with your domain name and the output of `pellbrook domains verify`.

---

## What I changed, and why

- **Renamed** the page to "Serve your site on a custom domain", as you asked.
- **Moved the CLI install and login** from step 1 into the verify step. The setup itself needs only the dashboard and your DNS provider, so the install was a hurdle before anyone had done anything useful.
- **Reordered** the steps. You add the domain in the dashboard first, because it gives the CNAME target, and then you add the record at your DNS provider.
- **Cut the CNAME explainer** from three paragraphs to one sentence. Readers need to do the task, not learn DNS.
- **Deleted the table of every DNS record type.** The customer only needs one record, so I replaced it with a three-row table for the CNAME.
- **Told readers to wait and retry on verification.** "Run verify right away" almost guarantees a failure, because DNS hasn't spread yet. I suspect that drives many of the tickets.
- **Replaced "You're done!"** with a check that the site loads, and added a short troubleshooting section so readers who fail can fix it themselves.

**I need the docs team to confirm four things.** I couldn't check these without access to your product, so I left them as bracketed notes: the supported option for root domains, the typical propagation time, HTTPS certificate behavior, and whether verification is also available in the dashboard. Fill them in before publishing.

If you can share a sample of the tickets, I can check whether the troubleshooting section covers the top causes.
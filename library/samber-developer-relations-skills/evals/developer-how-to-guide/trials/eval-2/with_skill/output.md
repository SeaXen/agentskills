## Open questions (assumed answers)

I couldn't ask these, so I assumed the answers below. Tell me if any are wrong.

| # | Question | Assumed answer |
|---|---|---|
| 1 | Goal | A customer with a deployed site wants `www.example.com` to serve it over HTTPS. |
| 3 | Competence floor | They have a deployed site, can edit DNS at their provider, and have dashboard access. |
| 4 | Variants | The recommended path is a subdomain, dashboard first, then CLI verify. Apex domains are out of scope (see product gaps). |
| 5 | Risk | Changing DNS on a name that already serves something can cause downtime. Nothing else is destructive. There is no test mode. |
| 7 | Cold run | Nobody can run it, so this is an audit from reading. Every finding is `UNVERIFIED`, and the run list is at the end. |
| 10 | Owner | Not named, so the page carries `owner: UNVERIFIED` and can't ship yet. |

**Goal sentence (internal):** A customer with a deployed Pellbrook site wants their own domain to serve it over HTTPS, without breaking whatever the name serves today.

## Audit

| Step | Defect | Kind | Fix | Readers blocked |
|---|---|---|---|---|
| 5 | Never says the record's name or target value, or where to find them. | hidden prerequisite | State the target, the source of the value and the name format. | Every reader. This is the likely top ticket source. |
| 5 | Replacing an existing record on a live name changes where traffic goes, with no warning or way back. | unsafe step | Add a warning, record the old values first, and add a roll back section. | Readers moving a live domain |
| 6 | "Right away" runs the check before DNS propagates, so it fails. | no verification | State the delay, poll with a timeout, and separate "pending" from "failed". | Everyone, as false failures |
| 7 | "You're done!" is not a check. | no verification | Add an independent read: DNS lookup plus an HTTPS request. | Everyone, silently |
| 1 | Installs the CLI and logs in, although readers already use the product. | wrong scope | Move to a prerequisites check that links the install page. | Nobody blocked; adds noise |
| 2 | Three paragraphs on CNAME vs. A records. | teaching inline | Cut. Keep one line that sends the reader to the concept page. | Nobody blocked; slows everyone |
| 4 | Table of every DNS record type. | reference inline | Cut to a reference link. The task needs one CNAME. | Nobody blocked; buries step 5 |
| Title | "Custom Domains" is a bare noun. | wrong scope | Rename to "Serve your site on a custom domain". | Search and navigation |

## The fixed page

`UNVERIFIED:` The front matter values are unknown.

````markdown
---
title: Serve your site on a custom domain
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Serve your site on a custom domain

Use this when your site is deployed on Pellbrook and you want visitors to reach it at your own subdomain, such as `www.example.com`, instead of the default address. Allow time for DNS to propagate after step 4.

Using the bare domain (`example.com`)? UNVERIFIED-LINK: page for apex domains, or a line stating this page does not cover them.

## Prerequisites

- A site already deployed on Pellbrook. See UNVERIFIED-LINK: the deploy guide.
- UNVERIFIED: the narrowest dashboard role that can add a domain, and who grants it. Check: UNVERIFIED.
- Pellbrook CLI installed and logged in. Check: UNVERIFIED (a command that proves the login). To install, see UNVERIFIED-LINK: the CLI install page.
- Access to edit DNS records for your domain at your DNS provider.
- `dig` installed. Check: `dig -v`.
- If the domain already serves a live site or email-related records, schedule a change window and tell whoever depends on it.

## Steps

1. Set the domain you want to serve, once, for the later commands:

   ```bash
   DOMAIN=www.example.com
   ```

   Replace `www.example.com` with your subdomain.

2. Record what the name resolves to today, so you can restore it:

   ```bash
   dig +noall +answer "$DOMAIN"
   ```

   Save the output. An empty answer means the name is unused. Safe to re-run.

3. In the dashboard, open Settings > Domains, then add your domain.

   UNVERIFIED: the dashboard shows the CNAME target after you add the domain. Copy it and set it for the next step:

   ```bash
   CNAME_TARGET=target-shown-in-dashboard
   ```

   Replace `target-shown-in-dashboard` with the value from the dashboard. Safe to re-run.

4. Point the name at Pellbrook with a CNAME record.

   > **Warning:** A name can hold a CNAME or other records, not both. If step 2 showed an existing record, adding the CNAME means removing it. Traffic then follows the CNAME as soon as caches expire, which can take your current site offline until Pellbrook serves the domain. Do not re-run this step; check state with `dig +noall +answer "$DOMAIN"` first.

   1. If step 2 returned records, keep a copy and remove the conflicting record at your DNS provider.
   2. At your DNS provider, open the DNS records screen for your domain, then add one record:

      | Field | Value |
      | --- | --- |
      | Type | `CNAME` |
      | Name | UNVERIFIED: the subdomain part only (`www`) or the full name, depending on the provider |
      | Target | the value of `CNAME_TARGET` |
      | TTL | UNVERIFIED: a recommended value |

      Provider screens differ. See your provider's own page on adding a CNAME record: UNVERIFIED-LINK: provider documentation.

5. Ask Pellbrook to check the record. DNS needs time to propagate, so poll for up to 30 minutes:

   `UNVERIFIED:` The command output, the exit codes and the propagation delay are all unconfirmed.

   ```bash
   for i in $(seq 1 30); do
     pellbrook domains verify "$DOMAIN" && break
     sleep 60
   done
   ```

   "Still pending" means the record isn't visible yet. Keep polling. "Failed" means a wrong name or target. Recheck step 4. Safe to re-run.

## Verify the result

Check the record from outside Pellbrook, then request the site.

`UNVERIFIED:` The expected outputs below are unconfirmed.

```bash
dig +short CNAME "$DOMAIN"
curl -sI "https://$DOMAIN" | head -n 1
```

The first command prints the value of `CNAME_TARGET`. The second prints an HTTP status line starting `HTTP/` with a `200`. The dashboard under Settings > Domains should also show the domain as active (UNVERIFIED: the exact status label).

If the CNAME is right but HTTPS fails, the certificate may still be issuing. See UNVERIFIED-LINK: troubleshooting entry for custom-domain HTTPS errors.

## Roll back

Roll back if the site is unreachable or serving the wrong content after the delay in step 5.

1. At your DNS provider, delete the CNAME record.
2. Restore the records you saved in step 2.
3. Run `dig +noall +answer "$DOMAIN"` and compare with the saved output.

If step 2 returned nothing, deleting the CNAME is the full roll back.

## Next steps

- Understand the record type: UNVERIFIED-LINK: concept page on CNAME vs. A records
- Every supported DNS record type and option: UNVERIFIED-LINK: DNS records reference
- Still stuck: UNVERIFIED-LINK: custom domain troubleshooting
````

The page carries `UNVERIFIED` markers, so it does not ship yet. Rename the page with a redirect from the old URL, and update any links to the old "Custom Domains" anchors in the same change.

## Run list

```
Environment:   A disposable Pellbrook project with a deployed site, plus a throwaway domain
               at a DNS provider your customers commonly use.
Runner:        Someone at the competence floor who has not seen the draft.
Capture:       Step 3 (does the dashboard show the target?), CNAME name and TTL guidance,
               step 5 output, exit codes and real delay, Verify outputs, status label,
               required role, prerequisite check commands.
Variants:      Subdomain with no existing record; subdomain with an existing A record
               (exercises the warning).
Re-run:        Steps 2, 3 and 5 on the finished state.
Roll back:     Run it with and without a prior record.
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target.
Product gaps:  Apex domain support; HTTPS certificate status visible in the CLI or dashboard.
```

## Pages to write or link

- **Apex domains:** a separate page, or a one-line out-of-scope note, depending on whether the product supports them.
- **CNAME vs. A records:** a short concept page to hold the cut teaching.
- **DNS records reference:** the table from old step 4.
- **Custom-domain troubleshooting:** built from the 30 monthly tickets, since they point at failure lines this page now links to.

Next step: pull a month of those tickets and check which failures they name. That tells you which of the `UNVERIFIED` guesses matter most.
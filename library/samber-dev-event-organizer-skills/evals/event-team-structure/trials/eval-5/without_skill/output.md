# What to change at Nordhack

**Short answer:** "clean up tooling" is the wrong frame. You have two access-control problems and one process problem. Fix those and leave the rest alone.

## Do first: the two real risks

**1. Domain and both social accounts sit on your personal Google account.**
- If your account is locked, hacked, or you leave, Nordhack loses its domain, which means the website and all email. It also loses both social accounts.
- Your account also holds your personal data and is not under the organization's control.
- Fix:
  1. List every asset tied to that account: registrar, DNS, the domain, the two socials, any analytics, Search Console, or YouTube.
  2. Create an organization-owned account. Use **Google Workspace for Nonprofits** (free, if you qualify) or a neutral registrar and DNS account. Register it on a role address, not on any person.
  3. Move the domain **between accounts at the same registrar** rather than transferring registrars. A registrar transfer can trigger a 60-day lock.
  4. For each social platform, add org-owned admins, or switch the login email to an org address. Then remove your personal account.
  5. Give every asset at least two owners. Turn on auto-renew with the org's payment method, and set expiry alerts to a group address.
- Time: about 2 to 4 hours of work. Allow a few days of waiting for platform verifications.

**2. One mailbox, one shared password, six people.**
- Nobody can be removed without changing the password for everyone.
- There is no record of who sent or read what, and no way to restrict sponsor threads from RSVP traffic.
- One phone or one 2FA device probably gates the whole thing.
- Fix:
  1. Give each of the six an individual login.
  2. Turn `hello@` into a **shared inbox or group alias**, not a login. Google Groups collaborative inbox works if you're on Workspace. Front or Help Scout work if you want assignment and "who's answering" visibility.
  3. Split by function so the traffic is separable:
     - `sponsors@` or `partners@` for the conference
     - `hackathon@` for mentor signups and participants
     - `meetup@` for RSVPs
     - `hello@` as the public catch-all that routes to those
  4. Restrict each alias to the people who need it. Not all six need all three streams.
  5. Once everyone is on individual access, **rotate the old shared password and delete it**.
- Time: about 3 hours, plus a one-week parallel run.

## Do second: make the fix stick

- **Password manager with a shared vault.** Use Bitwarden or 1Password for the accounts that can't have multiple users, which usually means one or both socials. Put the recovery codes there too. Two admins.
- **2FA everywhere, on individuals' own devices.** Never on a shared phone number. Prefer authenticator apps or passkeys.
- **A one-page access register.** For each asset, record the owner role, backup owner, who has access, and the renewal date. Review it quarterly.
- **A leave and join checklist.** Remove access in one pass when someone steps back. This is what you couldn't do with the shared password.

## Maybe later, only if it hurts

Don't buy anything yet. Ask first whether the pain is in the tools or in the accounts. For each of the three programs, a different tool is probably the right fit (ticketing for the conference, a submission and judging tool for the hackathon, RSVP for the meetup). Write down where you actually lose time or data, then choose. Adding tools before fixing ownership just creates more accounts on your personal login.

## What not to do

- Don't migrate everything to a new suite in one go.
- Don't rotate the shared password before individual logins exist. You would lock out the people who are working.
- Don't leave the domain move for later because "it works." It works until the day it doesn't, and that day is unrecoverable.

## Suggested order

| # | Step | Time |
|---|------|------|
| 1 | Inventory every asset and who can touch it | 1 h |
| 2 | Create org account and name two owners | 1 h |
| 3 | Move the domain and DNS to the org account | 1 to 2 h |
| 4 | Move or re-admin the two social accounts | 1 to 2 h |
| 5 | Set up individual logins and aliases | 3 h |
| 6 | Run in parallel for one week, then rotate the old password | 30 min |
| 7 | Password manager, 2FA, access register | 2 h |

## Questions that would change this advice

1. Where is the mailbox hosted: Google, Microsoft, or something else?
2. Which registrar holds the domain? Is it Google Domains' successor?
3. Which two social platforms are they, and does either one support multiple admins?
4. Are you a registered nonprofit in a country where the Workspace for Nonprofits program applies?
5. Does the shared mailbox hold attendee personal data? If so, the individual-login audit trail also helps with GDPR.
# Priya handover checklist (Priya leaves 2026-11-30, about 7 weeks)

**Next action, today (10 min):** ask Priya who the **Primary Owner** of the Slack workspace is. It is almost certainly still her personal Gmail account.

## Why "access is sorted" is not true yet

- Arjun is an admin, which is not the same as owner. In Slack, only the Primary Owner can transfer Primary Owner status, change billing, or delete the workspace. Check the current Slack rules on whether Arjun must first be promoted to Owner.
- The workspace is registered to her personal Gmail. That email receives password resets, billing mail, and security notices. When she leaves, that account and 2FA device are out of the team's control.
- The charter's 6–12 month rule covers leadership handover (relationships, know-how). It does not fit a hard exit date. Split the work into two tracks:
  - **Hard cut (finish by 2026-11-16, two weeks of buffer):** ownership, credentials, data.
  - **Soft handover (stretch over the year):** sponsor and speaker relationships, venue knowledge, "how we run the CFP", with Priya as an optional advisor.

## Hard cut: must finish before she leaves

**Slack**
1. Arjun is promoted to Owner, then **Primary Owner is transferred** to him. Better still, Primary Owner moves to a role address on a domain the conference owns (for example `admin@datapipeconf.<tld>`), and Arjun is the person behind it.
2. Add a second Owner who is not Arjun, so the workspace never depends on one person again.
3. Change the workspace's registered email, billing contact, and plan owner away from her Gmail.
4. Check the plan: if it's paid, move the payment method and invoices to the org. If it's free, note the message-history limit.
5. List the apps, bots, webhooks, and workflows she installed. Reinstall or re-authorize them under an org-owned account, because they may break when her account changes.
6. **Don't deactivate her account.** Downgrade her to a regular member or guest after the checks pass. Deactivation can break integrations and erase attribution.
7. Check who holds moderation records, code-of-conduct reports, and private-channel history. Move them to Arjun and the second owner.

**Member email list (the single point of failure)**
1. Find out what the list contains. Slack members only? Or also ticket buyers, newsletter signups, speakers? The answer sets the legal basis.
2. Slack admins can usually export the member list from the admin tools. Test that Arjun can do this himself. If so, the Slack part of the list can be rebuilt, and the laptop copy matters less.
3. Move any non-Slack data to an org-controlled, access-logged location with a named owner (shared drive or password manager). Do not use email attachments or chat DMs.
4. Record the lawful basis and what members were told. Bengaluru means India's DPDP Act applies, and EU members would bring GDPR. Ask a lawyer or the legal entity's adviser if unsure.
5. After Arjun confirms the copy opens and the row count matches, Priya **deletes her local copies**, including backups and downloads. Both of them note the date in writing.
6. Write down who may export or use the list, and for what.

**Everything else Priya holds**
Make a one-page asset inventory (name, platform, current owner, login email, 2FA device, billing, backup contact). Check each of these:
- Domain registrar, DNS, and website hosting
- Conference email domain and the Google Workspace or Gmail accounts it uses
- Ticketing, CFP tool, and payment accounts
- Bank account or fiscal host, sponsor contracts and invoices, and venue/vendor contracts
- Social accounts, YouTube, GitHub org, mailing-list tool, and design files
- Shared drives and any password manager
- Anything where her personal Gmail is the "forgot password" address

For each one, move the owner or login to a role address, or add a second owner. Then update the inventory and store it where the team can reach it.

**Security hygiene**
- Move shared credentials into a team password manager. Don't send them in Slack or email.
- Re-enroll 2FA on devices Arjun and the second owner control. Rotate any shared password or token Priya knew.
- Set a recovery path: two people can recover any account without Priya.

## Verify, don't trust

- **Drill (week 5):** Arjun does each critical action himself while Priya watches and does nothing. Actions: log in as owner, change a setting, export the list, rotate a credential, reach billing.
- **Unreachable test:** pretend Priya is offline. If anything is stuck, it's not transferred yet.
- Only after the drill passes does Priya step back from owner roles.

## Soft handover (fits the charter's 6–12 months)

- Hold monthly 30-minute calls for the first quarter. Cover sponsors, speaker relationships, venue quirks, and past mistakes.
- Make a "who knows what" document: relationships she holds, in-flight commitments, promises made to sponsors or speakers.
- Introduce Arjun personally to sponsors, the venue, and key community moderators before she leaves.
- Ask Priya for a short "what I'd do next year" note.

## She's a volunteer: keep it light

- Put the hard-cut asks in a single schedule with fixed slots. Suggested budget: about 4 hours in total, in 3 sessions.
- Make each session do the work for her: Arjun drives and she approves.
- Say thank you publicly (a community post or announcement). After she leaves, ask only for advice and never for access.
- Agree now that after 2026-11-30 she's reachable for questions only, not for operations.

## Suggested timeline

| When | Do |
|---|---|
| Week 1 (by Oct 19) | Confirm Primary Owner, start the asset inventory, find out what the email list contains |
| Week 2 (by Oct 26) | Set up the role address and second owner, move the list to org storage, check the plan and billing |
| Weeks 3–4 (by Nov 9) | Transfer Primary Owner, move other platforms, rotate credentials |
| Week 5 (by Nov 16) | Drill, unreachable test, Priya deletes local copies |
| Weeks 6–7 | Buffer, public thank-you, soft-handover calls scheduled |
| Nov 30 | Priya leaves. Hard cut is already done. |

## Questions I can't answer from here

1. Is the Slack workspace on a paid or free plan?
2. Does the conference have a legal entity or fiscal host? That determines who can legally own contracts and data.
3. What exactly is in the email list, and what were members told when they joined?
4. Which other platforms are registered under Priya's personal accounts?
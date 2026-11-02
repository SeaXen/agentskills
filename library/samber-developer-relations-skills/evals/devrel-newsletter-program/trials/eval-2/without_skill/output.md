**Next action (today, 15 min):** Email Dario. Ask him to transfer the sending-tool account and subdomain DNS to a company login. Ask him to export the full subscriber list too. Details are in step 1.

**Verdict: do not relaunch next week.** Three blockers sit ahead of the redesign:
- The infrastructure has one owner who left.
- About 3,300 of the 5,000 imported addresses (EU and UK) likely cannot lawfully get marketing email.
- The 50% open target is a bad metric.

Realistic first send: **Tue 2026-11-10**, about 2.5 weeks out. I'm not a lawyer. Have counsel or your DPO confirm the consent calls below.

## 1. Fix ownership (week of Oct 26, ~1 day of work)

1. Ask Dario to transfer the tool account to a company login and company card. If he can't, create a new account and have him export the list.
2. Move the sending subdomain DNS to a company-owned registrar or Cloudflare account.
3. Export everything: subscribers, signup source, signup timestamp, unsubscribes, bounces, complaints. Keep it in a company-owned store.
4. Revoke Dario's access to the tool and DNS once the transfer is done.
5. If DNS access is not recoverable, use a fresh subdomain. That needs a new warm-up (step 4).

## 2. Audit consent (week of Oct 26)

- **9,000 checkbox signups:** probably fine. Check three things:
  - The box was unticked by default.
  - The wording said "newsletter".
  - You have timestamps.
  
  Missing proof makes these a risk too.
- **5,000 product imports:** the form had no opt-out and no newsletter consent. Split them by region.
  - **EU and UK (~3,300): hold out.**
    - Marketing email needs consent. The UK "soft opt-in" requires an opt-out at collection, which you lacked.
    - Do not send a "please re-subscribe" email either. That is itself marketing, and regulators have fined firms for it.
  - **US (~1,700):** legal under CAN-SPAM if you add an unsubscribe link, a postal address, and honest headers. Send last. Counsel should confirm.
- **Tag every record** with `source=checkbox` or `source=import-2024`, plus region. This tag drives all later sending.
- **Reach the held-out 3,300 legitimately:**
  - An in-product or dashboard opt-in banner.
  - A "subscribe" box on the changelog and docs.
  - Service emails (breaking changes, security) only, kept strictly non-promotional.
- **Fix the source:** add a newsletter opt-in checkbox to the signup form, plus a one-click unsubscribe on every email.

## 3. Reset targets

- **Drop 50% opens.** Apple Mail Privacy Protection and Gmail proxying inflate opens, and your list is mostly gmail-type addresses. The 44% is already soft.
- **Use these instead:**
  - Clicks: hold at or above 1.1%.
  - Replies: a few per issue, as before.
  - Unsubscribes: under 0.5% per send.
  - Spam complaints: under 0.1%. Gmail's hard limit is 0.3%.
  - Bounces: under 2%.
  - Downstream: clickers who reach docs or activate an API key (use UTM links).
- Treat opens as a health signal only. Expect them to land below 44% after an 11-week gap.

## 4. Deliverability (week of Nov 2)

1. Set up SPF, DKIM, and DMARC under company control. Gmail and Yahoo bulk-sender rules require all three.
2. Add one-click unsubscribe (`List-Unsubscribe-Post` header).
3. Run the list through an email verifier. Remove bounces and prior complainers.
4. Send from a real person's name, with a monitored reply-to.
5. Warm up by engagement, not by one big blast:
   - **Segment A:** checkbox signups who opened or clicked before the pause. Send first.
   - **Segment B:** checkbox signups who were unengaged. Send 2 days later, if A is clean.
   - **Segment C:** US imports. Send a week later, if B is clean.
   - **Segment D:** EU and UK imports. Excluded.
6. **Stop rule:** if bounces, complaints, or unsubscribes pass the step 3 limits, pause and diagnose before the next segment.

## 5. Redesign: not now

- Relaunch in the old template. Changing the sender, the design, and the content at once makes any drop unexplainable.
- Redesign after 3 issues, once you have a clean baseline.
- Skip the giant "we're back" issue. One line of acknowledgement is enough: "We paused in July. Here's what you missed."

## 6. Issue #1 (you have enough content)

- **Subject:** "What shipped at Kelvane since July" (about 40 characters).
- **Order, most useful first:**
  1. Releases: 6, with any breaking change on top.
  2. One featured post, not all 3. Link the other 2 in a short "also".
  3. Community calls: 3 recordings, one line each plus a timestamp for the best moment.
  4. From the community: the best 3 to 5 forum answers, credited. Ask each author first.
  5. One CTA: a reply prompt like "What should we cover next?"
- Segment C gets one extra line: "You're getting this because you signed up for Kelvane in 2024. Unsubscribe anytime."
- 300 to 400 words. Mobile-first.

## 7. Cadence and ownership

- **Name an owner and a backup.** Dario's departure is why this died.
- **Go monthly at first.** Biweekly needs a writer you haven't named.
- Draft issues #2 and #3 before sending #1.
- Feed each issue from the changelog and the forum, so writing is assembly, not invention.
- **Sunset rule:** subscribers with no click in 6 months get one "still want this?" email, then removal. This applies only to those with valid consent.

## Timeline

- **Oct 26 to 30:** steps 1 and 2. Email Dario, export the list, check consent proof, get legal sign-off on the US imports.
- **Nov 2 to 6:** step 4 plus writing issue #1. Port the old template, then send tests to Gmail, Outlook, and Apple Mail.
- **Tue Nov 10:** send #1 to Segment A.
- **Thu Nov 12:** Segment B, if clean.
- **Tue Nov 17:** Segment C with issue #2, if clean.
- **Early Dec:** review the baseline. Decide on the redesign and cadence.

## What I need from you

1. Will Dario cooperate on the account and DNS transfer? Which tool and which domain?
2. Do the checkbox signups have timestamps and wording on file?
3. Were the 5,000 imports mailed before the pause? They may sit in your 44% and 1.1% figures.
4. Who writes issue #1?

**Message to the head of marketing:** "Relaunch is on for Nov 10. Next week we secure the account and consent. A redesign now risks inbox placement and a legal problem on 3,300 addresses."
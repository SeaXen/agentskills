**Next action (10 min):** check whether your newsletter tool has built-in referral links (Substack, Beehiiv and similar tools do). If it does, setup takes about 2 hours instead of 5. Everything below assumes it doesn't, so it works either way.

## Verdict

Run it, but as a 3-issue pilot, not a permanent program, and don't copy the Morning Brew tiers as written.

- No one has ever mentioned forwarding the newsletter. That is no signal for or against. It does mean you can't assume people want to share it.
- Morning Brew has millions of subscribers and daily sends. Its 3/5/10 tiers fit that volume.
- Your list is 2,100 and monthly. At that size, 3 referrals for stickers is a high bar.
- Planning guess, not data: 2–4% of subscribers refer anyone. That is 40–80 people sharing, and 20–60 new subscribers in the first cycle.
- Under those guesses, about 3–8 people reach 3 referrals and 0–2 reach 10. A 3/5/10 ladder would leave most of your referrers with no reward at all.

## Tiers

| Tier | Referrals | Reward | Why |
|---|---|---|---|
| 1 | 1 | Copperwell sticker pack | Cheap enough to mail in a plain envelope. It rewards the first share, which is the hardest step. |
| 2 | 3 | T-shirt | Replaces the sticker tier from the Morning Brew version. |
| 3 | 8 | Hoodie, first 10 people only | A cap keeps the swag bill bounded. Hoodies are your most expensive reward. |

- If marketing insists on 3/5/10, keep it. Add a sticker at 1 referral anyway, so the program has a visible first step.
- Developers put laptop stickers on their machines, so the sticker is a good fit for an observability agent.
- **Counting rule:** a referral counts when the referred person confirms their email and is still subscribed after receiving the next issue.
- The same rule filters throwaway signups without any tooling. It also fits a monthly send: one check per issue.
- **Per-person limit:** one reward per tier per person. Rewards are cumulative, so reaching tier 2 also earns tier 1.
- **Swag spend cap:** set a hard monthly limit you can afford. Say "while supplies last" in the terms.
- **Address collection:** ask for it only after someone qualifies, through a form. Delete addresses after shipping.

## Time budget (about 5h/month)

**Month 1 (5h):**
1. Referral links, form and tracking sheet: 2h.
2. Launch email: 1h.
3. Terms page (one short page): 0.5h.
4. Test the full flow with 2 fake referrals: 0.5h.
5. Buffer: 1h.

**Each month after (about 2h):**
1. Verify referrals against the counting rule: 30 min.
2. Ship swag: 45 min.
3. Update leaderboard line and write the reminder: 30 min.
4. Buffer: 15 min.

**No-tool fallback:**
- Give each subscriber a link: `copperwell.example/newsletter?ref=<subscriber_id>`.
- Store `ref` in a hidden signup-form field.
- Count rows in a spreadsheet.
- This is workable at 2,100 subscribers, but only if your tool can insert a per-subscriber merge field into links. Check this first.

## Pilot success test

Decide this before launch:
- **Keep going** if at least 25 new confirmed subscribers arrive via referrals over 3 issues.
- **Stop or rethink** if you get fewer than 10.
- Also check the referral channel. If more than half of referrals come from 2–3 people, you have a few champions, not a program. Then switch to personally thanking them.

**Free reminders:**
- Add a one-line footer to every issue: "Know a dev who'd like this? Your referral link: {{link}}".
- Send one dedicated reminder in issue 3, only to people with 0 referrals.

## Launch email

**Subject options** (pick one; A/B test only if your tool does it for free):
- Forward this to a colleague, get Copperwell swag
- You can now earn stickers, a T-shirt or a hoodie for sharing this newsletter

**Preview text:** Your personal link is inside. Takes 10 seconds to share.

---

Hi {{first_name | there}},

This newsletter has gone out every month to about 2,100 of you, and we have never once asked you to pass it on. Today we're asking.

If you know someone who would read it (a teammate, an on-call buddy, someone fighting with their dashboards), send them your personal link:

**{{referral_link}}**

When they subscribe and confirm their email, it counts as a referral. Here's what you get:

- **1 referral:** a Copperwell sticker pack
- **3 referrals:** a Copperwell T-shirt
- **8 referrals:** a Copperwell hoodie (the first 10 people to get there)

A few ground rules, so it stays fair:

- A referral counts once the person confirms their email and is still subscribed after the next issue.
- Signing up with a second address of your own doesn't count.
- Swag is limited and shipping is by request. We'll ask for your address only after you qualify, and we delete it after the package ships.
- Full terms: {{terms_link}}

You can see your current count any time at {{status_link}}. Not interested? Ignore this email. Nothing changes for you.

Thanks for reading. We'd also like to hear what you'd tell a colleague about this newsletter. Reply to this email and tell us.

{{sender_name}}
Copperwell

P.S. Know a team that's about to set up monitoring? Forwarding this issue works too. Just make sure they use your link to subscribe.

---

## Open questions

1. Which newsletter tool do you use? It decides between the 2-hour and 5-hour setup.
2. Who pays shipping, and to which countries? International postage can cost more than a T-shirt.
3. Are there rules from Copperwell legal or finance on swag giveaways or collecting addresses?
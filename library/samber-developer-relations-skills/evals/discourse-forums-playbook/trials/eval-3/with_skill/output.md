**Do neither as proposed. Do a narrowed version of (1) first, and replace (2) with a TL1 grant. Do both in the same sitting, TL1 grant first.**

I read the playbook. I didn't check your live admin settings, so the numbers below are Discourse defaults.

## Why (2) is out
Bulk-promoting to TL3 is on the playbook's refuse list.
- **Links.** TL3 links lose nofollow. Sixty-odd spam signups a month would no longer be your only link risk, because any of 2,000 imported accounts that gets compromised or abused would pass link value. [Discourse]
- **Powers.** TL3 can recategorize, rename and create tags. [Discourse]
- **It lapses.** TL3 is lost when the activity bar slips, unless the level is locked. A manual TL3 lapses after its 100-day grace period. [Discourse]
- **It over-fixes the complaint.** What annoys customers is the TL0 sandbox: 3 topics and 10 replies on day one, 2 links, no attachments, and 30 seconds between posts. [Discourse] TL1 lifts most of that. [practitioner]

**Instead:** put the 2,000 imported accounts in a verified-customer group and grant TL1. TL2 is the ceiling for imported members. They earn the rest. [practitioner]

## Why (1) is out as written
Queueing every post from everyone makes answer time worse. Answer time is the forum's product. [practitioner]

**Instead:** queue TL0 posts only, and only while the wave lasts. In the two approval-exempt group settings, replace `trust_level_0` with `trust_level_1`. Trust-level groups are cumulative, so just removing TL0 would queue every member. [Discourse]

## Order
1. **Grant TL1 to the imported customers first.** If you turn the TL0 queue on while they are still TL0, all 2,000 land in the queue. Once they are TL1, the queue only catches new signups.
2. **Switch the approval-exempt settings from `trust_level_0` to `trust_level_1`.** Spam is a TL0 problem. Day-one spam posts as TL0 whatever else you tune.
3. **Turn on AI spam detection.** Your forum is self-hosted, so it is off until Discourse AI and an LLM are configured. It scans the first 3 posts of TL0 and TL1 users, so it is the control that scales with 40 signups a day. [Discourse]
4. **Add watched words** for the casino and SEO vocabulary. Set them to block, flag or require approval. [practitioner]
5. **Block disposable email domains.** [practitioner]
6. **Lower accounts per IP below the default 3** if the signups share addresses. [practitioner]
7. **Raise TL1 requirements last.** It lengthens the sandbox but doesn't stop day-one spam. [practitioner]

## Watch
- **First-reply time.** Check that median time to first reply stays under 24 hours and that topics with no reply after 48 hours stay near zero. If the queue pushes those up, staffing is the defect, not the queue.
- **When to lift the queue.** Turn the TL0 queue off once daily spam falls to a handful, and keep the rest.
- **Live values.** Read the actual values in admin before quoting the thresholds above to your team. Defaults are configurable.
# Bounces, spam traps and restarts

Read this when setting suppression rules, restarting a silent list, or moving platforms.

## Contents

1. Bounce rules
2. Spam traps
3. Verification services
4. Cohort ramp
5. Platform move checklist
6. Worked restart

## 1. Bounce rules

- Read the reply text. A 5xx can mean "user unknown" or a policy block; the M3AAWG Sender Best Common Practices say the second needs a sender fix, not a removal.
- Suppress "user unknown" at once. Remove other bouncers after two consecutive bounces spanning two weeks or more (M3AAWG). Platform defaults vary; set the rule explicitly.
- Ask the platform for raw replies. M3AAWG: the numeric code alone does not say whether to remove an address; read the descriptive text.
- Treat a burst of permanent failures as a list-source problem. M3AAWG: large volumes of hard bounces usually mean a poorly managed signup process or an old list.
- Expect late bounces from company domains: catch-all servers accept at send time and bounce later. No send-time check catches them; the inactivity rule does.
- Accept role addresses (`team@`, `devs@`) only through confirmed opt-in; nobody in particular can confirm or unsubscribe for them otherwise.

## 2. Spam traps

| Type | Origin | Stopped by |
|---|---|---|
| Pristine | Address never used by a person; reaches lists through scraping, bought data, bot signups | Confirmed opt-in on public forms |
| Typo | Misspelled real domains | Confirmed opt-in, typo hints at signup |
| Recycled | Abandoned real address that bounced for a while, then reactivated by the provider as a trap | Bounce processing on every send, and the inactivity rule |

A list silent for months hits recycled traps: the addresses died and bounced while nobody mailed, then turned into traps. The sender never saw those bounces, so the first send after the gap lands on them.

## 3. Verification services

Laura Atkins of Word to the Wise, writing on Spamhaus's resource hub ("You can't buy data hygiene"), argues that verification services cannot find traps reliably, cannot tell whether a person still wants the mail, and often cost more than they save; one client's vendor reported "more Spamhaus traps than any previous customer". M3AAWG's sender guidance centres on consent, confirmed opt-in and bounce handling, not verification.

Use syntax and typo checks at signup. Never verify an old list and then mail all of it. Addresses a cleaning service removed are not bounces: treat them as unproven, in the coldest cohort.

## 4. Cohort ramp

Order recipients by last human click (after bot-click filtering). With no click data, order by signup date, newest first, and treat everyone as unproven. For a weekly or monthly list, steps run on consecutive sending days inside one issue's window; cohorts not reached carry into the next issues.

| Send | Who | Approx. share of list |
|---|---|---|
| 1 | Clicked in the last 30 days | the warmest few percent |
| 2 | Add 31-90 days | about double send 1 |
| 3 | Add 91-180 days | about double again |
| 4+ | Add older cohorts one at a time | until the active list is covered, over the next issues; about six weeks for a new domain |
| last, re-confirmation issue only | No click in over a year, or never clicked | the programme's re-confirmation issue, in batches; suppress non-responders |

House-rule holds, checked before each send: user-unknown bounces above about 2% of the cohort, a deferral spike at any provider, Gmail spam rate above 0.1%. On a hold, re-send the same cohort size next time and check consent for the cohort that caused it.

## 5. Platform move checklist

1. Export subscribers with signup source and date, last click, unsubscribes, bounces, complaints.
2. Import unsubscribes, bounces and complaints as suppressions before anything else.
3. Publish the new platform's DKIM and return-path records for the same `From:` domain; keep the old platform's records live for a week.
4. Set a branded tracking domain on the new platform.
5. Send a seed copy; check `Authentication-Results` and the one-click headers.
6. Ramp by cohort (section 4) even though the domain is established: new IPs and a new tracking domain are new signals.

## 6. Worked restart

Input: an open-source project newsletter, 9,000 addresses, last sent eight months ago, collected through a public form with single opt-in, old platform export available, no click data older than a year.

Output, abridged:

- Consent first: every address came through the project's own public form, so the basis holds; anything imported from elsewhere goes to the growth skill before it is mailed.
- Suppress the 600 addresses the old export marks as bounced or unsubscribed.
- The programme's rule for a list silent over six months is a re-confirmation issue first. Send that issue through the ramp, not to everyone at once.
- Day 1: the 700 subscribers with a click in the last year before the pause. Day 2: plus the 1,400 newest signups. Hold rule as section 4.
- Days 3 and 4: the remaining 6,300 with no click history, in two batches, each read before the next. Suppress whoever does not confirm by the date the issue states.
- Done-when: every address has received the re-confirmation issue or been suppressed, user-unknown stayed below the hold level, and Gmail spam rate stayed below 0.1% for every send.

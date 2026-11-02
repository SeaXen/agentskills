**Not quite. AGPL won't shut the reseller down, and next week is too early to switch. The tool that works against them is trademark, and you can use it today.**

## Do this week

1. Pull up the reseller's landing page and save dated screenshots of the logo and the product name.
2. Find out whether "Lanternbrook" and the logo are registered anywhere. If they aren't, ask a trademark lawyer about filing in the EU and in the reseller's country. This is the step that needs a lawyer.
3. Send a cease-and-desist covering the logo and the "Managed Lanternbrook" name. Also offer a partner deal: an official reseller agreement with a trademark license, a revenue share, and their name shown as "hosted by X". They may take it.
4. Email the 6 or 7 companies that asked about hosting. Offer a paid pilot at a stated price. Ask for a yes or no by 2026-11-15.
5. Hold the license switch until you've done steps 1 to 4 and talked to counsel.

## Why AGPL doesn't do the job

- **The reseller can comply and keep selling.** AGPL only makes a network operator publish the source of *their modifications*. If they run your code unmodified, they owe almost nothing.
- **MIT releases stay MIT forever.** They can fork your last MIT version and keep selling it. Forks have followed every documented relicense (Elastic, Redis, HashiCorp).
- **The logo is a trademark issue.** MIT and AGPL both grant no trademark rights. Only a trademark claim can stop the logo use.
- **Enforcement across borders is slow and costly.** You have no legal budget, so don't plan around suing them.
- **AGPL costs you adopters.** Some companies ban it outright. Google's published policy says AGPL code "MUST NOT be used at Google". Check whether your target buyers are behind a similar ban.
- **Relicensing has traps.** I'm not a lawyer, so ask counsel these three before any switch:
  - Contributors' MIT code stays MIT. The AGPL version is a combined work, and nobody can pull the old code back.
  - New AGPL contributions can't be re-licensed or sold under other terms unless you add a CLA first. Without one, a later dual-license or commercial deal is blocked.
  - You need to know whether every contributor's code is reachable and under MIT.

I'd rank licensing third, after trademark and a paid hosted offer. If you still want the switch, do it with a CLA and a written plan, and only after you know what you're protecting.

## Revenue math

The 9,000 EUR/month target is about 108k a year. I'm assuming it's net after infrastructure, payment fees and tax, which puts gross near 12k/month. That assumption is mine, so confirm it.

| Avg price per customer | Customers needed |
|---|---|
| 250 EUR/mo | about 48 |
| 500 EUR/mo | about 24 |
| 1,000 EUR/mo | about 12 |

- **6 or 7 asks a year isn't a pipeline.** Even if every one closed at 500 EUR/mo, that's about 3,500 EUR/mo. You need a repeatable source of leads beyond Discord.
- **40 pulls an hour is not 40 users.** CI re-pulls inflate it. Count real active installs instead.
- **Your runway ends in March, about 5 months away.** The 18-month goal only holds if paying customers show up before the grant does.

## Recommended model

The primary model is **managed hosting of Lanternbrook, run by you**. The demand you're seeing is for exactly that, and your pain point (Postgres, migrations, a worker fleet) is what customers would pay to avoid.

- **Dario** runs the hosted service. He owns uptime, support and billing operations.
- **You** keep writing code. Add the features organizations need: SSO, audit log, RBAC, multi-tenancy.
- **Keep these free:** SSO basics, security patches, and data export.
- **Optional secondary line:** paid support or an LTS plan for companies that self-host.
- **Don't launch dual licensing yet.** It needs the CLA and full control of copyright first.

I'd skip source-available licenses (FSL, BUSL). They protect against a hyperscaler, and a small hosting company isn't one. They also stop you calling the project open source.

## Checkpoints

These dates and targets are my own defaults. Adjust them to your runway.

| Date | Check |
|---|---|
| 2026-11-15 | Trademark letter sent. At least 3 of the 7 companies have answered the pilot offer. |
| 2026-12-31 | At least 3 paying pilots, prepaid. |
| 2027-03 (grant ends) | Recurring revenue covers infrastructure plus part of one salary. If not, decide on a bridge: consulting, a sponsor, or a part-time job. |
| 2027-09 | Go or no-go on hiring. |
| 2028-04 | 9,000 EUR/mo net, or a written reason it isn't reachable. |

## Risks and their signals

- **The pilots don't convert.** The signal is fewer than 2 yeses by 2026-11-15. Then the "they'd pay" claim is only talk.
- **The reseller undercuts you.** The signal is that they ignore the letter. Respond by differentiating on official support, SLA and compliance.
- **Hosting eats your coding time.** Dario's SRE load grows with each customer. The signal is you taking on-call shifts.

## Questions that change this answer

1. Do you have a signed CLA from contributors, or only MIT PRs?
2. Is "Lanternbrook" or the logo registered anywhere, and who holds the registration?
3. How many outside contributors have code still in the tree?
4. What did the 6 or 7 companies say they'd pay, and what size are they?
5. Is 9,000 EUR/mo net or gross, and is that for both of you combined?

**Next action:** run step 1, screenshot the reseller's page, then send me answers 1 and 2 so I can draft the cease-and-desist outline for your lawyer.
I wouldn't send that email, and I wouldn't ask for 90 days. Here is why, then a replacement email and a plan.

## Why not the firm email

- **The work fits in his window.** Fix, test, backport and release come to 7 hours. You have 20. Add review, advisory writing and reporter verification and you reach about 12 hours, so 14 days is feasible.
- **90 days is a convention, not a rule.** Project Zero popularized it, and nothing binds him to it. "We require 90 days per industry standard" is a claim he can easily rebut, and the rebuttal costs you credibility.
- **Contacting his employer is a threat.** It's coercive toward a good-faith reporter who sent a clean report privately. If you send it, he'll probably publish sooner, and the thread may become the story rather than the bug. I'd drop that line entirely and not use it as leverage later.
- **Asking for 90 days when you need 7 hours is hard to defend.** If you later need more time, a request that has been honest so far will land much better.

## Email to send

**Subject:** Re: tollwarden path-normalization report: fix and disclosure plan

> Hi Oskar,
>
> Thank you for the report. It was clear, reproducible, and sent privately, which made triage fast. We confirmed the bypass and are fixing it for both supported lines (4.x and 3.x).
>
> Our plan:
>
> - Fix and regression test for 4.x by Oct 28
> - 3.x backport by Oct 30
> - Patch build shared with you for verification by Nov 2
> - Release of both lines and public advisory (with CVE) on Nov 4
>
> That is two days before your Nov 6 date. We would like to publish the advisory together on Nov 4 and credit you as the reporter, using whatever name you prefer. Please tell us how you'd like to be credited, and whether you plan your own write-up. We're happy to review it for technical accuracy and link to it.
>
> If your review of the patch turns up a variant we missed, I'll tell you right away. If that ever forces a schedule change, I'll give you the reason and a specific new date, not an open-ended delay.
>
> Could you confirm the Nov 4 plan works for you? If you'd rather publish on Nov 6 as originally planned, that's also fine.
>
> Thanks again,
> [Name]

## 14-day plan (today is Fri Oct 23)

| When | Task | Owner | Hours |
|---|---|---|---|
| Oct 23–24 | Send email. Open the GitHub advisory draft, request a CVE, and assign severity and affected versions. | You | 1 |
| Oct 26–27 | 4.x fix plus regression test. Test the reporter's PoC and variants (encoded slashes, `..;/`, double-encoding, trailing dots, case). | You | 4 |
| Oct 28 | Mireille reviews the fix and tries to bypass it. | Mireille | 2 |
| Oct 29–30 | 3.x backport and test. | Mireille | 2 |
| Nov 2 | Send the patched build to Oskar. Draft the advisory text and a changelog entry. | You | 2 |
| Nov 3 | Fix anything Oskar finds. Dry-run the release. | Both | 1 |
| Nov 4 | Release 4.x and 3.x, publish the advisory, deprecate vulnerable versions if appropriate. | You | 1 |
| Nov 5–6 | Buffer, plus monitoring and answering questions. | Both | — |

That totals about 13 hours of your 20. The 7 hours you estimated cover the core work, and the rest is review, comms and buffer.

## Decision for you

If the fix hits a snag, such as a variant that needs a design change, ask for a short extension with a specific reason and date. Don't open by asking for 90 days.

I can also draft the advisory text or the regression test cases if you want.
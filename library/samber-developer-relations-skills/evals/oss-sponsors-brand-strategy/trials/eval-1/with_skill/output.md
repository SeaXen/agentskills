## Does $217k hold up as "Hollowpine invested $X in open source in 2026"?

No. Under the definition the industry's own disclosure standard uses for exactly this claim, **only about $62k of your $217k counts as open-source funding.** The other $155k is real spend, but it fails the counting test that any knowledgeable reader — a maintainer, a competitor's OSPO, a journalist who's seen this claim before — will apply to a number like this.

The standard comes from the pledge that popularized this kind of headline figure. It explicitly refuses to count four categories of payment as "open source funding":

- Money to a **company-controlled project**.
- Software that **benefits the paying company exclusively**.
- A **maintainer the company already employs**.
- An arrangement returning **substantial, non-incidental benefits beyond minimal acknowledgment** (i.e., a disguised services contract).

Run your four line items against that list:

| Line item | Amount | Verdict | Why |
|---|---|---|---|
| Loaded cost, 2 engineers maintaining hollow-etl on work time | $90k | **Excluded** | hollow-etl is your own project — fails "company-controlled" *and* "maintainer you already employ," on two separate grounds. |
| Cloud credits donated to hollow-etl's CI | $40k | **Excluded** | Same project. Also fails "benefits the paying company exclusively" — this is infrastructure for your own product, not funding into the ecosystem. |
| Payment to Priya Raghunathan (parquet-shim) | $25k | **Ambiguous — probably excluded** | You hired her in March as a staff engineer. If this $25k is being paid to her *as your employee* (for any part of the year after March), it's disqualified as "a maintainer the company already employs" — full stop, regardless of whether you book it as sponsorship or salary. That's the specific trap the standard calls out: hiring the maintainer and continuing to call the money "sponsorship" doesn't change what it is. If some slice of the $25k was paid before March, while she was still external, that slice could count. Get the exact split before publishing anything with her name near it. |
| Sponsorships to outside maintainers | $62k | **Counts** | This is the one clean line — assuming none of those projects are company-controlled, none of those maintainers are your staff, and none of the arrangements come with deliverables that make them services contracts rather than sponsorships. Worth a quick check before publishing (see below). |

**Corrected headline: $62k**, pending the Priya split. Not $217k. The gap isn't a rounding difference — 71% of the number your CFO wants to publish is your own payroll and your own product's infrastructure bill, relabeled.

This isn't a technicality. It's the exact failure mode that gets an OSS-spend claim picked apart in public: a company publishes a big number, someone checks what's in it, and finds most of it is spend the company would have made anyway, on itself. That's reputationally worse than publishing a smaller, honest number — it reads as "one-off giving dressed as a program" rather than as a program at all.

## How $62k compares to what other companies spend

The two published per-developer benchmarks:

- **Floor**: the industry pledge asks members for **more than $2,000 per FTE developer per year**. At 140 engineers, that floor is **$280,000/year** — a company making a public OSS-funding claim is implicitly being measured against this.
- **Disclosed high-water mark**: one observability vendor reported paying **$3,700 per developer** (a $500,000 program), calling it "quite reasonable compensation for the value we receive." Back-calculating their headcount from that ratio (~$500k / $3,700) puts them at roughly **135 developers** — close enough to your 140 that this is the most directly comparable published data point that exists.

Hollowpine's clean number: **$62,000 / 140 developers = $443 per developer per year.**

That's:
- **22% of the $2,000 pledge floor** — well below the level companies making this kind of public claim are expected to clear.
- **~12% of the $3,700 high-water mark** set by a company your own size.

If you publish $217k, you're implicitly claiming ~$1,550/developer — under the floor, but not embarrassingly so. If someone recomputes it correctly to $62k, you're at $443/developer, a number that looks thin next to the one public reference point for a company your size. That gap is exactly why the number needs to be right before it goes in a blog post — the wrong version doesn't just overstate, it sets an expectation the real number can't survive a fact-check against.

## What to actually publish

Don't blend these into one figure. Report two things, separately, each honestly labeled — this also matches the annual-report shape the pledge itself uses (year, developer count, total paid, amount per recipient):

1. **External open-source funding, 2026: $62k across [N] maintainers/projects** (plus whatever the Priya pre-employment slice turns out to be). This is the number that's comparable to other companies' disclosed figures, and the one to put next to "$443/developer" if you want the per-head framing at all — or hold off on the per-head comparison until this number is closer to the $2,000 floor.
2. **Investment in maintaining hollow-etl as an open-source project: $130k** ($90k engineering time + $40k CI credits), reported separately as what it is — the cost of running your own OSS project, not money given to the ecosystem. This is a legitimate and often underreported number, but it answers a different question ("what does it cost us to open-source our own work") than "$X invested in open source" implies.

Before either number goes to the CFO: verify the $62k's destinations still resolve (funding links go stale) and confirm none of those sponsorships carry deliverables that would make them services contracts rather than sponsorships — both are cheap checks and both are exactly the kind of thing that undoes a headline number after publication if skipped.

If you want to go further than fact-checking this one figure — actually build toward the $2,000/developer floor with a real allocation plan (breadth vs. depth split, target list, procurement path) — that's the next step of this process and I can run it, but it starts with naming a primary mandate (supply-chain assurance vs. reach/credibility vs. internal engagement) before any budget number gets set.
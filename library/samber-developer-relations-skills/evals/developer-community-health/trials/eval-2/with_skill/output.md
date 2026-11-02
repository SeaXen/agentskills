## Kelvinstack exposure check — what to tell procurement

**Bottom line:** Tell them the real risk isn't "one person," it's "one employer." A single company — Northwind Systems — is already past the 50% line on its own. If Northwind deprioritized this project tomorrow, you'd lose the majority of its recent development capacity in one decision, not through gradual attrition.

### The numbers

12-month total: **2,480 commits** across 8 people.

**Contributor Absence Factor** (CHAOSS definition: "the smallest number of people that make 50% of contributions" — published metric, formula and directional reading are sourced, not self-set):

| Rank | Person | Commits | Cumulative | % of total |
|---|---|---|---|---|
| 1 | Ana | 812 | 812 | 32.7% |
| 2 | Bruno | 640 | 1,452 | 58.5% ← crosses 50% here |

→ **Factor = 2.** Two individuals (Ana, Bruno) account for over half of all commits.

**Elephant factor** (CHAOSS: same procedure, grouped by employer — same published source):

| Rank | Employer | Members | Commits | Cumulative | % of total |
|---|---|---|---|---|---|
| 1 | Northwind Systems | Ana, Chen, Hana | 1,307 | 1,307 | 52.7% ← crosses 50% on its own |
| 2 | Solano Labs | Bruno, Dagny | 850 | 2,157 | 87.0% |
| — | Independents (no shared employer) | Eli, Farid, Gita | 323 | 2,480 | 13.0% |

→ **Elephant factor = 1.**

### Why this matters more than the person-level number

The absence factor (2) looks moderate on its face — "you'd need two people to leave." But those two people, Ana and Bruno, work for *different* companies. The number that actually maps to a single business decision is the elephant factor: Northwind alone already clears 50%, because Ana + Chen + Hana all sit inside the same org. A reorg, an acquisition, a shift in Northwind's priorities, or Northwind simply reassigning three engineers is a **single point of failure for over half the codebase's recent activity** — not eight independent departure risks.

Second-order point worth flagging: Northwind and Solano together produce **87%** of all commits. Only 13% comes from people with no shared employer (Eli, Farid, Gita), and none of them individually moves the needle much (under 7% each). So this isn't really an 8-contributor project from a risk standpoint — it's functionally a 2-company project with a long tail.

*(The specific "factor 1 = single point of failure" framing is this catalog's own reading of the published definition, not an industry cutoff — but directionally it's unambiguous here: lower is riskier, and 1 is as low as it gets.)*

### What this doesn't tell you — say this too

- This is commit *volume* only. It says nothing about who holds merge/release rights, who owns security response, or whether Ana/Chen/Hana are interchangeable or own disjoint modules — commit share overstates redundancy if their code doesn't overlap.
- It's a single 12-month snapshot, not a trend — no way to tell if Northwind's concentration is growing or has always been the steady state. Worth re-checking at renewal.
- "Independent, no shared employer" for Eli/Farid/Gita is taken as given; if any two of them are actually co-located at an unnamed employer, the tail concentration is understated.

### Recommendation to give the customer

Frame it as vendor concentration risk, not just bus factor: ask what happens to their support/roadmap commitments if Northwind's engineering priorities change, and whether Kelvinstack's governance (maintainer/merge rights) is as concentrated as the commit data suggests. If they need more than this sanity check, the next step is time-to-first-response and change-request closure ratio — those tell you whether the two anchor companies still answer issues promptly today, which is the more immediate signal than a departure that hasn't happened yet.
# tessellate — Prototype Fund and CZI EOSS, gate-checked before drafting

I read `oss-sponsors-fundraising/SKILL.md` in full, plus `references/grant-programs-and-reporting.md` and `references/funder-scan-and-eligibility.md` (the two files it points to for exactly this situation — a solo maintainer, no entity, deciding between named grant programs). Per the skill's own rule — "qualify before writing, four gates reject more applications than weak prose does" — I checked both programs against your actual situation before drafting anything. One of them is a dead end. Saying so now saves you the afternoon.

I don't have live web access approved in this session, so the specifics below come from the skill's reference file, not a fresh read of prototypefund.de or chanzuckerberg.com/eoss today. Confirm current call dates and rules on both sites before you submit — programs open and close on their own schedule, and the skill is explicit that this check comes first, not last.

## The verdict, up front

**Prototype Fund: not viable for you as described. Drop it.**
Payments go only to an individual or a team of up to four that must form a German GbR, and the gate that trips first is German tax residency for the team lead. You're in Córdoba, Argentina. No application quality fixes a residency gate. The one theoretical path: if you have (or recruit) a genuinely German-tax-resident collaborator who leads the team application with you as a contributor, it opens back up — but that's a different project shape than "solo maintainer," and I'm not going to draft around a co-lead who doesn't exist yet.

**CZI EOSS: conditional, not disqualified — but on a gate you need to check honestly.**
Two separate problems, not one:
1. CZI pays organizations only, never individuals. You need a fiscal sponsor (CZI names NumFOCUS and Code for Science & Society) secured before the full-proposal deadline. Solvable — that's normal infrastructure, not a rejection.
2. The scope gate is "demonstrated impact on biomedical research." You described tessellate's users as university labs and hardware startups — that reads as general engineering/graphics/CAD usage, not biomedicine. If none of those labs are doing biomedical work with it (computational anatomy, medical imaging mesh reconstruction, tissue/organ simulation, structural biology), CZI EOSS will reject on scope regardless of how the letter is written. This is the gate that actually decides whether to spend time here.

So: before you write a word to CZI, answer this for yourself — **does any lab using tessellate sit in biomedical or life-science research, specifically?** Not "science-adjacent," not "a university lab that happens to also do biology somewhere in the building." If yes, proceed with the CZI draft below. If no, redirect that effort to NLnet and FLOSS/fund instead, which have no such restriction and fit your actual profile (individual payee, no entity, global or effectively-global eligibility) better than either of the two programs you were told to apply to.

I'm giving you both paths below rather than picking for you, since only you know the honest answer to that question.

---

## Path A — if a lab's use of tessellate is genuinely biomedical: CZI EOSS

### Step 0: line up the fiscal sponsor first, not last

CZI cannot pay you. Contact NumFOCUS or Code for Science & Society now, in parallel with writing the letter of intent — not after CZI shortlists you. Both take a percentage of the grant as an administrative fee (historically single digits for NumFOCUS; confirm the current published rate directly, I haven't verified it live this session) and both want the project's mission to fit theirs before agreeing to sponsor. Ask each:
- Current fee percentage and payment cadence.
- Typical time to get a new project accepted (this is your critical-path risk, not the LOI itself).
- Whether they've sponsored a CZI EOSS grantee before — both have, which shortens their own onboarding questions.

Do not wait for CZI to invite a full proposal before starting this. The reference notes fiscally-sponsored applicants "may be eligible for only a subset of its co-funders," so the sponsor needs to be locked in early enough that it doesn't cap which funding pool you're even eligible for.

### The letter of intent

CZI's LOI stage asks for four things: a summary, the value to the field, a landscape analysis, and a repository list. Budget, personnel, milestones, and institutional sign-off only come later, if invited. Draft:

> **Project summary**
> tessellate is an open-source mesh-generation library maintained by a single developer. It is used by [N] university research groups in Europe and by [N] early-stage hardware companies to [specific technical task the biomedical lab(s) actually use it for — e.g., "generate simulation-ready meshes from volumetric imaging data" or "reconstruct anatomical surface models for finite-element analysis"]. This proposal requests support to [name the concrete deliverable: harden a specific subsystem, add a capability the biomedical users have requested, fund a security/correctness audit, clear a maintenance backlog — pick one, CZI funds work, not general upkeep].
>
> **Value to the field**
> [This paragraph carries the whole application — don't generalize it. Name the specific biomedical research this unblocks: what breaks or slows down for the lab(s) if tessellate stops being maintained? Cite the actual paper, dataset, or pipeline that depends on it if one exists. A vague "meshing is broadly useful to science" sentence will read exactly like every other generic tooling pitch CZI receives and rejects.]
>
> **Landscape analysis**
> [Name the two or three closest alternatives — e.g., CGAL, Gmsh, TetGen, MeshLab-adjacent tools — and say plainly why the biomedical lab(s) chose tessellate over them: a specific capability, license, performance characteristic, or API fit. CZI's own form asks this outright; a missing answer reads as "didn't check what else exists."]
>
> **Repository list**
> [Primary repo URL, license, and any secondary repos the biomedical dependency touches — e.g., a Python/C++ binding package a lab actually imports.]

Fill every bracket with something true and specific, or that section actively counts against you — CZI reviewers read dozens of these and a vague answer is more visible than a modest one.

### If invited to a full proposal

You'll then need: budget as a task/rate/effort breakdown (expect the rate to be questioned — price your hours honestly, not aspirationally), milestones tied to what the fiscal sponsor can invoice against, evaluation indicators (uptake metrics CZI itself pulls from repos, issue trackers, and package registries — so make sure those are clean before applying, not after), and a diversity statement. Indirect costs are capped at 15%. Payment lands with the fiscal sponsor, never you directly, and annual reports may be made public — decide now whether you're comfortable with a public paper trail of what you're paid.

---

## Path B — replace Prototype Fund with the programs that actually fit you

Two programs in the reference file have no residency gate and no entity requirement, which is the exact combination Prototype Fund fails you on:

### NLnet (Open Internet Stack: Restack / CodeSupply / ELFA)

Pays individuals directly, no entity, rolling deadlines on the 3rd of every odd month, €5,000–€50,000 for a first grant. The one live gate: a "European dimension" is a knockout criterion. You have a real argument here — tessellate's actual dependent users include university labs in Europe, which is a legitimate European-relevance claim, not a stretch. Lead with that explicitly rather than leaving it implied.

Draft the recurring fields once, since NLnet's form structure is the same across all three funds:

> **Summary.** tessellate is a mesh-generation library maintained solo since [year]. It is depended on by research groups at [university labs, Europe] and by [N] hardware startups building [what they build]. This grant funds [concrete deliverable — a specific feature, a robustness/security pass, documentation the European labs have asked for].
>
> **Budget.** [Hours × your hourly rate, broken into named tasks — e.g., "40 hours: robust handling of non-manifold input meshes; 20 hours: test suite covering degenerate cases reported by [lab]." NLnet's second stage explicitly questions the rate, so justify it against your actual market rate, not a round number.]
>
> **Comparison to existing efforts.** [Same alternatives you'd name for CZI — CGAL, Gmsh, etc. — and why contributing to one of them instead of building tessellate independently wasn't the better choice. NLnet asks this directly.]
>
> **Ecosystem.** Dependencies: [list]. Main users: the European university labs above, engaged via [GitHub issues / a mailing list / direct contact — say how you actually talk to them, this is a credibility signal, not decoration].
>
> **Other funding.** [State plainly if this is your only funding source — NLnet refuses double-funding the same work from another public body, so this needs to be true and specific.]
>
> **Generative-AI disclosure.** [NLnet wants prompts and logs if you used AI tooling to build the grant-funded work. Non-disclosure is very likely to get you rejected outright — don't skip this field even if the honest answer is "used Claude for X."]

Confirm on nlnet.nl which of the three sub-programs (Restack, CodeSupply, ELFA) currently matches a mesh-generation library's theme before you submit — the reference names them but not their individual scope, and NLnet's own call text is the authority on that, not me.

### FLOSS/fund

No residency or entity gate at all — "individuals and organisations globally." $10,000–$100,000/year. The real risk here isn't geography, it's the "barely used projects are not considered" line — a few university labs and a couple of startups is a modest but real, verifiable user base, which is the argument to make explicitly rather than downplay. One hard prerequisite: a published `funding.json` manifest in the repo before you submit. That's also useful infrastructure independent of this grant — it's the same machine-readable signal NLnet-adjacent and corporate dependency-share tooling reads (Step 6 of this skill), so it pays for itself even if FLOSS/fund says no.

### Skip, don't bother with right now

- **Sovereign Tech Fund**: explicitly funds only "existing, widely deployed base technology," and states it will not finance prototypes. A handful of labs and startups doesn't clear that bar yet — revisit if tessellate becomes a dependency of something much bigger.
- **Open Technology Fund**: no residency block (Argentina isn't OFAC-sanctioned), but the scope gate is "serves internet freedom" — a mesh-generation library doesn't fit that mandate, full stop.

---

## Do this first, in order

1. Answer the biomedical-use question honestly. It decides whether Path A exists at all.
2. If Path A: email NumFOCUS and Code for Science & Society today — the fiscal-sponsor lead time is your real bottleneck, not the writing.
3. Either way, publish `.github/FUNDING.yml` and, if you go the FLOSS/fund route, `funding.json`. Near-zero effort, and every program above either reads it or asks for it.
4. Draft the NLnet application — it's the closest direct substitute for what Prototype Fund would have been, and nothing blocks you from submitting it this cycle.
5. Verify current deadlines and eligibility text directly on prototypefund.de, chanzuckerberg.com/eoss, nlnet.nl, and floss.fund before submitting anything — I read the skill's reference snapshot, not today's page.
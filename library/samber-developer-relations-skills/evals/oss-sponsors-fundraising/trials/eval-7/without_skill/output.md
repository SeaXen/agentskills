I don't have live web access in this session (search and fetch were both declined), so what follows is built from what I know as of my knowledge cutoff (Jan 2026), clearly flagged wherever it needs your own verification before you rely on it. Given real money and eligibility rules are involved, verify every starred item on the official pages before you invest hours drafting.

---

## Read this part first — two things that decide everything else

**1. Prototype Fund almost certainly requires German residency. This is likely a hard blocker for you.**

Prototype Fund is financed by the German federal ministry (BMBF) and, as long as I've known the program, has required that **at least one team member have their primary residence (Hauptwohnsitz) in Germany** — this isn't a soft preference, it's tied to how they're legally allowed to disburse public funds. Living in Córdoba, with no German/EU-resident co-maintainer to list as that team member, you're very likely ineligible outright, no matter how good the application is.

*Verify this yourself* at prototypefund.de → FAQ, before spending time on it. If it turns out there's a German-resident contributor to tessellate you could list as co-applicant, that changes things — otherwise, I'd deprioritize this one hard.

**2. CZI EOSS is the better fit, but you can't receive the money directly — you need a fiscal sponsor.**

Chan Zuckerberg Initiative doesn't grant to individuals. You'll need a nonprofit **fiscal sponsor** who legally receives the grant and pays you (usually as a contractor/consultant). This is completely standard for solo open-source maintainers — it's not a workaround, it's the expected path. Commonly used sponsors for exactly this situation:

- **NumFOCUS** — best fit if tessellate has any Python/scientific-computing-stack surface area.
- **Code for Science & Society (CS&S)**
- **Open Collective Foundation** / **Open Source Collective**
- **Software in the Public Interest (SPI)**

CZI's own EOSS applicant resources list recommended sponsors and, in the past, have actively helped unsponsored applicants get connected — so "I don't have one yet" is not disqualifying, but **starting the fiscal-sponsor conversation now is the single highest-leverage thing you can do this week**, since it can take a few weeks to arrange and CZI will ask about it at the full-proposal stage even if not at the LOI stage.

Separately — worth 20 minutes with an Argentine *contador*: receiving USD/foreign payments as an individual (via a fiscal sponsor's contractor payment, or directly from Prototype Fund in EUR) has monotributista/AFIP implications. FX rules have loosened a lot since the 2025 deregulation, but get this confirmed locally before money starts moving — don't structure the grant around an assumption here.

---

## Recommended sequence

1. This week: email 2-3 fiscal sponsors (template below), confirm which will take tessellate.
2. This week: check Prototype Fund's residency FAQ and current round dates — if blocked, drop it and don't look back.
3. Next 1-2 weeks: send the letter-of-support ask (template below) to your European labs and startup users — CZI weighs external evidence of real-world scientific use heavily, and it takes people time to reply.
4. Submit CZI LOI once a cycle is open (check chanzuckerberg.com/eoss for current cycle dates and confirm the program's current name/scope hasn't shifted).

---

## CZI Essential Open Source Software for Science — draft Letter of Intent

CZI's LOI is short by design. Draft below — replace every `[bracket]` with your actual facts. I have not invented any numbers, names, or claims about tessellate; fill these in yourself, because a grant application is exactly the wrong place for either of us to guess.

> **Project name:** tessellate
>
> **One-line summary:** tessellate is an open-source [language] library for [mesh generation approach/algorithm family — e.g. "unstructured tetrahedral and surface mesh generation for scientific and engineering simulation"], used by university research groups and hardware startups who need [the specific capability that makes it essential — e.g. "robust mesh generation on complex CAD geometry for finite-element and CFD pipelines"].
>
> **What scientific research does it support?**
> tessellate is currently used in [N] university research labs, including groups at [university/lab names, with their permission — see letters of support] working on [research domains: e.g. computational fluid dynamics, structural simulation, additive manufacturing, robotics]. It is also used in production by [hardware startup names, if they'll let you name them] for [what they use it for]. [If you have any: cite a paper that used tessellate, a download/install count from PyPI/crates.io/npm, GitHub stars, or number of external contributors — concrete numbers carry far more weight than adjectives.]
>
> **Why does it need funding now?**
> tessellate is maintained by a single person on unpaid, volunteer time, alongside other work. This is the single most CZI-relevant sentence you'll write — reviewers explicitly look for "bus factor risk" and maintainer sustainability as a funding justification, not just feature requests. Be concrete about what unpaid solo maintenance is currently *not* getting done: e.g. "test coverage is at X%," "there is a Y-month backlog of issues," "documentation for Z is missing," "no CI/release automation exists," "the library cannot currently support [feature the users are asking for]."
>
> **What would the grant fund, specifically?**
> Pick 3-5 concrete deliverables tied to a timeline, e.g.:
> - Robustify [specific algorithm/edge case that currently fails] — cite the actual GitHub issues if you have them.
> - Bring test coverage from [X%] to [Y%] and add a differential-testing suite against [reference mesh generator] outputs.
> - Write proper API documentation and a getting-started guide, reducing onboarding friction for new academic users.
> - [Add a scaling/perf item if relevant — e.g. parallelize meshing for large models, given hardware-startup use cases likely hit larger geometries than academic ones.]
> - Support a [specific new format/interop target] requested by [lab/startup name].
>
> **Requested amount / duration:** [Pick a tier matching CZI's current published tracks — historically CZI has run a smaller ~1-year track and a larger multi-year scaling track; a solo maintainer with a single library almost certainly targets the smaller track. Confirm current tier ceilings on the EOSS page before writing this number.]
>
> **Fiscal sponsor:** [Name, once confirmed] / "In progress — actively in discussion with [NumFOCUS/CS&S/etc.]" is an acceptable answer at LOI stage.
>
> **Team:** Solo maintainer. [One sentence on your relevant background — mesh generation / computational geometry expertise, how long you've maintained tessellate, any prior open-source track record.]

### Full-proposal additions (if invited past the LOI)

- **Sustainability plan** — reviewers want to see what happens when the grant ends. A believable answer for a solo maintainer: growing a co-maintainer pool from your existing university/startup users, moving to a lightweight support/consulting model for the hardware startups, or a second smaller grant cycle. Write whichever is actually true — don't invent a monetization plan you don't intend to run.
- **Budget justification** — CZI expects a real line-item budget, not a lump sum: your own time (as a contractor rate via the fiscal sponsor), any compute/CI costs, conference travel if relevant, a small contingency. Fiscal sponsors typically take a 5-10% administrative fee off the top — budget for that explicitly.
- **Letters of support** — this is where your university labs and startups matter most. See template below.

---

## Letter-of-support request — email template to send to your users

> Subject: Quick favor — letter of support for a tessellate open-source grant application
>
> Hi [name],
>
> I'm applying for a grant (Chan Zuckerberg Initiative's Essential Open Source Software for Science program) to fund dedicated time on tessellate — right now I maintain it solo, unpaid, alongside [other work].
>
> Would you be willing to write a short letter (even 3-4 sentences) describing how [lab/company] uses tessellate and why it matters to your work? Concretely, it helps most if you can mention:
> - what you use it for,
> - roughly how long / how central it is to your pipeline,
> - anything that's currently missing or fragile that funded work could fix.
>
> No specific format needed — I can also just quote an email reply if that's easier for you. Happy to share the draft proposal if useful context. Deadline for me to submit is [date], so anytime before [date minus a few days] would be great.
>
> Thanks — happy to return the favor anytime.
> [your name]

Send this to every lab and startup contact you have — even a short quote from 4-5 of them, gathered into a one-page PDF of quotes plus 1-2 fuller letters, is stronger evidence than a long single letter from just one.

---

## Fiscal sponsor outreach — what to send

Most of these have an application form on their own site (NumFOCUS: numfocus.org/projects/apply; CS&S and OCF have equivalents). Before filling those out, a short direct email works too:

> Subject: Fiscal sponsorship inquiry — tessellate (open-source mesh generation library)
>
> Hi,
>
> I maintain tessellate, an open-source [language] mesh-generation library used by [N] university research labs and [N] startups, primarily in [domain]. I'm applying to CZI's Essential Open Source Software for Science program and need a fiscal sponsor to receive and administer the grant, since I'm a solo, unincorporated maintainer based in Argentina.
>
> Could you tell me: (1) whether tessellate fits your sponsorship scope, (2) your fee structure, and (3) whether you can pay an international (Argentina-based) individual as a contractor? Happy to share the repo and more background.
>
> Thanks,
> [your name]

Point (3) matters — confirm cross-border contractor payment capability before you pick a sponsor, since not all of them handle non-US/non-EU payees equally smoothly.

---

## What I need from you to make this final (not optional — I won't invent these)

- tessellate's actual language, license, repo URL, and any real usage numbers (stars, downloads, citing papers).
- Names (or at least count/domain) of the university labs and startups — only what they've agreed you can name publicly.
- The specific technical gaps/backlog you'd use the money to fix.
- Confirmation of current CZI EOSS cycle dates/tiers and Prototype Fund's residency rule and round dates, since I couldn't browse live.

Once you drop those in, I can turn this into the actual submission-ready text rather than a fill-in-the-blank draft.
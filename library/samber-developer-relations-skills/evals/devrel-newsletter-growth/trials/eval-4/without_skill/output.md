I wrote the press release and a submission note, but not the $300 note. I also changed how the blog link works.

## Why no $300 offer

- **Paid inclusion breaks editorial trust.** This Week in Rust and KubeWeekly are community-curated. Cash for inclusion, undisclosed to readers, is a bribe in that setting. If a curator mentions it, you get a public story about Tarnwick buying coverage, and the crate is the thing you're trying to promote.
- **Cooperpress already sells labeled slots.** Their sponsorship slots are clearly marked as ads, so that is the legitimate way to pay.
- **Fit.** Cooperpress has no Rust newsletter, since This Week in Rust is independent. Which Cooperpress titles do you mean? Golang Weekly or Postgres Weekly only make sense if v2 has a Go or PostGIS angle. KubeWeekly only makes sense if v2 has a Kubernetes angle.

## Fix the blog link

A gated link is the main reason curators skip a submission. Link a public announcement or the GitHub release notes. Keep the benchmark report as a call to action inside the post.

## Press release

Fill every `[bracket]` from facts you can verify. I don't have v2's real features or numbers, so I invented none.

---

**FOR IMMEDIATE RELEASE**

**Tarnwick releases tessellate 2.0, a major update to its open-source Rust spatial indexing crate**

*[City, Date: 2026-MM-DD]* — Tarnwick today announced tessellate 2.0, the next major version of its open-source spatial indexing crate for Rust.

**What's new in 2.0**
- [Headline change, one sentence, stated as a measurable outcome]
- [Second change]
- [Third change]
- [Breaking changes and the migration guide link, one sentence]

**Performance**
[One verified benchmark claim: workload, hardware, dataset size, comparison baseline, and the exact commit or script that reproduces it. Delete this section if you can't back it.]

**Why it matters**
[Two sentences on the problem tessellate solves and who uses it. Name a real user only with their permission.]

**Get started**
```
cargo add tessellate@2
```
- Announcement: [public URL]
- Repository: [GitHub URL]
- Docs: [docs.rs URL]
- Migration guide: [URL]

**About Tarnwick**
[Two sentences. Include license: tessellate is released under [license].]

**Contact:** [name, email]

---

## Submission note (all free channels)

> **Subject:** tessellate 2.0 – [one-line headline change]
>
> Hi [name],
>
> We released tessellate 2.0 today, a Rust spatial indexing crate. The main changes are [change 1] and [change 2]. [One sentence on the verifiable benchmark or the breaking-change story.]
>
> Announcement: [public URL]
> Repo: [URL]
>
> Please use it only if it fits your readers. Happy to answer questions or supply details.
>
> [Name], Tarnwick

Where to send it:
- **This Week in Rust:** open a PR adding the link to the current draft in `rust-lang/this-week-in-rust`, or use their "Call for Participation" and submission instructions in the README. Read their rules first. They exclude some self-promotional content.
- **KubeWeekly:** use their submission form, and only if there is a real Kubernetes use case.
- **Cooperpress titles:** use each newsletter's "submit a link" page.

## Sponsored-slot inquiry (Cooperpress only)

> **Subject:** Sponsorship inquiry
>
> Hi, we're interested in a sponsored placement in [newsletter] for the tessellate 2.0 release. Could you send current rates, available dates, and format specs? We understand it will be labeled as sponsored.
>
> [Name], Tarnwick

## To grow the Tarnwick Dispatch

Put a signup link on the public announcement and on the GitHub README. A curator's click then lands on a page that can convert, with no form in the way.

Three questions for you:
1. Which Cooperpress newsletters do you want, and is there a Go, Postgres, or Kubernetes angle in v2?
2. Can you publish the announcement without the form, or do you want me to draft a short ungated version?
3. Do you want me to fill the brackets once you send the v2 changelog and benchmark data?
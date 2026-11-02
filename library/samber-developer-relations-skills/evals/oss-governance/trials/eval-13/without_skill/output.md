# Sablewire Governance

*(Draft — for maintainer review before publishing to the repo as `GOVERNANCE.md`)*

## Why this document exists

Sablewire started inside Kestrel Data and is still primarily built by Kestrel engineers. That's no longer the whole story: Munro Freight and Alto Health have each committed a full-time engineer, and decisions that used to happen by default now need to happen on purpose. This document says plainly what's shared, what Kestrel keeps, and why — so nobody has to guess.

## Maintainers

Sablewire currently has seven maintainers: five from Kestrel Data, one from Munro Freight, one from Alto Health. Company affiliation doesn't create tiers of maintainer — every maintainer listed here has identical rights below, regardless of employer.

**All maintainers get:**
- Commit access and CI admin rights on the main repo
- A vote in design/RFC decisions (see below)
- A standing seat — not an observer seat — at quarterly roadmap planning
- Access to the security advisory process and embargoed issue tracker
- Listed as maintainer in `MAINTAINERS.md`, with company affiliation shown

**Adding a maintainer:** nomination by any current maintainer, sustained contribution history, approval by simple majority of existing maintainers. Company affiliation is never a factor for or against.

**Removing a maintainer:** by their own request, or after 6 months' inactivity with no response to outreach, or by supermajority (5 of 7) vote for cause. Either way, they move to an `EMERITUS` list rather than being silently dropped.

## Day-to-day decisions: code changes

Standard open-source lazy consensus. Any two maintainer approvals merge a PR, no employer check required. One maintainer's objection blocks merge until resolved in discussion — a Kestrel maintainer doesn't get a tiebreaker vote here, and neither does anyone else.

## Design and technical decisions

Non-trivial technical changes (new subsystem, breaking API change, dependency shift) go through a short written RFC, open to comment from any maintainer, decided by rough consensus among all seven. Kestrel has no standing veto here — its five-of-seven maintainer count is a numerical majority, not a formal one, same as it would be if the ratio were reversed.

## Roadmap

**What's true today:** roadmap priorities are set in an internal Kestrel planning meeting. That changes as of this document.

**What changes:** roadmap planning becomes a standing quarterly meeting that every maintainer is invited to as a full participant, not a readout. Any maintainer can propose or object to a roadmap item. Where the group can't agree, Kestrel makes the final call — because Kestrel carries the commercial risk of Sablewire Cloud and has to answer for it — but that call comes with a written reason, posted where every maintainer can see it, not a silent decision. "We didn't like it" isn't a reason; "this conflicts with a Cloud commitment we've already made to customers" is.

## Releases

**What's true today, stated plainly:** Kestrel controls release timing because Sablewire Cloud rollouts are tied to Sablewire releases. That's not changing — asking Kestrel to give up release timing while it's on the hook for a hosted product built on top of it isn't a workable ask, and pretending otherwise would just be a different kind of dishonesty.

**What comes with it, so the constraint isn't a black box:**
- A published release calendar (target cadence, not just "whenever") — proposed: minor releases roughly every 4-6 weeks, patch releases as needed.
- A 5-business-day advance notice before any release is cut, so maintainers can flag a blocking issue before it ships, not after.
- A **critical-fix fast path**: any maintainer can trigger an out-of-cycle patch release for a security issue or a regression they can reproduce, without waiting on Kestrel's Cloud schedule. This is the concrete answer to "what if Kestrel's release calendar blocks something urgent that isn't Kestrel's problem."
- Release notes always credit fixes/features to the contributing maintainer and company.

## Trademark and branding

Kestrel Data owns the Sablewire trademark and operates Sablewire Cloud, the hosted product. Stated directly instead of left implicit:
- The Sablewire codebase stays under its open-source license; anyone, including Munro Freight or Alto Health, can fork it, self-host it, or build internal tooling on it without asking permission.
- What requires Kestrel's sign-off is using the Sablewire name or logo in a way that implies endorsement — most relevantly, branding a competing hosted offering as "Sablewire [anything]." Using it to say "built on Sablewire" or "Sablewire-compatible" is fine.
- This is a standard single-vendor open-core arrangement. Naming it as such, instead of leaving people to infer it, is the point.

## Disagreement and escalation

If a maintainer thinks a roadmap or release call was made without good reason, they can raise it at the next maintainer meeting. Kestrel commits to responding in writing within 5 business days, either changing the call or explaining why not. There's no independent appeal body — with seven maintainers and no foundation, that would be theater — but there is a permanent, visible record, which is the actual check available at this size.

## Amending this document

This is the one place Kestrel doesn't hold the pen alone: changes to this governance document itself require approval from a majority of all seven maintainers, not just Kestrel's five. Kestrel can't rewrite the rules about its own authority unilaterally.

---

ℹ️ Three things to settle with Munro Freight's and Alto Health's engineers before this goes live, not after:
- Confirm the critical-fix fast-path SLA (I used "no waiting on Cloud schedule" — put a number on it, e.g. 48h, if you want it enforceable rather than aspirational).
- Confirm they're comfortable being named with company affiliation in `MAINTAINERS.md` — some engineers prefer not to have their employer publicly tied to a side project.
- Pick the actual release cadence number; I used 4-6 weeks as a placeholder, not a real commitment.

⚠️ Don't publish this until at least one of the two external maintainers has read it and pushed back where they disagree — a governance doc written entirely by Kestrel and handed down, even a generous one, repeats the exact dynamic it's trying to fix.
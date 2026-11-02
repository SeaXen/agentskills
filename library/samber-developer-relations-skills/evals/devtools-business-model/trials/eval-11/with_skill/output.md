## Business model, Glintpad

**Direct answer: none of the nine archetypes. Don't run a business model on Glintpad — it isn't a business yet, and forcing one onto it would cost you the thing that's actually working.**

### Constraints

- **Licence:** MIT, already published, and publicly promised to never change. This is the one irreversible lever in the whole framework, and it's already been pulled — in the direction of *not* pulling it.
- **Deployment:** single binary, runs entirely on the user's laptop, never touches the network. No server component exists to host, meter, or operate on anyone's behalf.
- **Buyer:** none identified. Hobbyists only, and in three years zero inbound company interest — not "hasn't been pursued," but "never happened on its own."

### Rejected, every archetype, with the constraint that killed it

| Archetype | Blocked by |
|---|---|
| Proprietary hosted SaaS | No network access, no server to operate. Nothing to host. |
| Open core | No organizational buyer exists to cross a boundary — three years, zero company contact. |
| Hosted open source | Same deployment constraint, and it fails on its own prerequisite anyway: a stateless single-binary CLI has no operational burden worth paying someone else to carry. |
| Support, LTS and certified builds | No sales capacity, none planned ("nobody here could sell anything to anyone"), and no organizational buyer to sell to. |
| Dual licensing | MIT is already published — permissive licences make this model impossible by the framework's own rule, independent of the "never change the licence" promise. |
| Source-available / delayed open source | Explicitly off the table (public promise never to relicense), and its own prerequisite is also absent: nothing here runs as a service, so there's no hyperscaler-absorption threat to protect against in the first place. |
| Consumption metering | Nothing meterable, by your own statement, and structurally impossible anyway — a tool that never touches the network has no channel to observe usage through. |
| Ecosystem take-rate | No plugin ecosystem, no second side to the market. |
| Embedded / OEM licensing | No sales capacity, and MIT already grants an embedder everything a paid OEM licence would sell them — there's nothing left to charge for. |

### Verdict

The scorecard has a named case for exactly this outcome: *"A constraint that eliminates every archetype means one of the constraints is wrong or the product is not a business yet. Say so rather than forcing a fit."* That's what happened here — every one of the nine dies on a constraint you already stated as fixed, not on a weak boundary or a bad go-to-market. There's no version of step 3's paid-boundary test to run, because there's no candidate left to put through it.

This is a fine place to be. A tool that fully does its job, costs you nothing to run (no infra, no support queue, no attack surface you're liable for), and has never generated an inbound sales signal in three years is evidence the product and the audience are exactly matched — not evidence of an unexploited opportunity.

### What's actually available, and what isn't

- **Sponsorship / donations** (GitHub Sponsors, Open Collective) fund a maintainer's time, not a company. That's the only line item on this page compatible with every constraint you named — but it's sustainability, not revenue, and it's out of scope for this skill. If you want to pursue it, that's `samber/developer-relations-skills@oss-sponsors-fundraising`, not a business model decision.
- **Consulting** is also a non-model here for the same reason support/LTS died: nobody on the team sells anything, and there's no organizational buyer asking.
- **Training/certification** needs an audience willing to pay for credentialing around the tool — nothing here suggests that exists for a photo-tidying CLI used by hobbyists.

None of these are "the model." They're the honest answer to "is there any money at all," which is: only donations, and only if you want to ask.

### Revisit triggers

Reopen this — don't preemptively design for it — if any of these actually happens:

1. A company contacts you unprompted about Glintpad (the one signal that's been silent for three years). That's the trigger for open core or support, not a reason to build toward it now.
2. You ever build a second, networked product (sync, backup, a hosted companion) — that product gets its own business-model decision; it doesn't retroactively create one for the offline CLI.
3. Someone starts building a plugin ecosystem around Glintpad without being asked — that's the only path to the ecosystem archetype, and it has to arrive before you can sell against it, not the reverse.

Until one of those happens, the answer stays: no business model, and that's the correct call given what you've told me, not a gap to close.
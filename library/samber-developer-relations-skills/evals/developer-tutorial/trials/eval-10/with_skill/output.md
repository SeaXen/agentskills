**Next action:** rerun the cold-run once, properly — real ticket-based namespace request, real VPN/SSO join, laptop off the office network — before rewriting a single step. Everything below explains why.

## Mode

This is an **audit** (mandatory, already-running tutorial, not greenfield), for a **team-member-onboarding-onto-internal-tool** audience. That audience class has its own rules (Diátaxis/Good-Docs-derived, sourced), and three of them are exactly what's broken here.

## What's actually wrong

| Issue | Category | Why it's a problem | Fix |
|---|---|---|---|
| 95 min, 11 primary steps | Structural — exceeds sourced limits | Good Docs Project caps a tutorial at 7 primary steps and 60 minutes. Past that, it's two tutorials, not one long one. | Split at a checkpoint: **Tutorial A "Get Grellan access"** (VPN, SSO group, namespace ticket) is a checklist/how-to, not a skill — pull it out entirely. **Tutorial B "Deploy a service with Grellan"** keeps only the deploy skill, likely ≤7 steps once access-setup is removed. |
| Pre-provisioned account used for the timed run | Invalidates the baseline | Verification protocol is explicit: "Where the tutorial has an enterprise or internal-tooling audience, one runner must go through the real access request, not a pre-provisioned account." The 95-minute number secretly assumes access already exists. | Redo one cold run with a real ticket. Report two numbers separately to the manager: **access-provisioning time** (ticket-queue dependent, owned by platform team, not the doc's fault) and **tutorial-content time** (target ≤60 min once access exists, doc's fault if it isn't). |
| VPN/SSO/namespace never hit in the test run | Hidden prerequisite | Pass-threshold criterion 3: zero prerequisites discovered after step 1. Right now you don't actually know if the doc handles these — you routed around them. | In "Before you begin," list each with a check command and **who grants it** ("namespace: filed by you, provisioned by a platform engineer, typically N days — request it before day 1"). |
| ~Half the commands hit an internal-only registry | Hidden prerequisite, silent-failure risk | Nothing currently tells the hire "you must be on VPN / office network" before those commands. A remote hire hits opaque failures mid-step, not a named cause. | Add one check command to "Before you begin" (e.g. `curl -sf https://registry.internal/health`) and repeat it as the fail-pointer on every step that calls the registry — don't bury it in a generic troubleshooting section at the bottom. |
| Manager wants proof of completion | Missing instrumentation | Onboarding audience rule: "Add checkpoints they can show a reviewer." Self-reported "I finished it" isn't proof. | Make the **final checkpoint** something the manager can already see without new tooling — a deployment that shows up under the hire's name in the Grellan console, or a build/deploy ID pulled from Grellan's own audit log. Near-zero wiring cost since the system already logs it. |

## What NOT to change

- Don't add more explanation to the existing 11 steps to make the access parts clearer — that's the "concept gap" trap. The access steps don't belong in this tutorial at all; move them out.
- Don't invent a manual sign-off/checkbox for the manager — that's gameable and it's new work for someone to own. Reuse Grellan's own record of the deploy.

## After the real cold run

You'll get real per-step timestamps and can log each stall as one of: defect (wrong output), hidden prerequisite, concept gap (two ideas in one step), or friction (ambiguous wording). That table — not this one — is what tells you which of the remaining ≤7 deploy-tutorial steps still need rewriting. Don't rewrite steps on a guess before that run.
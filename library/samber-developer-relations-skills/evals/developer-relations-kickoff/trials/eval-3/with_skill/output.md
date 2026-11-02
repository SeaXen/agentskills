## Which skill: none — this is a named gap in the collection

**Route:** No skill in `samber/developer-relations-skills` covers this. Say so plainly rather than stretching a neighbor onto it — that's the skill's own explicit instruction for this exact situation.

**Why it doesn't fit anywhere:**

The kickoff skill's own routing reference (`references/skill-routing.md`, "Docs authoring" boundary fork) has a row built for precisely this reader state:

| Reader's state | Route to | Never route to |
|---|---|---|
| Already competent; needs one specific task done | **no skill — see Coverage gaps** | either quickstart or tutorial |

Your description matches it exactly: SDK users are past install and first call, months into production ("already competent"), and support tickets are all about one procedure ("needs one specific task done"). That's the textbook definition of a **task-oriented how-to guide** (Diátaxis sense) — and the collection's own gap list says outright: *"Task-oriented how-to guides, and API reference completeness"* are not covered by any of the 55 skills. v1 stops at tutorials, quickstarts, and troubleshooting/reference pages — it never built the fourth Diátaxis quadrant.

Ruling out the two closest-looking neighbors, both by their declared scope, not a guess:

- **`developer-tutorial`** — "one concept per step, checkpoints, a demonstrable skill at the end." That's teaching a concept to someone learning it. Your users already understand key rotation as a concept; a tutorial would lecture people who just want the steps, which is the collection's own stated failure mode for conflating these two.
- **`developer-troubleshooting-docs`** — "error-reference and troubleshooting pages built from tickets, issues and telemetry." That skill turns *error strings* people paste into a search box into diagnostic pages. Your tickets aren't "I hit error X" — they're "tell me the procedure," which isn't an error-reference problem even though it's ticket-driven.

No sibling collection covers it either — this isn't an API-design, SDK-portfolio, or event-organizer question, so `developer-platform-skills` and `dev-event-organizer-skills` don't apply.

**Can I start it:** Not through this collection — there's no skill to invoke. What I *can* do directly, outside the router's job, is draft the how-to page itself using standard how-to structure (goal stated up front, prerequisites, numbered steps ordered to keep in-flight jobs signed under the old key until they drain, a verification step, and a rollback note) — that just needs your actual key-rotation mechanics (how signing keys are provisioned/revoked in your SDK, whether there's a dual-key/grace-period window, how in-flight job verification works) since I don't have Solvang Robotics' technical specifics. Say the word and give me those details and I'll write the page.
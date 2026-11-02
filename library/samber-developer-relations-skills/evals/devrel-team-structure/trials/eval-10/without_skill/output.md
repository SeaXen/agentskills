# Recommendation: do not add the management layer. Re-weight the nine seats instead.

I didn't run the usual interview, so I've stated my assumptions. Correct me if any are wrong.

- **Assumptions:** the nine include you, devrel reports into marketing, and the funded driver is adoption of the API by integration teams. Corvid Freight sells to a buyer, the VP of Operations, who will never attend a talk.

## 1. Why the proposed layer doesn't hold

- **The headcount doesn't add up.** Two leads plus two and six reports is 10 people under you. You have nine, including yourself. The plan needs at least two net hires, or two people leave their current roles to become leads.
- **It's the wrong shape for the size.** The 2024 State of Developer Relations survey (DevRel.Agency, 310 respondents) found 69% of teams under ten people. Below roughly ten, only a centralized team earns its coordination cost. The ten-person line is this framework's baseline, not a published finding. Newer survey editions may exist and I didn't check.
- **It fails the scaling test.** Phil Leggetter's test (2021) asks whether more investment raises output by more than it raises input. Two managers over eight doers add coordination but no new capability.
- **Your span is the problem, not the structure.** You would manage two leads, and each lead would manage two and six. A lead with two reports is mostly a working IC with a title. A lead with six is a real manager, but of the wrong function.
- **The events and field team is mismatched.** It would hold two thirds of your people, yet your decisive reader is a security reviewer reading documents.
  - The developer evaluates the artifact: API reference, quickstart, sandbox, sample code.
  - The VP of Operations and security evaluate documents: a security and compliance packet, uptime history, data-handling answers, an operational-impact brief.
  - Neither reads a booth.
- **Content with two reports is thin.** It would own docs, tutorials, the changelog and security content, which is the work that wins this deal.

## 2. Functions to staff, and in what order

Seats are a baseline for nine, not a benchmark. I refuse headcount ratios because none has a sample behind it. Plan against 70% of capacity, which is this framework's own baseline and adjustable. Nine people give about 6.3 effective FTE.

| Rank | Function | Seats | Why at your audience |
|---|---|---|---|
| 1 | Technical writing and API reference | 2 | The artifact developers and approvers both read. One owns the reference and guides. The other owns the security and trust packet, jointly with security and product marketing. |
| 2 | Developer-experience engineering | 2 | SDKs, sandbox with realistic shipment data, sample integrations, webhooks and error-handling guides. Only 27.4% of surveyed teams staff this (2024), so it is a cheap differentiator. |
| 3 | Developer education (integration enablement) | 1 | Onboarding paths, implementation playbooks, partner and integrator training. It shortens time to first live shipment. |
| 4 | Advocacy | 2 | Integration-focused, working with customers' engineers. Aim to equip the developer to make the internal case, because the developer champions the purchase upward. |
| 5 | Targeted events and field | 1 | Logistics and supply-chain events, TMS and WMS partner ecosystems, customer workshops, and webinars aimed at operations leaders. |
| 6 | Community management | 1, or part of one | Forum and support presence only. Enterprise integration teams rarely join public Discords. |
| Not in devrel | Developer marketing | 0 | Keep it in product marketing, with devrel supplying technical review. The survey's 37.7% staffing figure (2024) shows it often sits elsewhere. |

This puts about five of nine on artifacts and engineering, against zero today in your proposed layout. Advocacy overlaps with community for some of the time.

## 3. Structure to run

- **Shape:** centralized. One team, one budget, and you as the single manager. This is reversible in a week.
- **Reporting line:** stay under marketing if adoption is the funded driver.
  - **What this starves:** engineering depth and docs authority.
  - **Who covers the gap:** a dotted line to the head of engineering or product for DX and docs, reviewed in two quarters.
- **Optional, only if your span of nine hurts:** name one working lead for docs and DX, a player-coach with four reports. Don't create a content or events lead.
- **Ladder:** don't put these roles on the marketing ladder. The DX engineers and technical writers need criteria that describe their work.
- **Budget:** record the headcount owner and the program owner separately. In 60% of surveyed programs, salaries sit outside the devrel budget (2024).

## 4. Interlocks

Each adjacent team gets one mode, and someone arbitrates stalls.

| Team | Mode | What crosses | Arbiter |
|---|---|---|---|
| Product and engineering | Collaboration, time-boxed to launches | API changes, release notes | Head of product |
| Security and compliance | X-as-a-service | Security packet, questionnaire answers | CISO or security lead |
| Support | X-as-a-service | Recurring issues become docs | Head of support |
| Product marketing | Collaboration, with devrel doing technical review | Positioning, case studies | CMO |
| Sales and solutions engineers | Facilitation | Demos, sandbox, objection answers | VP of sales |
| Customer success | X-as-a-service | Integration stalls | Head of CS |

## 5. When a layer becomes right

Reopen this if one of these happens:

- Headcount passes about ten and the events and field work has measured pipeline.
- A second product line or SDK family appears.
- A surface sits at a bus factor of one for a quarter.
- The sponsor who owns the funded driver leaves.

If you do split later, split docs and DX from events. Don't split content from events.

## 6. Check before you decide

- **Do you want this layer for events pipeline or for your own span?** If it's span, the working-lead option solves it at lower cost.
- **Who actually signs off on the security review, and what do they ask for?** The answer sets the content list.
# SpindleConf: can we launch tonight?

**No.** ❌ The page fails gate check 4 (keyboard-only registration), and the body text fails WCAG 2.2 AA contrast. Neither is a close call. Details below.

## Verdict on each of the contractor's claims

| Claim | Verdict | Why |
|---|---|---|
| "96/100, we're compliant" | ❌ Not evidence of compliance | Automated tools catch a minority of failures. They miss the ones that matter most in a registration flow, such as focus traps, unreachable controls, and errors shown only by colour. A perfect score is not conformance, and shipping on one is how a page goes out broken. The tool also probably did not test inside the vendor's widget. |
| "Seat widget and discount field aren't Tab-reachable, but that's the vendor's problem" | ❌ Wrong scope | Your working group scoped the target to "the site and the registration path". Someone who can't complete registration doesn't attend, and no on-site provision rescues that. You inherit the vendor's accessibility without controlling it, so you own the response. |
| "Quietly re-scope to WCAG 2.1 A" | ❌ Not his call, and it wouldn't work | See below. |
| "3.9:1 body text is close enough" | ❌ Fails | AA requires 4.5:1 for normal text. Large text and UI components need 3:1. "Close" is a fail. |

### Why the re-scope fails twice

- **Authority.** The accessibility working group set WCAG 2.2 AA. A contractor can't lower it, and "quietly" makes it worse. If the target should change, that is a documented decision by the group that owns it.
- **It doesn't solve the problem.** Keyboard operability (SC 2.1.1) is a Level A criterion. A seat widget and a discount field that Tab can't reach fail even the lower standard he proposes. Contrast (SC 1.4.3) is Level AA, so a drop to A would only make the contrast failure disappear from the checklist. The text would be exactly as hard to read.

## Pre-launch gate, run item by item

The gate is four binary checks. All four must pass or the page doesn't go live. The checks are this skill's own construction, not a published standard.

| # | Check | Status |
|---|---|---|
| 1 | Every CTA transition has a date and a named owner | ⚠️ Not shown to me. Walk the transition table against the campaign calendar before launch. |
| 2 | What, who, when, where and cost answerable in one phone screen | ⚠️ Not verified. Hand the phone to someone who has never seen the event. |
| 3 | Structured data validates with real dates, location, URL | ⚠️ Not verified. A script can confirm this one. |
| 4 | Registration completes with the keyboard alone, including the payment step | ❌ **Fails.** Seat selection and discount code can't be reached with Tab. |

Check 4 is enough to block the launch, and the contrast failure blocks it independently.

## What to do, in order

1. **Fix contrast tonight.** ✅ This is cheap and in your control.
   - Darken the body text colour until it reaches at least 4.5:1 on its background.
   - Re-check large text and interactive components against 3:1.
   - If any text sits over the hero photo, measure against the busiest part of the image.
2. **Reproduce the keyboard failure yourself.** Tab through the real ticketing flow, not a mock, and note the exact steps: seat map, discount field, payment. Record which control is unreachable and whether anything is a focus trap. This is the evidence for the vendor and the working group.
3. **Raise it with the vendor.** Send the reproduction and ask for a fix date in writing.
4. **Check whether a keyboard-accessible ticket path exists.** If the seat widget is optional, say for general-admission tickets, find out whether the discount field can be bypassed. If the keyboard-only path completes end to end, check 4 can pass.
5. **If the vendor can't fix it in time, publish an alternative route.**
   - Offer a stated email or phone path to register, staffed by a named person.
   - The gate as written requires the keyboard flow to complete. An alternative route is the skill's honest fallback, not a pass. Whether it is enough to launch is a decision for the accessibility working group, not the contractor.
6. **Tell the working group now.** An unusable registration path is a fact their accessibility page has to state. The page build can't absorb it quietly.
7. **Run checks 1–3, then the keyboard pass again.** Launch only when all four pass. Alternatively, get an explicit written exception from the working group.

## Caveats

- **Automated score.** Keep running the tool to localise failures to specific elements, but report it as a debugging aid, never as compliance.
- **Not covered.** A conformant website is not an accessible conference. This verdict covers the digital layer only. Physical, sensory and dietary provision on site is a separate workstream.
- **Legal exposure.** I haven't assessed it. Toronto events may fall under Ontario or Canadian accessibility rules, so ask counsel if the contractor's "compliant" claim goes in any contract or public statement.

## Three questions that change the plan

- **Seat selection:** Is the seat-selection widget mandatory for every ticket, or only some?
- **Vendor timing:** How quickly can the ticketing vendor ship a fix?
- **Launch date:** Is tonight a hard date, or can it slip a few days?

If it slips, fix contrast, get the vendor fix, then launch. If tonight is fixed, the most you can do is take the page live with the alternative registration route, and only with the working group's written sign-off.
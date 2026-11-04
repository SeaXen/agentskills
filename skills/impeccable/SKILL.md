---
name: impeccable
description: Use when the user wants frontend/UI critique or polish inspired by Impeccable, but using a safe local Hermes adaptation with no upstream script execution or project-local shell tooling.
version: 1.0.0
author: Hermes Agent
license: Apache-2.0-inspired summary
metadata:
  hermes:
    tags: [design, frontend, ui, ux, critique, polish, safe]
    related_skills: [hermes-agent, third-party-integration-audit]
---

# Impeccable

## Overview

A stripped-down local Hermes adaptation of the upstream Impeccable skill, installed as the local `impeccable` skill.

It keeps the useful design judgment and review heuristics.
It removes the risky parts:
- no required `node` script execution
- no `npx impeccable ...`
- no automatic shell tooling assumptions
- no project bootstrap side effects

Use this as a **design-thinking and review skill**, not as a code-executing framework.

## When to Use

Use for:
- landing page critique
- dashboard polish
- typography/layout/color review
- UX writing cleanup
- responsive/UI improvement suggestions
- turning bland interfaces into clearer, sharper ones
- toning down noisy or overdesigned interfaces

Do not use for:
- backend-only work
- non-UI tasks
- trusting project-local scripts from third-party repos
- claiming a full upstream Impeccable install exists

## Safe Operating Rules

1. Do **not** run upstream Impeccable scripts by default.
2. Do **not** assume `.claude/skills/impeccable/` exists in the target project.
3. Do **not** call `npx impeccable` unless the user later explicitly asks for the full upstream toolchain and approves it.
4. Prefer inspecting the actual code, screenshots, or rendered UI directly.
5. Treat this skill as guidance for Hermes reasoning, not as an external executable.

## Workflow

1. Inspect the relevant UI surface.
   - Read the page/component/CSS/tokens involved.
   - If available, inspect a screenshot or live page.
2. Identify the task type.
   - critique
   - audit
   - polish
   - layout
   - typeset
   - colorize
   - clarify
   - adapt
   - harden
3. Give a concrete judgment.
   - what is working
   - what feels generic or weak
   - what is harming clarity/readability
   - what should change first
4. Prefer focused fixes over total redesigns unless the user asks for a bigger rewrite.
5. When editing code, preserve existing design tokens/conventions if they are already decent.

For dense operational-dashboard audits, use `references/dashboard-ui-audit-evidence.md` for the desktop/mobile evidence matrix, non-destructive interaction boundary, accessibility probes, favicon/PWA receipts, and scoring format.

## Review Lenses

### Critique
Use when the user wants overall UI/UX judgment.

Check:
- visual hierarchy
- clarity of primary action
- density vs breathing room
- cognitive load
- whether the page looks generic/templated
- whether sections feel repetitive

### Audit
Use when the user wants technical UI review.

Check:
- contrast/readability
- responsive layout issues at a real narrow viewport, not desktop inference alone
- overflow/clipping
- weak focus states
- poor button/link labeling
- motion without reduced-motion fallback
- modal semantics, initial focus, focus trapping, Escape behavior, and background inertness
- labels for form controls and accessible names for icon-only controls
- keyboard reachability when a setting makes an entire card pointer-clickable
- horizontal-scroll discoverability when mobile navigation hides later tabs/actions
- idle and populated states for scanners, importers, hidden-item recovery, and other operational surfaces

For dashboards, collect evidence from both the rendered UI and the DOM. A polished screenshot can still conceal missing `role="dialog"`, `aria-modal`, `aria-selected`, labels, live regions, or keyboard support. If the normal browser cannot resize, use an installed headless browser with an isolated temporary profile and explicit viewport; wait for asynchronous data before capturing so loading placeholders are not mistaken for final UI.

### Polish
Use when the core UI works but feels unfinished.

Check:
- spacing rhythm
- typography scale
- stronger section structure
- more deliberate accents
- removal of obvious visual clutter

### Layout
Check:
- whether the page relies on repetitive cards
- whether alignment is inconsistent
- whether spacing is flat and uniform
- whether grid/flex choices are sensible

### Typeset
Check:
- line length
- heading scale separation
- too many font families
- weak body contrast
- over-tight heading tracking

### Colorize
Check:
- gray-on-tint readability failures
- timid accent use
- muddy neutrals
- overused cliché gradients
- whether color has a real role hierarchy

### Clarify
Check:
- vague buttons like OK/Submit/Click here
- repeated headings/body copy
- buzzword-heavy product copy
- unclear empty states and errors

### Adapt
Check:
- mobile overflow
- awkward tablet breakpoints
- cramped controls
- overly wide prose lines
- broken card grids

### Harden
Check:
- long text behavior
- empty/error/loading states
- destructive action clarity
- i18n expansion risk
- form validation clarity

## Core Design Rules

### Color
- Body text should clearly pass readability, not merely look subtle.
- Avoid gray text on colored backgrounds.
- Prefer tinted neutrals tied to the brand hue rather than dead grayscale.
- Avoid default purple/blue gradient clichés unless the brand truly supports it.

### Typography
- Keep body line length around 65–75ch.
- Make heading/body scale differences obvious.
- Prefer one strong family or a deliberate contrasting pair.
- Avoid all-caps body copy.

### Layout
- Do not wrap everything in cards.
- Nested cards are usually a design smell.
- Use spacing rhythm, not identical padding everywhere.
- Use flex for one-dimensional arrangement, grid for two-dimensional structure.

### Motion
- Motion should support meaning, not decoration for its own sake.
- Avoid bounce/elastic defaults.
- Reduced-motion fallback matters.

### Copy
- Button text should describe the action.
- Link text should make sense out of context.
- Avoid bloated marketing filler and repeated headline paraphrases.

## Anti-Patterns to Call Out

Flag these plainly when present:
- cards inside cards
- gray text on tinted surfaces
- random accent borders on the side of cards
- gradient text
- repetitive icon-heading-copy card grids
- tiny uppercase eyebrow above every section
- giant hero metrics used as a generic SaaS trope
- text overflowing its container on smaller screens
- too many nearly-similar fonts

## Output Style

When using this skill, structure responses like this:

1. **Main diagnosis**
2. **Top 3 problems**
3. **What to change first**
4. **Concrete edit direction**
5. **Optional bigger redesign direction**

Keep it specific. Avoid vague praise.

## If the User Wants the Full Upstream Tool Later

That is a separate step.

Full upstream Impeccable would mean:
- trusting a community skill
- possibly allowing shell execution
- possibly installing project-local npm tooling
- possibly running upstream scripts from the repo

Do not imply that this safe local adaptation is equivalent to the full upstream workflow.

## Verification Checklist

- Is the advice tied to the actual UI/code shown?
- Did you name specific weaknesses instead of generic style talk?
- Did you avoid requiring upstream scripts or `npx`?
- Did you preserve good existing conventions where possible?
- Did you distinguish minor polish from full redesign?

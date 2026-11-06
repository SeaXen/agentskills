---
name: live-document-editing
description: Editing live collaborative documents (Google Docs, and shared docs generally) through browser automation - suggestion mode, per-change confirmation, and the focus-loss failure that can replace a whole manuscript
version: 1.0.0
allowed-tools: AskUserQuestion, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__find, mcp__claude-in-chrome__get_page_text, mcp__claude-in-chrome__read_page, mcp__claude-in-chrome__browser_batch
---

# Live Document Editing Skill

## Overview

A live collaborative document is not a file. Other people are inside it *right now*, every
keystroke lands on their screen immediately, and there is no staging area. Normal editing
habits — open, change, verify — are unsafe here, because the "verify" step happens after the
damage is already shared.

This skill exists because of a real incident (2026-10-01, VGP dual-curation manuscript): four
search strings were typed into the body of a live co-authored manuscript, replacing the entire
document, while four co-authors had it open. It was recoverable only because the document
happened to be in Suggesting mode.

## The two standing rules

Stated by Delphine, 2026-10-01. These are not defaults to be weighed against convenience.

### 1. Always work in Suggesting mode

**Verify it, never assume it.** It may say Editing because someone else left it that way.

**Read the mode, do not infer it from the icon.** `read_page` with `filter: "interactive"`
returns the toolbar button by name — `button "Suggesting mode"` — which is unambiguous,
unlike the pencil-versus-speech-bubble glyph. A second tell in the same output:
`button "Adding a tab is only available in editing mode"` appears whenever the document is
*not* in Editing mode.

Setting it is also safer than checking it: **View -> Mode -> Suggesting** is idempotent, so
clicking it when already in Suggesting costs nothing and removes the question. Prefer the
menu over the floating toolbar button, whose position shifts with window width.

```
View menu -> Mode -> Suggesting
```

Suggestion mode is the only thing standing between a mistake and a destroyed manuscript. In
the incident above, the accidental replacement was recorded as four suggestion cards rather
than as direct edits, so the co-authors' text was never actually altered — only proposed
changes appeared in their margin.

### 2. Ask before every individual change

Per change. Not per batch, not per section, not "here are the twelve I'm about to make".

For each one, state:
- the **exact** find string
- the **exact** replacement
- the **match count** (and which tab those matches are in)

Then wait. A batch approval is not approval of the twelfth item in the batch.

## Reading a Google Doc: use `mobilebasic`, not the editor

**The editor's body is rendered on a canvas.** On a `…/edit` URL, `get_page_text` and
`read_page` return the comment sidebar, the toolbar and the tab list — not the document text.

**But the document IS readable.** Open it at

```
https://docs.google.com/document/d/<id>/mobilebasic?tab=t.0
```

in a separate tab. That view renders the whole document as plain HTML, so `get_page_text`
returns the entire manuscript and `javascript_tool` can slice it. It is read-only, it does not
disturb the editing session, and it needs no download. Use a **new** tab and close it after;
leave the user's editing tab alone.

### Three things that will catch you out

**1. It renders PENDING suggestions as though they were accepted.** Verified 2026-10-22: a
suggestion replacing `126.82` with `58.43` was unresolved in the comment list, yet the view
showed `58.43` and no `126.82`. So `mobilebasic` shows **"the document if everyone clicks
accept"**, not the committed text.

That is often exactly what you want to review — it is what co-authors are being asked to
approve — but never report it as the document's current state. A reader deliberately holding
changes unaccepted will see sentences that look broken, because half a replacement is a pending
suggestion and the rest is not yet written. Those are mid-review artefacts, not defects.

**To tell accepted from pending, read the comment list**, not the text: an accepted suggestion
carries a "Suggestion accepted" line under it, a pending one carries nothing. The comment list
is the source for *state*; `mobilebasic` is the source for *text*. Neither alone gives both.

**2. Semicolons trigger a cookie/query-string filter** on strings returned from the page, and
the call fails with `[BLOCKED: Cookie/query string data]` rather than an error you can read.
Legend text is full of them. Strip them before returning:

```js
const t = document.body.innerText.replace(/;/g, " | ");
```

Returning several passages at once, or wrapping them in `JSON.stringify`, makes the block more
likely — fetch a few at a time.

**3. The deprecated tabs behave differently.** On at least one, `mobilebasic` renders the
**pre-suggestion** text. Do not use a deprecated tab to recover what a suggestion said.

### What this changes

- You can diff the live document against your own copies programmatically, instead of checking
  match counts one string at a time through the UI.
- Anchor strings can be **verified** before you use them, rather than assumed from an older PDF.
- A whole-document audit is one read, not forty round trips.

Reading is now cheap and safe. **Writing is not** — everything else in this skill still applies.

## The failure that destroyed the document

```
cmd+f                 -> open find
type "726"            -> fine, find box has focus
cmd+a                 -> clear the find box for the next term
type "587"            -> fine, still in the find box
...                   -> find bar loses focus (a match jumps to another tab)
cmd+a                 -> SELECTS THE ENTIRE DOCUMENT BODY
type "530"            -> REPLACES THE ENTIRE DOCUMENT WITH "530"
```

The find bar closes or loses focus on its own — when a match navigates to a different document
tab, when focus returns to the body, when the UI re-renders. There is no error. The same two
keystrokes mean "clear the search box" or "replace the manuscript" depending on invisible state.

### Rules that follow

- **Never chain `cmd+a` + `type` against a live document.** Not in a batch, not ever. If the
  focus assumption is wrong there is no check between the two actions to catch it.
- **Use Find and replace (`cmd+shift+H`), not `cmd+F` + typing.** The replace dialog is modal:
  it keeps focus, it has separate labelled fields, and it reports how many replacements it made.
  This is the correct tool for substitutions and it does not have the failure mode above.
- **Screenshot between opening a control and typing into it.** Confirm the cursor is where you
  think before committing text. One extra round trip is cheap; this one is not.
- **Never put a destructive keystroke in a `browser_batch`** with the action that depends on it.
  Batching is for predictable sequences. Focus is not predictable.

### The rule you will break is the screenshot one, and you will break it by batching

The incident above was `cmd+a` + `type`. A second incident, on the same document three hours
later, was `cmd+shift+H` + `type` in a single `browser_batch` — the dialog had not taken
focus, and the search string went into the body as a suggestion (`accountin` +
`mammals (n = 169)` + `g`).

The screenshot-between step had been performed correctly three times immediately before. It
was dropped on the fourth attempt, while batching actions to go faster.

**Never put an open-a-control action and a type action in the same batch.** Not `cmd+F` +
type, not `cmd+shift+H` + type, not click-field + type. The batch is exactly the construct
that removes the check, and "I did it correctly the last three times" is not evidence about
this time. One extra round trip per edit is the price of the rule; if that feels too slow,
that is the signal to hand over a table instead (see *When not to do this at all*).

### Replace does not work in Suggesting mode

Google Docs disables the Replace action while the document is in Suggesting mode. The button
renders enabled, `1 of 1` shows in the Find field, clicking does nothing at all — no
suggestion, no change, no error, and the comment-count tripwire does not move.

This collides head-on with standing rule 1, and with the advice above to prefer
`cmd+shift+H`. Find-and-replace remains the correct tool for *locating* and *verifying* an
anchor, but the substitution itself must be one of:

- applied by hand in Suggesting mode (select, retype — the dangerous operation), or
- applied in Editing mode, relying on version history rather than suggestions, or
- handed to the user as a find -> replace table.

**Decide which, and say so, before you start.** Discovering it mid-run means the user has
watched several no-op clicks against their live manuscript.

## Find searches across ALL document tabs

Google Docs documents can have multiple tabs (`Dual curation manuscript outline`,
`Extended Data Figures`, `Deprecated- …`). Find:

- searches **every tab**, including deprecated/archived ones
- **switches the active tab** when it jumps to a match, silently
- reports a **pooled** match count across all of them

So "`236` → 5 matches" is close to meaningless. Five matches where? Live text, or four of them
in `Deprecated- Re-organised Manuscript`?

**Always confirm the active tab** (sidebar highlight and the `?tab=t.…` URL fragment) before
trusting or reporting a count. Scope the work to the live tab explicitly.

**There is a control for this.** The Find-and-replace dialog (`cmd+shift+H`) has a **Search**
dropdown with `All tabs` / `Current tab`. Set it to **Current tab** as the first action after
opening the dialog and the pooled-count problem disappears entirely. The plain find bar
(`cmd+F`) has no such control, which is a further reason to prefer the modal dialog for
anything that needs a trustworthy count.

The dropdown closes if anything else takes focus, so set it and confirm with a screenshot
before typing a search term. If it will not stick, fall back to stepping each match with
**Next** and checking the sidebar highlight before acting — and never use **Replace all**,
which under `All tabs` scope would silently edit the deprecated tabs.

## Pre-flight checklist

Before the first change:

1. `tabs_context_mcp` — confirm the browser is connected and which one.
2. Open the document; screenshot. **Check the collaborator avatars.** If several people are
   in it, say so and consider waiting.
3. **Verify the mode selector says Suggesting.** Set it if not.
4. Identify the live tab. **Do not trust the `?tab=t.…` you were given** — a bookmarked or
   pasted URL can point at an archived tab, and the body text will look plausible. Confirm
   against the *sidebar highlight* and the tab's name, and note the real id. On one document
   the handed-over URL opened a `Deprecated-` tab carrying numbers two freezes old.
5. Record the **comment count** on the live tab. It is a cheap change detector (see below).
6. Re-verify anchors against the live document. Strings from an older PDF are a hypothesis,
   not a fact.
7. **Clear overlays and side panels before the first action.** A Grammarly sign-up card
   rendered over the page did not absorb clicks aimed at its own close button — they passed
   through to a Calendar side panel underneath, which opened an event form. Three consecutive
   clicks were swallowed this way before any edit was attempted.

   Extension overlays, Workspace side panels and a window too narrow for the toolbar all move
   or intercept the targets you measured from a screenshot. Ask the user to close them rather
   than working around them; it costs them seconds and removes a whole class of misclick.

## Verification and recovery

**Comment count as a tripwire.** The per-tab badge in the Document tabs sidebar includes
suggestions. In the incident it went 32 → 36 when four stray suggestions landed and back to 32
after undo. Note it before starting; it tells you something happened even when you cannot read
the text.

**If you break something:**

1. `cmd+z`, repeated. Google Docs undo is per-user, so it unwinds your actions, not theirs.
2. Verify with a **probe search** for a string that can only exist if the damage survived —
   e.g. the concatenation of what was wrongly typed (`711587` → expect `0 of 0`).
3. Check the comment count is back to its starting value.
4. **Tell the user immediately**, before continuing. Say what landed, what you reverted, and
   what they should check themselves (**File → Version history**, and any suggestions bearing
   the relevant timestamp).
5. Do not quietly continue the task. The user decides whether to proceed.

## When not to do this at all

Driving a canvas editor blind is a poor trade for a small number of mechanical substitutions.
There are two alternatives, and they are good for different things. Offer one of them honestly
rather than defaulting to the browser because it was asked for.

**A find → replace table**, when the changes are agreed and the user will apply them:

> "I can give you an exact find → replace table in document order, scoped to the live tab.
> Five minutes with `cmd+shift+H`, and you see every change before it lands."

**Anchored comments in a downloaded `.docx`**, when the changes are *proposals* rather than
decisions — see `collaboration/docx-comment-injection`. Download the tab as `.docx`, write
`w:commentRangeStart` / `w:commentRangeEnd` markers around each sentence, upload to Drive and
open with Google Docs: every point arrives as a native sidebar comment anchored to its
sentence, with live Paperpile/EndNote citations intact. The live document is never touched, so
none of the hazards on this page apply. The cost is that it is a *separate copy* — comments
travel, edits do not.

Prefer one of those when:
- the changes are mostly mechanical (numbers, terminology) → table
- the changes need co-author agreement before they are applied → comments
- several co-authors are in the document → either
- the document is a manuscript near submission → either
- anchors could not be verified against the live text → fix that first, in both cases

Prefer driving the browser yourself when the user explicitly wants it, the document is quiet,
and each change still gets its own confirmation.

**Comments through `.docx`, edits in the live document.** That split resolves most of the
pressure that led to the incident at the top of this page.

## Transfers to other live documents

The specifics above are Google Docs, but the shape is general — HackMD, Notion, Office 365 and
any real-time editor share these properties:

- **No staging area.** Every change is immediately visible to everyone.
- **Prefer the reviewable channel**: suggestions, comments, branches, drafts — whatever the
  platform offers instead of direct mutation.
- **Focus is invisible state.** Any keystroke whose meaning depends on which control has focus
  is a hazard; confirm before committing text.
- **The undo scope is not obvious.** Know whether undo is per-user or global before relying on it.
- **Check who else is present** before writing.

## References

- Incident: VGP dual-curation manuscript, 2026-10-01 — see
  `~/.claude/projects/-Users-delphine-Analyses-Curation-Paper-figures/memory/feedback_google_doc_editing.md`
- Related skills: `collaboration/docx-comment-injection` (the offline channel for
  proposals), `collaboration/hackmd`, `analysis/scientific-publication`

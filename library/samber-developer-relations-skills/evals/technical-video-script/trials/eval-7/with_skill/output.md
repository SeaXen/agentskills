## Note on chapters

The skill's default for a sub-90s changelog clip is *no* chapter list (release clips usually don't clear the platform's 3-chapter minimum). You explicitly asked for chapter markers, so I split the single claim into three genuine demonstration segments — each ≥10s — instead of manufacturing arbitrary breaks. Still one change, one claim: the read-only expiring link.

Items I couldn't confirm from your message are flagged `[unconfirmed]` inline — fill those before recording, don't guess past them.

---

## Header

```
Title (working):   Kestrel Analytics 4.2: Share Saved Views with an Expiring Link
Promise:            For existing Kestrel Analytics users, this video shows sharing a
                     saved view via a read-only, auto-expiring link, working end to end.
Shape:               changelog / release clip
Audience:            existing user learning a new feature
Surface:             release post embed + product feed
Target runtime:      1:15          Estimated runtime: 1:15
Recorder:            [unconfirmed — who shoots this and on which machine]
Speaking rate:       [unconfirmed — not yet measured. Budget below assumes 150 wpm.
                     Time a 200-word read on the actual recorder before locking the cut plan.]
Companion:           none named — the release post is the landing point for this clip
Off-limits:          real customer/tenant names, internal hostnames, pricing, any
                     account not seeded specifically for this recording
```

## Beat table

| #   | Visual                                                       | On-screen action                                                       | Narration                                                                                                                                    | Starting state                                                                          | Est. s | Core/cut |
| --- | ------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------ | -------- |
| **Segment 1: Share a saved view (00:00)** |
| 1   | Kestrel Analytics dashboard, a saved view already open        | Cursor moves to toolbar, clicks the new Share icon `[unconfirmed — confirm exact label/icon]` | "Saved views in Kestrel Analytics can now be shared as a read-only link." `[verbatim]`                                                       | Demo account, seeded data, saved view `[unconfirmed name — e.g. "Weekly Signups"]` open, browser clean, zoomed to 125% | 7      | core     |
| 2   | Share panel/modal opens                                       | Modal shows a Read-only toggle (locked on) and an expiry field           | "Open Share on any saved view, and Kestrel Analytics generates a link that's locked to read-only — nobody using it can edit filters, add metrics, or touch your data." | Share modal open, expiry field not yet set                                                 | 13     | core     |
| **Segment 2: What the recipient sees (00:20)** |
| 3   | New incognito window, the copied link pasted and loaded        | Page renders; edit, save and duplicate controls are absent or greyed out | "The recipient opens the link and sees the same chart, with every editing control removed. They can look. They can't change it."             | Link already copied; second browser profile or incognito window ready, no login prompt configured | 15     | core     |
| **Segment 3: Set the link to expire (00:35)** |
| 4   | Back to the original tab, expiry field                        | Click the expiry field, select a preset `[unconfirmed — actual expiry presets/max duration not given]` | "Before you send it, set an expiry. Kestrel Analytics offers presets up to `[X]` days — after that, the link stops working, automatically."  | Share modal reopened, expiry field closed                                                  | 15     | core     |
| 5   | Calendar/time-lapse graphic, then the same link reopened past expiry | Expired-link state shown on screen `[unconfirmed — needs a staged screenshot or a backend-forced expiry; real elapsed time can't be shot live]` | "Once it expires, the link just stops working — no lingering access, nothing to manually revoke."                                            | Pre-staged "expired" screenshot or test account with an already-elapsed link                | 15     | cuttable |
| 6   | Back to the dashboard, saved views list                       | Zoom across the Share icon on two or three views                        | "It's live now in every saved view. Update to 4.2 and share what you built — safely." `[verbatim]`                                           | Dashboard view list, cursor idle                                                           | 10     | core     |

Rules this table follows: no beat depends on a prior beat's live output — beat 5's "expired" state is staged, not waited-out live, so it's re-shootable on its own.

## Chapters

```
00:00 Share a saved view
00:20 What the recipient sees
00:35 Set the link to expire
```

All three clear the platform's 10-second floor (20s / 15s / 40s), first entry is `00:00`, three entries, ascending. `[unconfirmed — re-verify the platform's current chapter rules before publish; this skill's reference wasn't re-checked live]`

## Cut plan

```
If long by ~12s:  drop beat 5 (staged expiry screenshot). Fold one clause into
                   beat 4: "...after that, the link simply stops working."
Never cut:         beat 1 (opening claim), beat 2 (read-only mechanic), beat 6 (CTA)
```

## Runtime

Narration word count: 113 words (12 + 28 + 20 + 22 + 15 + 16 across beats 1–6).
At the assumed 150 wpm: ≈45s narration + 30s budgeted dead time (modal opens, tab switch, expiry-lapse graphic, CTA hold) = **1:15**, matching the target.
Replace 150 wpm with the recorder's measured rate before treating this as final — if the real rate lands lower, cut beat 5 first per the cut plan above.

## Recording brief

**Starting states**

| Beat | Enter this state with | Verified |
| ---- | ---------------------- | -------- |
| 1    | Log into demo/seeded account, open saved view `[unconfirmed name]`, clear browser chrome, zoom 125% | no |
| 3    | Copy share link from beat 2's take, open in a fresh incognito window with no saved login | no |
| 5    | Load a pre-staged "link expired" screenshot, or force-expire a test link server-side `[unconfirmed — confirm which method Kestrel Analytics supports]` | no |

**Machine hygiene:** notifications off at OS level; recording browser profile with no personal bookmarks/autofill; no real customer names or tenant IDs anywhere in the seeded account; terminal N/A (UI-only clip); window sized 16:9; text/UI legible at phone-sized playback.

**Off-limits, concrete:** no real customer names, no real tenant IDs, no pricing page in frame, no colleague names in any shared account list, no unreleased 4.2 features beyond this one.

**Caption/description pack**
- Description opening (2 sentences): "Saved views in Kestrel Analytics can now be shared as a read-only link. Set an expiry, and the link stops working on its own — no manual revoke needed."
- Links to include: release post URL, in-app changelog entry.
- Caption fix list: "Kestrel Analytics," "read-only," "4.2" — check auto-captions render these correctly.
- Claims to re-verify before publish: exact expiry preset options and max duration (beat 4), release date (v4.2 ships "the 3rd" — confirm month before the clip goes live, since it can't publish ahead of the embargo).

## Pass threshold — status

1. Promise stated in one sentence, delivered inside 30s (beats 1–2 land it by 0:20) — **pass**
2. Every beat has a re-enterable starting state — **pass**, contingent on resolving the beat 5 `[unconfirmed]` staging method
3. Audio-only read teaches the thing, zero deictic sentences — **pass**
4. Runtime estimate includes dead time and lands on target — **pass**, pending real speaking-rate measurement
5. Every segment has a chapter title clearing the platform minimum — **pass**
6. Every beat marked core/cuttable; cutting all cuttable beats still delivers the promise — **pass** (cutting beat 5 leaves the read-only + expiry claims intact)
7. Every claim is reproducible on the recording machine — **blocked** on the three `[unconfirmed]` items above (exact share-icon label, expiry presets, expiry-staging method)

Next: confirm the three `[unconfirmed]` UI/product details, then this is shootable as-is.
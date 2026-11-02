Two blockers before I can produce the actual 9-language deliverable — flagging them now rather than guessing:

**1. I don't have marketing's English text.** You described it (3,180 characters, offline map packs, elevation profile, GPS drift fix) but didn't paste it, and I'm not searching for it — nothing in this repo relates to Trailmark, and skill-wip/ is off-limits per your instructions anyway. I won't invent replacement copy and pass it off as a translation of marketing's approved text — that's how a fabricated feature claim ends up live in a store listing in 9 languages. Paste the actual text and I'll translate it verbatim-in-meaning.

**2. The length doesn't fit both stores as-is.** This is the deliverable-blocking finding, independent of content:

| Store | Field | Hard limit |
|---|---|---|
| Apple App Store Connect | `whatsNew` (per locale) | 4,000 characters |
| Google Play Developer API | `releaseNotes[].text` (per language, on the track release) | **500 characters** |

3,180 characters fits Apple fine. It's **6.4× over** Google Play's limit. Google Play will reject the `edits.tracks.update` call outright if any `releaseNotes.text` exceeds 500 chars — this isn't a soft truncation, it's a validation error. German and Finnish-style compounding languages also typically run 20–30% *longer* than English, so a translation of an already-oversized EN text makes Play's overage worse, not better.

So this can't be "translate once, ship to both stores." It has to be:
- **App Store version**: full localized text (up to 4,000 chars), 9 languages.
- **Play version**: a condensed, separately-written ≤500-char release note per language (not a mechanical truncation of the long version — needs its own tight pass per language so it doesn't just get cut off mid-sentence).

**Before I can produce either, I need from you:**

1. The actual English "What's New" text (paste it, or point me at the file outside skill-wip/).
2. Portuguese: **pt-PT, pt-BR, or both?** These diverge meaningfully (vocabulary, formality, "ecrã" vs "tela") — App Store and Play both support both as distinct locales.
3. Dutch: nl-NL only, or nl-BE too?
4. Should I write the condensed Play version myself (I'll flag it for your review before anything's uploaded), or do you want to approve a condensed *English* version first, then I translate that into 9 languages?
5. For the Play API upload: confirm you want me to actually call `edits.insert` → `edits.tracks.update` → `edits.commit`, and which track (production / beta / etc.) and package name. I won't push to a live store listing without that confirmed explicitly, since it's visible to real users and not something to guess into.

Send the source text and answers to 2–5, and I'll turn around all 9 localized App Store entries plus 9 condensed Play release notes in one pass, ready to review before anything ships.
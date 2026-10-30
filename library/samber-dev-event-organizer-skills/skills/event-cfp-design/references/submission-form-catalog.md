# Submission form catalog

Field-by-field guidance for the CFP form. Sources: swyx's "CFP Advice", PyCon US's live CFP page, and the published feature sets of CFP platforms.

## Core fields (the standard rung)

- **Title** - the field the reviewer reads first and weighs most; swyx calls it "twice as important as your abstract." Give it its own label and space; never bury it as the first line of the abstract.
- **Abstract** - one paragraph, capped near 100 words (swyx's recommendation). A short cap is a design choice: it forces the pitch, keeps the review pool comparable, and stops the abstract from absorbing the outline and the bio.
- **Context / "why me" field** - a separate, optional field for why this speaker is the right presenter for this topic. Swyx emphasizes this field ("USE IT!!!") because most templates conflate it with the abstract. The split lets a committee score topic quality and speaker fit as two things.
- **Format pick** - one choice from exactly the session formats the chosen structure offers. Each format gets its own submission type where requirements differ.
- **Intended audience level** - PyCon US offers three tiers: "Just starting out / Some experience / Advanced experience." Three tiers is enough; finer scales invite false precision.
- **Speaker bio** - short: what the speaker does and is interested in (per swyx).
- **Photo** - recommended for consistency across submissions to the same event (per swyx). Optional at submission time; required only on acceptance.
- **Prior-talk links** - optional links to previous presentations or materials. The cheapest speaker-fit evidence a form can collect.

## Extended fields (the extended rung)

- **Track/category selection** - including edition-specific theme tracks where the program has them (PyCon US adds per-edition themes such as security or AI tracks).
- **Outline** - a structured outline field, separate from the abstract (PyCon US collects title, description, and outline as three fields).
- **Travel-grant request checkbox** - folded directly into the submission form rather than run as a separate process (per PyCon US). Pair it with the grant-policy language in the call.
- **Consents** - recording permission, photo release, code-of-conduct acknowledgment. Collect as checkboxes at submission; chasing consents after acceptance is a known time sink.
- **Per-format conditional fields** - fields that appear only for the format they concern: workshop prerequisites and capacity, hands-on setup requirements, poster dimensions. Conditional display is a shipped platform capability, so a long form need not look long to a talk submitter.

## The format menu belongs in the call

PyCon US's call offers four submission types: Talks, Tutorials, Charlas (Spanish-language talks), and Posters. Two lessons transfer:

- A call is not obliged to offer a single "talk" slot when the structure has more formats.
- A non-English track can be a stated, structural inclusion mechanism rather than a diversity sentence in the preamble.

## Submission cap

PyCon US: "a limit of three proposal submissions per person." A small cap keeps review load proportional to the submitter pool and discourages shotgun submissions; state it in the call rather than enforcing it silently.

## Tooling capability checklist

Per the tool-independence rule, design against capabilities, then pick whichever platform ships them. Capabilities the designs in this skill assume:

- Configurable submission fields (text, files, links, consents) with conditional logic.
- Scheduled automatic open and close - plus an escape hatch (one platform ships a "secret link for speakers that can submit after the deadline").
- A choice of review modes (comparison, star rating, yes/no) and separate evaluation plans per track or format.
- An optional anonymous-review mode.
- Speaker messaging: accept/decline flows with optional individual feedback on declines, post-acceptance forms for materials and travel data, and group mailings - one platform also ships pre-decision back-and-forth messaging between organizers and submitters.

Integration note (examples, not endorsements): Sessionize and PaperCall are commercial platforms covering the checklist above at different depths. Pretalx is the open-source option the DevOpsDays community runs for members and the platform PyCon US submits through. Any tool covering the checklist fits.

## Positive and negative example

**Negative - the one-box form:**

> Talk title: ______
> Tell us about your talk (unlimited): ______________________
> Email: ______

Everything - pitch, outline, credentials, audience level - lands in one unbounded box. Reviewers cannot compare submissions, cannot score topic and speaker separately, and blind review is impossible because identity is woven through the only field there is.

**Positive - the standard-rung form:**

> Title (one line)
> Abstract (max 100 words - the pitch, not the outline)
> Why you? (optional - why you're the right person for this topic)
> Format: [ ] 30-min talk [ ] 5-min ignite [ ] Half-day workshop
> Audience level: [ ] Just starting out [ ] Some experience [ ] Advanced experience
> Bio (2-3 sentences) - Links to prior talks (optional)

Each review question has its own field, the caps keep the pool comparable, and the identity-bearing fields (bio, links) are separable for a blind first phase.

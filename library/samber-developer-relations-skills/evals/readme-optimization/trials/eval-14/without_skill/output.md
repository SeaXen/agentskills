Here's the actual plan — not a checklist regurgitation, a week budget.

## The core call

`dtx`'s entire pitch is "look at this output." Every other GitHub-presence lever (badges, profile README, funding.yml, GitHub Actions automation, a logo) is in service of getting eyeballs onto that one recording faster. If the week goes to general README hygiene instead of the recording, you've optimized the frame and left the picture blank. Spend against this ordering, stop when the week runs out — everything below the line gets cut, not deferred.

## Day-by-day

**Day 1 — the hero capture.** This is the actual deliverable of the week; everything else is packaging.
- Build a realistic-but-readable Terraform plan pair: not a toy 2-resource diff, not a 40-resource wall either. Aim for ~6-10 resources with a mix — one addition, one destroy, one in-place update, one force-replace. That mix is what sells "colour-codes the drift" — a diff with only additions doesn't demonstrate anything a human can't already picture.
- Record with **vhs** (charmbracelet) or **asciinema** + **agg** to convert to GIF — vhs is the better pick since the `.tape` file is scriptable and reproducible, so you can re-record in 30 seconds when you tweak colours or copy later in the week.
- Target terminal width ~100 cols, dark theme (matches how most devs actually run a terminal), font large enough to read on a phone-width GitHub preview.
- Output two artifacts from the same session: an animated GIF (README hero) and one static PNG frame at the moment of peak colour-density (social preview + docs screenshot).

**Day 2 — README rebuild around the capture.** Plain-text README with no images is the single biggest thing actively working against this project. Structure:
```
# dtx

One sentence: diffs two Terraform plans and colour-codes the drift.

[hero GIF, full width, right under the one-liner — before any prose]

## Install
brew install ambervale/tap/dtx
# or: go install github.com/ambervale/dtx@latest

## Usage
dtx plan-a.json plan-b.json
```
Everything else (flags, config, CI integration, comparison to `terraform show -json | diff`) goes below the fold. A visitor should see the colourized diff before they've scrolled once — right now they see none of it, ever, because there's no image in the README at all.

**Day 3 — repo metadata (30 minutes of work, currently 100% missing).**
- **Description** (repo Settings, or `gh repo edit ambervale/dtx --description "..."`): one sentence, keyword-front-loaded — e.g. "Colour-coded diff for Terraform plans — see exactly what changed, added, or was destroyed." Avoid burying "Terraform" or "diff" past word 5; that's what search and link-preview truncation both key off.
- **Topics** (`gh repo edit ambervale/dtx --add-topic ...`): `terraform`, `terraform-plan`, `cli`, `devops`, `infrastructure-as-code`, `diff`, `drift-detection`, `terminal`, plus your implementation language (`golang`/`rust`). These are free discoverability — GitHub topic pages get organic traffic you're currently getting zero of.
- **Website field**: only fill this if something real exists to link (docs site, landing page). Don't fabricate a placeholder — an empty field reads as "early project," a dead link reads as "abandoned," which is worse.
- **Social preview** (Settings → General → Social preview, upload manually — no CLI for this): use the Day-1 static PNG, not a logo. When this repo gets linked in Slack/Discord/a tweet, the colourized diff *is* the pitch — a generic banner wastes that slot.

**Day 4 — second usage example + polish pass.** One more GIF or PNG showing a second scenario (e.g. a *clean* run — no drift, all green/neutral — since "what does it look like when nothing's wrong" is half the value prop for a tool people run in CI). Add 3 badges max: build status, latest release, license. Skip download counts, coverage, Discord — you have none of the traffic those badges are meant to signal yet, and an empty-looking badge row undercuts trust more than no badge row.

**Day 5 — submit for discovery.** Now that the README actually demonstrates the thing, this is worth doing:
- PR into `awesome-terraform` and one general `awesome-cli-apps`-style list — small effort, and reviewers on these lists judge almost entirely off the README you just built.
- Skip Product Hunt / HN for this specific week unless you're prepared to also handle the traffic and comments that follow — that's a separate, bigger commitment than "where does GitHub-presence effort go."

## Explicitly skip this week

Profile README, GitHub Sponsors/funding.yml, auto-tweet-on-release Actions, GitHub stats widgets, a custom logo/SVG wordmark. None of these move the needle for a tool nobody has seen work yet — they're retention/monetization plays for a project that already has traffic. A terminal tool doesn't need a logo; a monospace `# dtx` heading is more on-brand than an icon would be anyway.
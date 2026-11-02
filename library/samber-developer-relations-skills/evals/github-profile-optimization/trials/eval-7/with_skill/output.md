# Profile audit — halvard-nyqvist (personal)

Using `github-profile-optimization` (samber/developer-relations-skills). I couldn't run `scripts/profile-audit.py` or fetch the live page — network/API access wasn't granted this session — so this audit runs on the pasted README text plus your statement that pins are unset, per the skill's fallback path. Facts I could **not** verify: whether `banner.png` actually renders, whether `blog.nyqvist.dev` resolves, the bio/company/location fields, social links, follower count, and what repos the "Popular repositories" fallback currently surfaces. Treat those as open, not as passing.

```
PROFILE AUDIT — halvard-nyqvist (personal)
Goal on record: not yet established (interview Q3 unanswered)

Blocking
  B1 renders            PASS (unverified) — taking your word this is the live README; confirm banner.png
                         actually displays (relative path, unchecked) and that the repo is named
                         exactly "halvard-nyqvist", public, with README.md at root
  B2 identifiable        PASS (weak) — a sentence exists ("Software engineer. I love building things
                         and learning new technologies.") but names no domain, stack, or audience
  B3 claims true         PASS (risky) — nothing named, so nothing disprovable, but "🔭 I'm currently
                         working on something exciting" and "🌱 Learning Rust" are undated — exactly
                         the stale-phrase pattern this skill's own audit script flags. Could be from
                         2021 or from yesterday; a reader can't tell and neither can you without checking
  B4 next step           PASS — blog link present, email given

Scored  5/16
  S1 positioning         1/2  "Software engineer. I love building things and learning new
                               technologies." — vague but present. Any GitHub account could paste
                               this sentence unchanged; it fails the skill's own test for that reason
  S2 pins                0/2  pins unset by your own account — fallback is GitHub's auto-selected
                               "Popular repositories," which you don't control and which frequently
                               surfaces something abandoned
  S3 pin descriptions     0/2  cascades from S2 — nothing is pinned, so nothing is editorially
                               described; whatever the fallback shows wasn't chosen or labeled by you
  S4 reading order        0/2  banner image sits directly under the heading with zero prose above it,
                               violating "one sentence of prose above every image." There's also no
                               proof segment at all — no project, no example of work, nothing to verify
  S5 decoration budget    2/2  one image, no widgets, nothing stale — clears the mechanical bar
  S6 accessibility        1/2  alt="banner" is present but non-descriptive — a screen-reader user
                               learns nothing about what the image shows. Otherwise readable in a
                               plain markdown viewer, no meaning in colour alone
  S7 freshness            0/2  no owner named, no review trigger, and the two "right now" lines carry
                               no date — a visitor has no way to judge whether this page is current
  S8 route to destination 1/2  blog link is clear but untracked (no UTM/query param)

Cold reader   2/4 — reader can answer "what do they do" (thin) and "what do I do next" (blog/email),
              but not "which project should I look at first" (nothing named, pins unset) or
              "is this active" (no dated evidence either way)
```

## Your actual question: is it good enough to leave alone?

**No — mainly the pins.** Leaving them unset isn't a neutral choice; per platform mechanics, GitHub silently falls back to an auto-ranked "Popular repositories" list you don't control, which commonly surfaces something abandoned or a fork. That's the single biggest miss here, independent of anything else on the page — it costs nothing to fix and it's the difference between routing a visitor deliberately and routing them by accident.

The README itself also isn't "leave it alone" material: 5/16 against this skill's own 13/16 ship bar, and the cold-reader test fails on the two questions that matter most (what to look at, whether it's active).

## Fix order (return per hour spent — leads on efficiency; effort and value orderings shown for context)

- efficiency, do first: verify claims/render → pins → positioning → page rebuild
- effort, least first: verify claims/render → pins → positioning → page rebuild
- value, most first: positioning → pins → page rebuild → verify claims/render

They converge unusually well here because the whole page is ~30 words — there's no expensive step to defer.

1. **Confirm the render risk and date-or-delete the vague lines** (minutes). Check `banner.png` actually loads. Either put a date on "currently working on X" and "learning Rust," or delete both — undated "right now" claims are the thing that goes stale without anyone noticing.
2. **Set six pins deliberately, flagship first** (minutes, zero cost). This alone fixes cold-reader Q2 and recovers S2+S3.
3. **Write one real positioning sentence.** Gated on you, not on me — see questions below.
4. **Reorder the page: one sentence of prose before the banner**, or drop the banner if it's not earning its place. Bundle with step 3, same edit pass.
5. **Name yourself as owner and pick a review trigger** (next role change, next project ship, next talk) — cheap, and it's the thing that stops this drifting stale again like it may already have.

I'm not drafting positioning-sentence candidates yet — the skill gates that on knowing the audience and outcome first, and a generic sentence built from "software engineer, likes Rust" would just be a different version of the same problem. Three quick answers unlock that step:

1. What do you actually build — pick one thing a stranger could picture, not a job title.
2. Who's the one outcome this page should produce: project adoption, contributors, inbound work, speaking invites, or job leads?
3. Is most of your real work public, or does it happen at a job/private repos? (Decides whether the private-contribution toggle belongs above the pins fix.)
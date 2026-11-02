# quillsync label redesign — final list

## Reading the numbers back first

47 labels for 2 maintainers with ~4 hours/week combined (best case) is already past what either of you can keep straight from memory, and a 6-family, area-split taxonomy (Kubernetes-scale) needs an owner and a written enforcement doc neither of you has time to run. That points at the **small-team** tier, not bigger — fewer axes, no `area/*` split, no automation layer yet.

One honest flag before the list: 35 new issues/week against ~4 hours/week of triage capacity is a capacity problem, not a labels problem — relabeling won't shrink 912 open issues on its own. This redesign fixes "nobody agrees what a label means," not "too many issues for two people." Worth a separate pass on intake (chooser routing / cutting what reaches the tracker at all) when you have another hour.

## The new label set (target state)

One label per axis per issue, max. Colors are grouped by axis, not by individual label — swap hex values freely, keep the grouping.

**State — always applied, `#BFD4F2`**

| Label | Definition |
|---|---|
| `needs-triage` | Nobody has looked at this yet |
| `needs-info` | Waiting on the reporter for details |
| `accepted` | Confirmed real, will be worked |
| `needs-owner` | Accepted, but nobody has picked it up |
| `blocked` | Waiting on something external (a dependency, another issue, an upstream app's API) |

**Type — always applied, `#D4C5F9`**

| Label | Definition |
|---|---|
| `type/bug` | Confirmed defect in existing sync behavior |
| `type/feature` | New capability or new sync target being requested |
| `type/docs` | Documentation gap or fix |
| `type/support` | Usage question, not a defect or a request |

**Priority — applied once triaged, warm family (`#B60205` → `#FBCA04`)**

| Label | Definition |
|---|---|
| `priority/now` | Drop other work — data loss, crash, broken sync for many users |
| `priority/later` | Real, not urgent |

Two values only — a third tier just starts arguments at this team size.

**Contributor-facing — optional, add only if you'll actually honor it, `#0E8A16`**

| Label | Definition |
|---|---|
| `help wanted` | Maintainers want outside help on this |
| `good first issue` | Scoped, low-risk, enough context for a first-time contributor |

Skip this pair entirely for now if neither of you has spare time to shepherd a newcomer's PR — an unanswered `good first issue` is worse than not having the label.

**Total: 11 required + 2 optional = 13 labels**, down from 47.

Not included, deliberately: `wontfix` / `duplicate` / `invalid`. GitHub's native "close as not planned / duplicate" reason on the close action already carries that information — a label duplicating it is one more thing to keep in sync by hand.

## Disposition of the old 47

**The three bug labels** — merge into `type/bug`, keep history via rename rather than delete-and-recreate:

```bash
# whichever of the three has the most issues, rename it (issues keep the label for free)
gh label edit "bug" --repo <owner>/quillsync --name "type/bug" --color D4C5F9 \
  --description "Confirmed defect in existing sync behavior"

# migrate the other two before deleting them
for n in $(gh issue list --repo <owner>/quillsync --label "Bug" --state all --json number -q '.[].number'); do
  gh issue edit $n --repo <owner>/quillsync --add-label "type/bug" --remove-label "Bug"
done
gh label delete "Bug" --repo <owner>/quillsync -y

for n in $(gh issue list --repo <owner>/quillsync --label "type: bug" --state all --json number -q '.[].number'); do
  gh issue edit $n --repo <owner>/quillsync --add-label "type/bug" --remove-label "type: bug"
done
gh label delete "type: bug" --repo <owner>/quillsync -y
```

**The 19 single-use labels** — default to delete; a label applied to exactly one issue over the project's life is a private note, not a taxonomy value. Exception: if any single one of them is clearly a real axis value that's just rare (e.g. a genuine one-off `priority/critical`-type case), rename it into the new vocabulary instead of deleting — don't delete-then-forget a label that was actually right, just rare.

**The remaining ~25 named labels** (I don't have their actual names — sort them yourselves in a couple minutes each with this rule):
- Names a kind of work → rename into `type/*`.
- Names urgency → rename into `priority/*`.
- Names what it's waiting on → rename into the state set above.
- Anything else (a connector name, a platform, a vague catch-all) → delete. If you later split ownership by connector (Obsidian, Notion, Apple Notes, etc.), add a proper `area/*` family then — don't half-build it tonight with nobody assigned to maintain it.

## Doing the migration tonight

1. Create the 11–13 new labels (name, color, description) first.
2. Run the bug-label merge above.
3. Sort and migrate the other 25 named labels with the rule above.
4. Delete the 19 singletons (reclassify the rare exception if you find one).
5. **In the same sitting**, update anything that references the old names: saved/filtered views, issue templates, any bot or Action config — a half-migrated label set is worse than the old mess, because now two vocabularies both look current.
6. Paste this table into a `LABELS.md` (or a section of `CONTRIBUTING.md`) in the repo — the definition needs to live somewhere other than the tracker's own tooltip, or the third contributor who shows up in six months reinvents `Bug` again.
7. Post one message in whatever channel you two use, once, saying the label set changed and pointing at `LABELS.md` — don't let it be a silent change only one of you remembers making.
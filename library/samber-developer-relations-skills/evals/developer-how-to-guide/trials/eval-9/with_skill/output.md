## Open questions

No one could answer the interview, so these are the answers I assumed. Each point where your brief and the skill disagree is marked.

1. **Title.** Your titles are gerunds ("Creating flags"), so I matched them. I did not use the bare noun "Percentage rollouts", because the skill bans bare nouns. Gerunds in a new set would be a set-wide change to raise with the owner. I did not retitle one page out of line.
2. **Role.** I wrote "Admin" as you asked. The skill says to name the narrowest role that works. Is there a role below Admin that can edit production targeting? If so, name it.
3. **Option table.** I cut it and linked to reference instead. The skill puts option tables in reference, not mid-procedure. I also have no verified facts about Tidewell's seed, schedule or kill-switch semantics, and I will not invent them. To keep a table anyway, supply the facts and put it in an appendix below Next steps.
4. **Two paragraphs on consistent hashing.** I cut them and linked an explanation page. This is explanation, not action. I do not know Tidewell's algorithm. The page keeps one line only where the reader must choose.
5. **Eight "Learn more" links.** I kept the heading you asked for but wrote three links, the template default. The five extra links were not needed for the task, and I cannot confirm pages exist for them. Tell me your set's real limit.
6. **Competence floor.** The reader has an existing flag and dashboard access. This is not a quickstart.
7. **Cold run.** Nobody has run this yet, so it carries `UNVERIFIED` markers and does not ship. The run list is at the end.
8. **Variants.** Cloud and self-hosted use one recommended path. I assumed the dashboard steps are the same on both and marked that as unverified.

## The page

````markdown
---
title: Rolling out a flag to a percentage of users
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Rolling out a flag to a percentage of users

Use this page when you want a flag on for a slice of your production users while everyone else keeps the current behavior. The change takes about two minutes and affects live users.

## Before you begin

- You need to be an Admin on the project.
  UNVERIFIED: the check command or screen that shows your role, and whether a narrower role can edit production targeting.
- You have a flag, and it is turned on in the production environment. If not, see [Creating flags](UNVERIFIED-LINK: Creating flags).
- You are on Tidewell cloud, or on self-hosted version UNVERIFIED or later. Check your version at UNVERIFIED.
- This task changes what production users see. Try it first on a non-production environment. See [Managing environments](UNVERIFIED-LINK: Managing environments).

## Steps

1. In the dashboard, open the flag you want to roll out and select the production environment.

   UNVERIFIED: exact navigation path and UI labels.

2. Set the rollout percentage to a small slice, such as 5%.

   UNVERIFIED: field label, accepted range, and whether the unit is a percent or a fraction.

   Start small so that a bad result reaches few users. You raise the number later by repeating steps 2 and 3.

3. Save the change.

   > **Warning:** After you save, the percentage applies to live production users. UNVERIFIED: whether the change is immediate or delayed, and whether each SDK picks it up at once. To undo it, see [Roll back](#roll-back).

   Safe to re-run.

## Verify the result

Confirm that the flag serves the new value to roughly the percentage you set. Use a read path other than the save screen.

UNVERIFIED: the independent read (a dashboard evaluation count, an SDK debug log, or an API read), its command or screen, and its expected output. If Tidewell has no such read, say on this page what the check cannot prove.

If the flag still serves the old value to everyone, see [Troubleshooting flags](UNVERIFIED-LINK: Troubleshooting flags).

## Roll back

Roll back if your error rate rises or users report wrong behavior after the change.

Open the flag in the production environment, set the percentage to 0, and save. For an immediate stop, use the kill switch instead. UNVERIFIED: where the kill switch is and what it does to the stored percentage.

## Learn more

- [Rollout options reference](UNVERIFIED-LINK: Rollout options reference): percentage, bucketing key, seed, schedule and kill switch.
- [How bucketing works](UNVERIFIED-LINK: How bucketing works): why the same user keeps the same result.
- [Troubleshooting flags](UNVERIFIED-LINK: Troubleshooting flags)
````

## Hand-over

**Pages to write** (all `UNVERIFIED-LINK` targets):
- Rollout options reference. Goal: a reader looks up any option without a procedure.
- How bucketing works (explanation). This is where your two consistent-hashing paragraphs belong.
- Troubleshooting flags.
- Creating flags and Managing environments should already exist in your set, so check their URLs.

**Variants dropped:** none. The page assumes cloud and self-hosted dashboards are identical. If they differ in steps or verification, the skill says to split them into separate pages sharing a title stem.

**Product gaps to confirm:** an independent read path for verification, and whether saves are immediate.

**Run list**
```
Environment:   a disposable Tidewell cloud project and a self-hosted instance, each with one flag, seeded to the floor
Runner:        someone with the Admin role who has not seen this draft
Capture:       every UNVERIFIED block, by step number, with the real UI labels and output
Variants:      cloud and self-hosted, one run each
Re-run:        step 3 on the finished state
Roll back:     set to 0, and the kill switch, once each
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target
Product gaps:  independent read path; save propagation delay
```

**Not run:** I did not run any command or touch Tidewell. The page cannot ship until the markers are cleared. I also did not run the humanizer pass or load the caveman and ADHD modes from your CLAUDE.md. The page's prose is plain and the markers are the point of the hand-over.
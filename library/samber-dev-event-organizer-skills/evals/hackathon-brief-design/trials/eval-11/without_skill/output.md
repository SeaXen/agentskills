# Answer: yes, send tonight, but fix the public rules in the same email

⚠️ The reuse gap is not your biggest problem. Your brief copies the public-repo and public-video rules from the usual template, and your teams are working on patient records. Those rules probably tell teams to publish. Teams started yesterday morning, so some may already have a public repo or a screen recording.

## Before you send (about 15 min)

1. **Decide the reuse policy.** I recommend *allowed, but declared*. A ban would invalidate a day of work already done. Declaring keeps judging fair and keeps your risk visible.
2. **Check what already exists.** Ask your GitHub admin to list repos created since yesterday morning and flag any that are public. Check whether anyone has posted a recording or demo link.
3. **Fix the template rules in the same email.** Repos private, videos internal, no data in anything shared outside the event. Do not send a reuse-only email and leave the public rules in place.
4. **Have security or privacy sign off on the wording.** I don't know your compliance obligations. De-identified data can still be re-identifiable, so they should confirm the data rules.

## Draft email

**Subject:** Hackathon brief update: reusing existing code, and where your work lives

Hi all,

We are making two updates to the brief. Please read both tonight.

**1. Reusing existing repos and code**

Using code you had before the hackathon is allowed, with these conditions:

- Declare it. Add a `PREEXISTING.md` to your team repo listing each reused repo, library or component, who owns it, and its license. Deadline: [DATE/TIME].
- Judging looks at what you build during the hackathon. Pre-existing code is not scored as new work.
- Do not point a pre-existing repo at hackathon data. Copy the code you need into your team's private repo in [ORG].
- Open-source libraries and internal shared packages are fine. Code from a previous employer or a personal project needs a quick check with [CONTACT] first.
- Teams that already reused code: you don't need to rebuild anything. Just declare it by the deadline above.

**2. Correction: repositories and videos**

The earlier brief carried over rules from our public events. They do **not** apply here, because you are working with patient-derived data.

- All repos must be private and inside [ORG]. If you created a repo anywhere else, including a public one, move it today and tell [CONTACT].
- Demo videos and screenshots stay internal. Share them only through [INTERNAL CHANNEL]. No public posting, no personal accounts.
- No record-level data in code, commits, notebooks, slides or recordings. Use aggregates or synthetic examples for demos.
- If you think something sensitive has left the approved environment, message [CONTACT] right away. Reporting early is the right call, and no one will be penalized for it.

Questions: [CONTACT / CHANNEL].

Thanks,
[NAME]

## After sending

- ⏳ Follow up tomorrow morning with the repo audit results. Ask directly any team that has a public repo or a shared video.
- ℹ️ Post the same text in the hackathon channel, because email alone gets missed.
- ✅ Fix the brief itself so later readers see the corrected rules, and note the update date at the top.

If you'd rather ban reuse, tell me. I'll rewrite section 1, but you will need a plan for teams that already used old code.
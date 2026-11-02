**Next action:** don't accept yet. Reply to the fintech first (draft below), and cut the five small gems this week (about 1 hour). Your two assumptions need fixing before the plan holds.

## Where your assumptions break

1. **$600/month does not justify 15 hours.**
   - At 15h/week (about 65h/month) it pays about $9/hour.
   - At 4h/week (about 17h/month) it pays about $35/hour.
   - The money only makes sense if the hours drop.
   - Accepting it "to justify the hours" backwards-justifies the hours you want to cut.
2. **Splitting 4 hours evenly across seven gems is the wrong plan.**
   - That gives about 34 minutes per gem.
   - hearthstone-csv gets the same time as a gem with a few hundred downloads.
   - hearthstone-csv has about 3M downloads a month, so it is the one that carries supply-chain and security risk.
3. **"To keep it going" is vague.**
   - Without written terms, the fintech may expect priority fixes or roadmap say.
   - Write the terms down before you take the money.

## Plan

### 1. Budget: 4h/week, about 17h/month

| Gem | Hours/week | Work |
|---|---|---|
| hearthstone-csv | 2.0 | Security fixes, triage, compatibility with new Ruby and Rails versions |
| quillbind | 1.0 | Same, with a lighter bar |
| Five small gems | 0.25 total | Batched into one 1h session per month |
| Buffer | 0.75 | Sponsor and security email, releases, co-maintainer onboarding |

Set a "no work outside the budget" rule. A bad week borrows from the buffer, never from the next week.

### 2. Cut the five small gems (this week, about 1h)

Pick one of these per gem:

1. **Hand off:** Give the gem to a volunteer, or to a maintainer who already uses it.
2. **Archive:** Mark it unmaintained in the README and gemspec, and archive the repo.
3. **Keep it frozen:** Make one last compatibility release, then do no feature work.

Don't yank released versions. A few hundred downloads a month still means installs that break. Once they're archived, those five stop taking your time.

### 3. Reply to the fintech (this week, about 30 minutes)

- Say yes in principle, with a written one-page scope.
- Money buys three things: a named security contact with a response target, upgrade-compatibility checks, and acknowledgement as a sponsor.
- Money does not buy roadmap control, merged PRs, or guaranteed outcomes.
- Ask for an annual commitment, an invoice route, and a named contact at the company.
- Counter on price. They run it in production, so $600/month is the floor. Try $1,500–2,000/month for a retainer shape with a response target. This is a guess about what they'd pay, not a market figure, so treat it as an opening ask.
- Add a "pause or stop" clause: you can end the arrangement with 60 days' notice.

Draft:

> Thanks, glad it helps you. I'd like to formalise this. Sponsorship covers: security-report handling with a defined response window, compatibility releases for new Ruby/Rails versions, and sponsor acknowledgement. It does not cover roadmap decisions or merging specific changes. I'm reducing my time on this project, so this funds sustained minimal maintenance, not new work. Annual terms, invoiced. Can we discuss amount and scope?

### 4. Reduce the bus factor on hearthstone-csv (next 4–8 weeks)

- With 3M downloads a month and Rails gems depending on it, you are a single point of failure.
- Ask the maintainers of the dependent Rails gems whether one of them will co-maintain.
- Give the co-maintainer commit and release rights. Turn on MFA and trusted publishing on RubyGems.
- Add a `SECURITY.md` with a reporting address.
- This is the real route to 4 hours. Money does not reduce your hours; a second maintainer does.

### 5. Public funding setup (about 1h, after the fintech reply)

- Add GitHub Sponsors and a `.github/FUNDING.yml` to the two real gems.
- Other dependents, such as the Rails gems' maintainers, may also pay. Don't count on it.

## Checkpoints

- **Day 7:** five small gems cut; fintech reply sent.
- **Day 30:** terms signed; co-maintainer identified.
- **Day 90:** your actual weekly hours are at or under 4. If not, drop quillbind's support level or hand it off.

## Questions I need answered

1. What takes the 15 hours today? If most of it is hearthstone-csv issue traffic, a co-maintainer helps most. If it is support questions, a triage policy helps most.
2. Do you have a legal entity for invoicing, or would the $600 come to you personally? That decides the payout route.
3. Is there someone who could co-maintain hearthstone-csv?

**Next:** send the fintech reply from step 3 (draft above), then tell me the answer to question 1.
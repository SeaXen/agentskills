# Saltmarsh Hack: 4 days, 5 hours, no lawyer

I'm not a lawyer, and I don't know your country. Where the rules vary, I've marked it **[check]**.

## The decision that shapes everything

Minors change the risk more than the 5,000 EUR does. Do these four things, and the rest is ordinary hackathon admin:

1. **Bring the school in as a partner.** They already hold parental consents, supervision rules and insurance for pupils.
2. **Collect less data.** Don't ask for what you don't need.
3. **Get written parental permission** for under-18s.
4. **Pay prizes to a guardian,** or give them in kind, for minors.

## Time budget (5h)

| # | Task | Time |
|---|------|------|
| 1 | Email the school contact, plus a call with the sponsors | 0:45 |
| 2 | Fix the data form | 0:30 |
| 3 | Write the rules page (the brief) | 1:30 |
| 4 | Parental permission form | 0:30 |
| 5 | Privacy notice | 0:30 |
| 6 | Sponsor one-pager (prizes, data, conduct) | 0:30 |
| 7 | Code of conduct and a reporting contact | 0:20 |
| 8 | Final read-through, publish | 0:25 |

## Day 1: ask three parties (45 min)

**The school.** Ask one teacher or the head:
- Does the school have a standard parental authorisation for off-site or extracurricular events?
- Can the school distribute it, or co-sign the invitation?
- Will a teacher attend or supervise?
- Is the event on school premises?

**Each sponsor.** Ask:
- Who pays the prize, and when? Cash, vouchers or hardware?
- Does their legal or compliance team have a template for prize terms? They usually do, and they have a stake in getting it right. This is your free lawyer.
- Do they want participant data? The default answer is no.

**Decide now:**
- Is the event in person, online or hybrid?
- Is it a single day, or does it run overnight?
- **Recommendation:** make it daytime-only and in person, with a supervising adult. Overnight with minors multiplies safeguarding duties, so skip it in year 1.

## Day 2: the form (30 min)

Collecting names, emails and school from 16-year-olds is workable if you keep it minimal.

**Collect:**
- Full name
- Email
- Date of birth, or just "under 18? yes/no" **[check: you only need this to trigger the parental form]**
- School, optional. Make it required only if you need it for eligibility.
- A parent or guardian email, required if under 18

**Don't collect:**
- Phone numbers
- Home addresses (ask the winners only, at payout)
- Photos at signup
- Anything about health or diet, unless there's food. If there is, ask "allergies?" as free text and delete it after the event.

**Add to the form:**
- A checkbox linking to the privacy notice.
- A separate, unticked checkbox for "photos and video at the event".
- A separate, unticked checkbox for "share my name and email with sponsors". Default it to no.

**Age of digital consent [check].** In the EU it is set between 13 and 16 by country. 16-year-olds clear it everywhere in the EU. Parental sign-off is still needed for the prize and for attending, and the form above covers that.

## Day 2–3: the brief (rules page, 90 min)

Paste this skeleton and fill the brackets.

```
# Saltmarsh Hack [YEAR] — Rules

**When / where:** [date, hours, address]. Daytime only.
**Who can enter:** Anyone aged [14+/16+]. Under 18s need a signed
parental permission form by [deadline]. Teams of [1–4].
**Theme / challenge:** [one paragraph]
**What to submit:** [repo link + 2-minute demo or README] by [time].

## Judging
Judges: [names or roles]. Criteria, equal weight unless stated:
[Idea], [Working demo], [Technical quality], [Presentation].
Judges' decision is final. Decisions are based on skill, not chance.
Ties: [rule, e.g. sponsor judge casts the deciding vote].

## Prizes (total 5,000 EUR)
[1st: X, 2nd: Y, 3rd: Z, sponsor specials: ...]
Provided by [Sponsor A] and [Sponsor B].
Team prizes are split equally unless the team tells us otherwise
in writing before the awards.
Winners aged under 18: the prize is paid to a parent or guardian,
or given as [voucher/hardware]. We'll ask for details only after winners
are announced.
Prizes may be taxable for winners. [check] We can't give tax advice.
Prizes are not transferable. If a winner can't be reached within
[14] days, the prize passes to the next entry.

## Your work
You keep ownership of everything you build. By submitting, you let
Saltmarsh Hack show your project name, description and demo on our
website and social channels. Sponsors get no rights to your code.
Use of open-source libraries and AI tools is allowed [if you allow it];
you must disclose them in the README. Work started before the event
is not eligible.

## Eligibility exclusions
Organisers, judges and their immediate family can't win.

## Conduct
Be respectful. No harassment, discrimination or sharing of
others' personal data. Report concerns to [name, email, phone],
reachable during the event. Organisers may remove anyone who
breaks these rules, with no prize.

## Safety (under 18s)
At least [two] adult organisers are present at all times. [A teacher
from X school attends.] Parents or guardians can reach [contact]
during the event.

## Your data
See the privacy notice: [link]. Short version: we use your details
to run the hackathon and contact winners. Sponsors don't get them
unless you tick the box. We delete everything by [date + 6 months]
except winners' names, which we may keep publicly.

## Changes and cancellation
We may change the schedule or cancel for safety or force majeure.
If we cancel, [no obligation beyond refunding anything paid].
Questions: [email].
```

Three points to hold the line on:
- **Skill-based judging only.** This avoids lottery and gaming rules **[check]**. Don't add a random raffle.
- **Participants keep their IP.** Taking IP from teenagers creates the most trouble for the least benefit.
- **No sponsor data access by default.**

## Day 3: the other documents

**Parental permission form (30 min, half a page).** Include:
- The child's name and the event, date and place.
- Supervision arrangements.
- Consent to attend.
- Consent to the processing of the child's data.
- Optional consent to photos.
- The prize will be paid to or via the guardian.
- An emergency phone number for the parent.
- A signature line.
- Check first whether the school already has a template. If it does, use it.

**Privacy notice (30 min).** One page, plain language. It says who the controller is (name and email), what you collect, why, who sees it, how long you keep it, and the rights to access, delete and complain (name the regulator **[check]**). Add one line: "Organisers only; no sponsors unless you opt in." Free generators from your national data protection authority work, and so do their templates.

**Sponsor one-pager (30 min).** Get it signed or confirmed by email. It states:
- The amount, the date they pay, and the prize form.
- That participant data is not shared (unless the opt-in is ticked).
- That sponsors don't contact minors directly.
- Their role in judging, if any.
- That they accept the code of conduct.
- What happens if they back out. Hold the funds before announcing the prizes, if you can.

## Year 2

A bad year 1 is cheap to fix. Fix these then:
- Get a real lawyer's review, one hour, paid from the sponsor budget. It is cheap with templates already in place.
- Add a standing data deletion routine.
- Keep a template pack: rules, forms and sponsor terms, re-dated each year.
- Agree an annual calendar with the school.

## Don't bother

- A formal company or association now. A named person as organiser is fine for a first small event **[check]**.
- Insurance. Ask the venue and the school what their policies cover first.
- Customised terms and conditions. The skeleton above is enough.

## Do first, today

1. Send the school and sponsor emails (45 min).
2. Say which adult will supervise.
3. Reply to me with the school's answer, the venue and the date, and I'll turn the skeleton into the final page.
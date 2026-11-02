# What to do instead of Marketing's dinner

**Short answer:** keep the dinner but remove the funnel. Run it as a no-pitch thank-you for contributors and users. Give the cloud console its own opt-in slot, and make every follow-up opt-in.

## Why the proposal feels off

It tries to do three jobs in one room. Each job needs a different promise to the guest.

1. **Wrong audience for the demo.**
   - Contributors gave their time to an Apache-2 project. A cloud console demo at their dinner says "you're the audience for our product".
   - Many contributors don't use the managed cloud, and some may resent it. The console is the commercial layer on top of their work.
   - Data engineers do care about the console, but only if they asked for it.

2. **Badge scan breaks the invitation.**
   - You invited people to dinner, and the scan quietly turns them into leads.
   - Badge scans are normally consent at a sponsor booth. At a private dinner, nobody agreed to it.
   - PyCon's lead-retrieval and attendee-data terms are in the sponsor prospectus, which I haven't read. Check them. Confirm with legal if you have EU or UK guests, because marketing email generally needs explicit opt-in there.

3. **Enrolling everyone in the nurture sequence is the real damage.**
   - Contributors get trial-conversion emails from the project they help build. This is the fastest way to turn goodwill into unsubscribes.
   - It also hits people who are already customers, and people who work at competitors or at your customers' vendors.

4. **Recap with photos and quotes needs consent.**
   - Dinner talk is assumed to be semi-private.
   - Some contributors are pseudonymous, or can't be named publicly by their employer.
   - Published quotes from a "thank-you" dinner read as testimonials you collected.

**The principle:** a contributor event earns trust, and a lead event spends it. Keep them separate, or label the commercial part and make it optional.

## What to run

### 1. The dinner: a contributor and user table, no pitch

- **Purpose:** thank contributors and put them next to the people who run the database in production.
- **Guest mix (30 seats):**
  - About 18 contributors, chosen by contribution type, not commit count. Include docs, triage, reviewers, maintainers and a few recent first-time contributors.
  - About 8–10 data engineers who use Ferrovia. Source them from issue authors, community chat and customers, not only from the CRM.
  - Ferrovia staff: 3 at most, and mostly maintainers.
- **Invitation:** ask in the RSVP who is already attending PyCon. Don't fly anyone in for the dinner unless you decide to fund travel as a separate program.
- **Program (about 2 hours):**
  - A short welcome from a maintainer, not marketing.
  - One or two user lightning talks (5 minutes each) on running the database in production, including what went wrong.
  - A roadmap and RFC open mic. Ask what's blocking contributors and what users need.
  - Seat contributors and users alternately. Have maintainers collect issues and pain points at the table.
- **Check-in:** a name list and name tags. No badge scanning.

### 2. The console demo: separate and opt-in

Pick one of these:
- A 20-minute demo and Q&A at the booth, or a listed session that people choose to attend.
- An after-dinner "optional demo, 15 minutes, in the next room, leave or stay". It must be on the invite, so no one is surprised.

Marketing gets a real, engaged audience, which beats a captive one.

### 3. Data and follow-up: opt-in only

- **RSVP form:** include one unchecked box, "Email me about Ferrovia Cloud and events". Only checked boxes enter any nurture flow.
- **Contributors:** never auto-enroll them. Send a personal thank-you from a maintainer within a week. Include concrete next steps, such as open "good first" issues, a contributor-program path and a link to the roadmap thread.
- **Opted-in data engineers:** send one useful asset, such as a tuning guide, notebook or migration note, with a trial link on request. Don't send a drip sequence.
- **CRM overlap:** check the guest list against existing customers and open deals first. Don't send trial emails to customers.

### 4. Recap: consent-first

- **Photos:** use an "OK to be photographed" sticker. No sticker means no photo. Skip faces, or shoot hands, table and food.
- **Quotes:** send each quote to the person for written approval, with their name, handle or "a contributor" as they choose.
- **Content:** write about what was discussed and what changed. For example, "three roadmap items came from this table". That is worth more to readers than guest praise.
- **Voice:** have a maintainer or DevRel write it, not the marketing team.

## What to measure

Don't count leads, because the event isn't built to produce them. Use outcomes you can defend:

- **Contributor retention:** how many invited contributors open a PR, issue or review in the 90 days after, against their own pre-event baseline.
- **Conversion to repeat contribution:** first-time contributors who make a second contribution.
- **Product signal:** the number of concrete issues or RFC comments that came out of dinner conversations.
- **Opt-in rate and what opted-in guests do next:** report these as a side effect, not the goal.

Set targets from your own contributor-activity baseline. I don't have your numbers, so I haven't invented any.

## Message to Marketing

> We keep the dinner and the recap, and the demo gets its own slot where people choose to come. Badge scans and automatic nurture enrollment break the consent people gave when they RSVP'd, so we use an opt-in checkbox instead. You get a smaller list of people who want to hear from us, and we protect the contributor trust that the cloud business depends on.

## Open questions

These would change the plan:

1. Do you already have PyCon sponsor terms on lead retrieval? Who owns them?
2. Is the budget fixed at 30 seats, or can it be a smaller room if you can't fill it with the right mix?
3. Do you have EU or UK contributors on the list? That raises the consent bar.
4. Who owns the follow-up emails: DevRel or Marketing? Settle this before the invites go out.
# Follow-up messages

Contents: templates per track → good and bad pairs → hackathon and workshop variants → measurement sheet.

Adapt the words; keep the order: who you are and where you met, their problem in their words, what you promised, one next step. Plain text, from a person's address, one link where possible. Run every draft through your preferred humanizer skill before it sends.

Any message the gate classes as marketing (community invitation, nurture, a promised-item message carrying the opt-in line) ends with `<sender identification + postal address + unsubscribe or objection link>`: CAN-SPAM, CASL and EU/UK soft opt-in each require it in every message. A requested reply carries none, because it is not marketing.

## Personal note (A)

```
Subject: <their problem, in their words>

Hi <first name>,

We talked at <event> about <problem as they said it> on <stack>.
As promised: <the item, attached or one link>.
<Next step agreed at the booth: "I'll ping you Thursday to see if the import ran" / "Here's a 30-minute slot with Priya, who built that part">.

<staffer name>
```

## Promised-item message (B)

```
Subject: The <item> from <event>

Hi <first name>,

Here's the <item> you asked for at <event>: <link>.
<Only where the gate's marketing column says yes:> If you'd like occasional updates on <topic>, you can opt in here: <link>.
This is the only email you'll get from me about it.

<staffer or DevRel name>
```

## Community invitation

```
Subject: <community> - where people working on <problem> compare notes

Hi <first name>, you mentioned <topic> at <event>. <N> people building the same thing talk in <community>: <link>.
The next <meetup / office hours> is <date>.

<sender identification + postal address + unsubscribe link>
```

## Sales handoff (A with a buying signal)

Same thread as the personal note, never a new cold sequence:

```
Hi <first name>, you asked about <pricing / SSO / procurement> at <event>.
I'm adding <account owner>, who handles that, so you don't have to repeat yourself. I'll stay on the thread for the technical side.
```

## Good and bad pairs

```
// ✓ Good - from the person they met, their words, the promised item, one next step
Subject: staging DB refresh taking a day
Hi Ana, we talked at KubeCon about the day-long staging refresh blocking releases on your Postgres 15 / EKS setup.
Here's the Terraform module we sketched and the event credit. I'll check in Thursday.
Priya

// ✗ Bad - generic, from a marketing alias, ignores the conversation, adds a purpose
From: marketing@acme.dev
Subject: Thanks for visiting Acme at KubeCon!
Great to meet you! Check out our latest features and book a demo today.
```

```
// ✗ Bad - sales sequence on a student from the hackathon
Subject: Quick question about your team's budget
// Students and hobbyists route to community or recruiting. This email comes back to DevRel as a complaint.
```

## Hackathon variants

- Within two days: public showcase of every submission (with the teams' permission), named winners, the repo links.
- Teams that built on your API: personal note referencing their project by name, an offer to feature it with permission, extended credits.
- Day 30: one check-in to teams whose repo still shows commits; ask what blocked them, route bugs to engineering.
- Everyone else: the showcase link, and the community invitation where the basis covers it.

## Workshop variants

- The activation path: a "finish the exercise" page that starts from the step where the session ended, with a credit or sandbox already provisioned.
- Send it within the week to every roster member whose sign-up line covered the materials.
- Record which attendees reach the activation event; those who stall at the same step tell you where the workshop or the docs break.

## Measurement sheet

| Field                                                 | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- |
| event, date closed                                    | DevOpsDays Lyon, 2027-03-12                           |
| cohort tag                                            | `evt-dodlyon-2027` on signup and credit codes         |
| activation event                                      | first successful API call                             |
| counts by grade                                       | A 14, B 37, C 210                                     |
| messages sent per track                               | personal 14, promised item 37, recap published        |
| replies to A notes                                    | 9 of 14                                               |
| activated by day 30 / 60 / 90, per grade              | A 6 / 8 / 9, B 5 / 7 / 8                              |
| non-event baseline for the same window                | same-month organic signups                            |
| complaint rate, unsubscribes, max days to suppression | 0.02%, 3, 1 day                                       |
| opportunities sourced / influenced                    | 0 / 2                                                 |
| threshold and label                                   | 8 A activations by day 60, self-set from last edition |

Figures in this sheet are constructed for illustration.

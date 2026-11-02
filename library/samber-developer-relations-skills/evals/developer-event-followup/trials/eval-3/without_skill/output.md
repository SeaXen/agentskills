# Workshop follow-up plan and 60-day boss readout

## Verdict

Send the slides and thank-you, but don't auto-add everyone to the newsletter. The sign-up form promised "get the workshop materials", and nothing more. A newsletter subscription is a different purpose, so it needs its own opt-in. PyCon US draws EU and UK attendees, so GDPR/PECR likely apply, and CAN-SPAM requires an unsubscribe in any case. Auto-adding 45 people also gives you a padded subscriber count that shows nothing.

A newsletter count also won't impress your boss. A better 60-day result is how many attendees built something on your product.

## Plan

| When | Action | Why |
|---|---|---|
| Day 0–2 | Send materials, thank-you, and one opt-in line | This fulfils the promise and asks for the newsletter openly. |
| Day 3–7 | Send a "stuck on anything?" note with office-hours or reply-to | This surfaces blockers and gives you quotes. |
| Day 14 | Send a nudge to people who haven't hit the activation event | This is the highest-leverage follow-up. |
| Day 30 | Run a mid-point data pull | It shows whether the plan works while you can still adjust. |
| Day 45 | Final data pull | Leaves time to write it up. |
| Day 60 | Show the one-pager to your boss | |

If the workshop was already more than a few days ago, send now and skip the apology. Lateness costs less than silence.

## Set up before you send

1. **Pick one activation event** that proves the person got value. Examples are "created a cluster and ran a query" or "indexed their own data", not "opened the email". I don't know your product, so you pick this.
2. **Make the follow-up trackable.** Use a workshop-specific link with UTM parameters, or a workshop code on signup. Without this you can't tie product usage back to the room.
3. **Record the baseline.** Note how many of the 45 actually attended (roster is not attendance), and how many already had an account before the workshop.
4. **Add two survey questions** to the materials email:
   - "What will you build with this?"
   - "What blocked you?"

## Email 1: materials, thank-you, opt-in

> **Subject:** Your retrieval pipeline workshop materials
>
> Hi {first_name},
>
> Thanks for spending 90 minutes with us at PyCon US. Here's what you asked for:
>
> - Slides: {link}
> - Workshop repo and starter code: {link}
> - Free sandbox to keep building: {tracked link}
>
> Two quick questions. Reply with one line each:
> 1. What are you planning to build with this?
> 2. Where did you get stuck?
>
> I read every reply, and I'm happy to help you get unstuck.
>
> We also send a monthly newsletter on retrieval patterns and product updates. If you want it, [click here to subscribe]({opt-in link}). If not, you won't hear from us again beyond this thread.
>
> {name}

The opt-in link should be a real confirmation. Don't use a pre-ticked box.

## Email 2, day 14: only for people who haven't activated

> **Subject:** Did the pipeline run for you?
>
> Hi {first_name}, most people hit one of two snags after the workshop: {snag 1} and {snag 2}. Here's the fix for each: {link}. If you're stuck on something else, reply and I'll look at it this week.

Use the real top two snags from the Day 3–7 replies instead of the placeholders.

## 60-day one-pager for your boss

Fill this in with real numbers. Leave a cell blank rather than estimate it.

**Workshop: Building retrieval pipelines at PyCon US**

| Metric | Value | Note |
|---|---|---|
| Roster / attended | 45 / {n} | |
| Opted in to newsletter | {n} ({%}) | Explicit opt-in only |
| Replied to follow-up | {n} | |
| Created account or sandbox via tracked link | {n} | |
| **Reached activation event** | **{n} ({%})** | Primary result |
| Still active at day 60 | {n} | |
| Teams or companies represented | {n} | Qualitative pipeline signal |
| Cost | {hours + travel + sponsorship} | |

**What we learned:** top 2–3 blockers from replies, with 1–2 verbatim quotes (get permission before quoting by name).

**What changes next time:** one or two concrete items, such as "fix the setup step that blocked {n} people" or "add the activation step to the workshop itself".

**Recommendation:** repeat, change, or drop, with the reason.

## Caveats

- 45 people is a small sample. Expect single or low double digits at the activation step, and present it that way. A cohort of 8 who built something real plus clear blockers is a good result. A big headline number would not survive questions.
- Report activation as a share of attendees, not of the roster. Otherwise no-shows drag the rate down.
- Don't credit the workshop for anyone who already had an account before it. The baseline step handles this.
- I haven't seen your product, signup flow or analytics setup, so the activation event and tracking method above are placeholders for you to fill in.

## Questions for you

1. What is the one action that counts as "got value" in your product?
2. Do you have the roster's emails from the form only, or also from badge scans?
3. Does your newsletter tool support double opt-in?

I can tailor the emails and one-pager once I know those answers.
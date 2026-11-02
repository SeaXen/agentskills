# Corvid Conf tracing workshop: making questions safe to ask

**Core idea:** the problem is the cost of asking in front of a senior expert, not the instructor's content. Redesign the session so most questions never need a public ask. For the rest, give people a low-exposure way to ask.

## 1. Change the structure (biggest lever)

- 🎯 **Pairs, not individuals.** Seat 12 people as 6 pairs. Questions go to the partner first, which is a tiny, safe step.
- 🎯 **Add a floor helper.** Pick a mid-level engineer, not the principal. They walk the room during exercises and take first-line questions. Juniors ask peers-ish people far more readily.
- 🎯 **Hands-on dominates.** Cap talking at 10 minutes per block, then at least 20 minutes of exercise. The instructor spends exercise time circulating and **sitting beside** people, not standing at the front.
- 🎯 **Show-and-tell by pair, never by person.** Nobody gets cold-called.

## 2. Give people a quiet way to ask

- ✅ **Signal cups or sticky notes** (green = fine, yellow = stuck, red = need help). The helper sees yellow and comes over, so no hand-raising is needed.
- ✅ **Anonymous question wall.** Use paper cards or a shared pad (Slido works too). The instructor answers a batch at each checkpoint, without names.
- ✅ **Replace "Any questions?"** with "Write down the most confusing thing so far." Writing is the exercise, so everyone does it and nobody is singled out.
- ✅ **Help ladder, written on the slide:** ask your partner, then the next pair, then the helper, then the instructor.
- ✅ **Seed the first questions.** The helper asks one deliberately basic question early (for example, "wait, what exactly is a span?"). That sets the bar low.

## 3. Brief the instructor (15 minutes, before the session)

Frame it as a design goal, not a criticism: "Most of the room has never been to a conference. Success means they ask."

- Open with a **story of his own tracing mistake**, ideally one that cost him days. That lowers the status gap.
- After any question: thank the person, answer in under 60 seconds, then ask "does that match what you see on your screen?"
- Wait about 7 seconds after asking something. Don't fill silence.
- Avoid "as you know", "obviously", and finishing people's sentences.
- Don't hover behind screens. Kneel or sit next to the person.
- If he is not comfortable doing this, split roles. He gives the short demos, and the helper leads the exercises.

## 4. Sample 120-minute agenda

| Time | Block |
|---|---|
| 0:00–0:10 | Welcome, pairs, norms ("questions are the work here"), instructor's failure story |
| 0:10–0:20 | Short live demo: one trace end to end |
| 0:20–0:50 | Exercise 1 (pairs): find the slow span in a prepared trace. Checkpoint: question cards |
| 0:50–1:00 | **Break.** Most 1:1 questions surface here, so keep the instructor and helper in the room |
| 1:00–1:35 | Exercise 2 (pairs): instrument a small service |
| 1:35–1:50 | Exercise 3 (pairs trade): find the bug in another pair's broken trace |
| 1:50–2:00 | Wrap-up: "one thing still unclear" cards, answered aloud. Share a standing channel for follow-ups |

## 5. Prep that removes avoidable fear

- **Pre-built environment** (container or hosted sandbox) so nobody fails on setup in front of peers.
- **Pre-email a week out:** agenda, what to bring, who the instructor and helper are (with photos), and a line saying "no prior tracing knowledge needed, questions are expected."
- **Conference buddy:** pair each first-timer with a veteran for the day, since this session may be their social anchor.

## 6. Check it worked

- Send an **anonymous 3-question form**. One of the questions: "Did you ask everything you wanted to?"
- Ask the three people from last year what would have helped. You'll get better input than my guesses, and it shows you listened.

## Avoid

- Cold-calling
- Individual presentations
- Two hours of the instructor at the front
- Telling attendees "don't be shy"

## Open questions for you

1. Who could be the floor helper?
2. Is the environment already containerized, or does that need building?
3. Will the instructor accept a pre-brief, and does he have any say in the format?
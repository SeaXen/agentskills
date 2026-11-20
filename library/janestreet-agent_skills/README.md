# Agent skills from Jane Street

A collection of skills for AI agents and chatbots.
Each skill is a directory containing a `SKILL.md` file
with instructions for the agent.

## Skills

- **socratic-tutor** — turns an LLM into a strict personal tutor that teaches a
  topic of your choice using the Socratic method: a diagnostic, a skill map with
  levels 0-5, one question at a time, spaced review, and a final assessment.

## How to use

With a coding agent that supports the common `SKILL.md` format, copy the skill
directory into your agent's skills folder, then ask the agent to use it
("teach me X").

With a plain chatbot, paste the body of the skill's `SKILL.md` into the chat
(or into a custom/system prompt), followed by what you want it to do.

## Contributing

These skills are exported from our internal repository, where we use them day to
day, and we hope it's interesting to share that experience more widely. Since
we're trying to share what _we've_ found to be useful, we're not looking for new
skills or for pull requests that change the text of existing ones. If you've
adapted a skill and it works better for you, that's great, but please keep your
own copy.

Issues are welcome if something doesn't work as described, though we may not be
able to act on all of them.

## Prior art

Teaching by asking questions is the
[Socratic method](https://en.wikipedia.org/wiki/Socratic_method), which is
rather older than LLMs, and there are other tutoring prompts and skills built on
the same idea. Our skill was written internally and isn't knowingly derived from
any other implementation.

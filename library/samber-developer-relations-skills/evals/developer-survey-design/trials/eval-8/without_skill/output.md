Before the draft, two things to settle, because they change which questions are worth asking.

**1. Name the decision first.**
- "A pulse" with no planned use is the weakest case for a survey. Answers with no decision attached tend to get skimmed once and forgotten.
- Your community will have spent its time and attention on that.
- Ask the founder one question: "If 60% said X, what would we change?"
- A weak answer is still useful. A "pulse" survey should be short and re-runnable, so you can compare the next one.
- I tagged each question below with the decision it could feed. Cut any question whose tag nobody cares about.

**2. Respondents will only see what you tell them.**
- "No plans to publish" is fine. But promise respondents a short "what we heard and what we'll do" note, even a few lines.
- Without it, response rates drop on the next survey.
- Keep it anonymous by default and collect no personal data except an optional email at the end. That keeps GDPR simple.

Also expect bias. Respondents out of roughly 4k stars will skew toward your most engaged users. Treat the results as "what engaged users think", not "what the community thinks".

---

# Cinderwell community survey (draft)

**Intro text**

> Help us make Cinderwell better. This takes about 4 minutes. It's anonymous unless you choose to leave your email at the end. We read every answer, and we'll share a short summary of what we heard and what we're doing about it.

**About you** *(segments every other answer)*

1. **Which best describes your use of Cinderwell?** *(single choice)*
   - Running it in production
   - Running it in staging, dev or a side project
   - Evaluating it right now
   - Tried it and stopped
   - Haven't used it, I follow the project
   - I contribute code or docs

   *Skip logic: "Haven't used it" jumps to Q8. "Tried it and stopped" goes to Q7 first.*

2. **How do you run it?** *(multi-select: Kubernetes, VMs or bare metal, serverless or edge, local dev only, other)*
   Also ask: **Roughly how much traffic does it handle?** *(under 100 req/s, 100–1k, 1k–10k, over 10k, don't know)*

**Usage** *(feeds docs and roadmap priorities)*

3. **For each feature, how would you describe your use?** *(grid: "Use in production", "Tried it", "Didn't know it existed", "Don't need it")*
   - [Insert your 8–10 real features, e.g. routing, auth plugins, rate limiting, observability, config reload, admin API]

   The "didn't know it existed" column is the most useful one. It separates a discoverability problem from a demand problem.

**Sentiment** *(feeds retention and positioning)*

4. **How satisfied are you with Cinderwell overall?** *(1–5)*
   Follow-up, open: **What is the main reason for that score?**

5. **How disappointed would you be if Cinderwell stopped existing tomorrow?** *(Very / Somewhat / Not disappointed / I no longer use it)*
   This is a stronger signal than satisfaction, which people inflate for free tools.

6. **What would you use instead?** *(open, or a list of the main alternatives plus "build my own")*

**Gaps** *(feeds roadmap)*

7. **What is the biggest frustration you've had with Cinderwell in the last 3 months?** *(open)*
   *Shown to "tried and stopped" users as "What made you stop?"*

8. **Is there something you wanted to do with Cinderwell but couldn't, or gave up on?** *(open)*

9. **Pick the 3 things that would help you most.** *(choose up to 3)*
   - [Insert 6–8 real candidate items: a feature, better docs, performance, a managed or hosted option, more integrations, a stability guarantee, etc.]
   - Other: ___

   Only include options you'd realistically consider. Don't list ideas you'd never build.

**Community and support** *(feeds DevRel channel choices)*

10. **When you're stuck, where do you go first?** *(rank or pick top 2: docs, GitHub issues, Discord or Slack, search engine, Stack Overflow, AI assistant, ask a colleague)*
    **How would you rate the docs?** *(1–5, with an optional "what's missing?")*

**Close**

11. **Anything else you want us to know?** *(open, optional)*
12. **Open to a 20-minute chat with us?** *(optional email field)*
    The chats are probably the highest-value output of the whole survey.

---

## Running it

- **Length:** the intro estimate of 4 minutes assumes about 8 required answers. Make Q6, Q8 and Q11 optional.
- **Tool:** use Tally, Typeform or Google Forms with no required login.
- **Distribution:** use the repo README, release notes, your Discord or Slack, and one social post. Keep it open for 2–3 weeks.
- **Timing:** avoid launching it during a release week, when answers skew toward the new release.
- **Pilot:** send it to 5 people first. If any question confuses them, fix it before the wide launch.
- **Reading results:**
  - Segment everything by Q1 and Q2. Production users and evaluators want different things.
  - Read the open answers (Q7, Q8) before looking at the charts.
  - Q3 "didn't know it existed" and Q5 "not disappointed" are the two numbers to watch.
- **Repeat:** if you want a real "pulse", rerun the same questions every 6 months. Don't change the wording, or you lose the comparison.

## Open items for you
- Fill in the feature list for Q3 and the candidate list for Q9. I don't have your product details.
- Tell me whether the founder can name one decision this should inform. If so, I'll trim the survey to the questions that matter for it.
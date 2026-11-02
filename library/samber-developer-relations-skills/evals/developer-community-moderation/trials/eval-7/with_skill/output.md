## The call: grade individually, don't blanket-recuse

Blanket-recusing all four Orrindale people isn't the fix — it trades one bias problem for a worse one (n=1 deciding), and it throws away people who could legitimately still take part. The runbook uses two grades precisely because treating every connection the same "either paralyses a small team or lets a conflicted member vote."

Grade each person against the two buckets:

| Person | Connection | Grade | What they can do |
|---|---|---|---|
| Two responders | Sit in Marisol's weekly standup | **Hard** — close professional relationship | Out entirely: no discussion, no vote, no access to confidential material |
| One responder | Shares a manager with Marisol | **Soft** — same employer, no close relationship (unless in practice they work closely with her too — self-declare if so) | Can take part in discussion, cannot vote |
| One responder | Only ever met her at an offsite | **Soft** — this is the textbook case the runbook names: "same employer without a close relationship" | Can take part in discussion, cannot vote |
| Fifth responder | No connection at all | **No conflict** | Full participant, can vote |

## Run the numbers before deciding anything else

The decision rule is "at least two non-conflicted members agree, consensus preferred, two-thirds majority as fallback." Soft-conflicted people don't count toward that — they can talk, not vote. After correct grading:

- Hard-conflicted (excluded outright): 2
- Soft-conflicted (can discuss, can't vote): 2
- Fully clean: **1** (the customer-side contributor)

One clean voter is below the floor the rule requires. This isn't a close call and it isn't solved by anyone recusing further — it's already the minimum footprint on your side. So:

**This case escalates to the body named above your response team**, the same as if everyone were conflicted. If Orrindale hasn't named that body yet, that gap is the actual finding here, not the recusal question — name it now (a senior neutral leader, a cross-functional panel, whoever sits above the five of you) before this case can close. Since Marisol is an employee and any sanction against her is also an HR/employment decision, loop in the HR/legal interface at the same time — don't let that surface for the first time at the sanction stage.

Your instinct that "one person deciding alone" is wrong was correct — you just arrived at the same one-person problem from the other direction. The fix isn't fewer Orrindale people in the room, it's routing the actual decision to a body sized to make it.

## The clock, regardless of who ends up deciding

The clock started when the report landed, not when this gets sorted out — recusal wrangling doesn't pause it:

- **Acknowledge the reporter now**, before the escalation question is even settled. Published bands: 1 business day (Django) to 3 business days (CNCF) — pick one and hold it literally.
- **Decision target: 10 business days** from report to decision (Aurora & Gardiner's worked benchmark), whether it's your panel or the escalation body deciding. Escalating changes who decides, not when it's due — hand the clock to them, don't reset it.
- The dominant failure mode here is a case that drifts because nobody quite owns it once it escalates — put the deadline in the escalation body's calendar the moment you hand it over, not as a follow-up.

## Before any of that

- Have all four Orrindale-side people declare their conflict **in writing, now** — recusal takes effect the moment someone realizes it applies, including mid-read of the report.
- Record each grade and rationale in the case file before investigation starts. That record is what makes this defensible later if anyone questions how the panel was composed.
- Separately, flag for your own roster review (not this case): a 5-person team where 4 sit at one employer will hit this exact quorum wall on a recurring basis whenever the report touches that employer's staff. Worth a cap on seats from a single employer next time you revisit the roster.
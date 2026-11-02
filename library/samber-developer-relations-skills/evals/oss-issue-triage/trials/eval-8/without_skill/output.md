Quick math check before the draft: 2 engineers × ~6h/week = 12 combined engineer-hours/week covering the public tracker — and those same 2 people are contractually on the hook for 4-hour response across 11 enterprise contracts, which will take priority whenever both queues hit at once. A literal "24-hour response on all GitHub issues" reads as calendar hours with no carve-out (weekends, holidays, a single support incident eating a whole engineer's day) — that's a materially harder bar than "1 business day," and unlike a private enterprise SLA miss, a broken public promise sits on a timestamped issue thread for anyone to screenshot. I've drafted it scoped to business days rather than raw calendar hours, since that's the version 12h/week can actually sustain — flag it to leadership if they specifically want the calendar-day framing instead, since that's a different (harder) commitment.

---

## Support & Response Times

**Community support (GitHub Issues)**

We aim to respond to every new issue within 24 hours on business days (Mon–Fri). Response times may be longer around holidays or during periods of high issue volume.

**Enterprise support**

Organizations with an active Halbrecht Systems support contract receive a guaranteed 4-hour response time, backed by an SLA. [Contact us](mailto:support@halbrechtsystems.example) to learn more about enterprise support.

---

Two things worth deciding before this goes live:

1. **"Aim to" vs. "guarantee."** I used "aim to" for the community tier and reserved "guaranteed... SLA" for enterprise. Using "guarantee" in both places blurs the thing your 11 paying contracts are actually paying for — worth keeping that distinction explicit rather than letting the free tier borrow the paid tier's language.
2. **Business days vs. calendar days.** If leadership specifically wants "24 hours, no exceptions, every day of the week" published as-is, say so — that's a stronger public commitment than 12 combined engineer-hours/week can reliably back once an enterprise incident lands mid-week, and it's worth them making that call knowingly rather than by default.
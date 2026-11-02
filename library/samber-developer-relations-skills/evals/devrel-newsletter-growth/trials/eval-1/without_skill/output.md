# Plan: hmig changelog digest, 2,300 to 10k

## Verdict

- **(1) In-CLI prompt:** keep it, with changes. It is your best channel and it's free.
- **(2) Bulk import of 14,000 trial accounts:** don't do it. Replace it with a consented invite.
- **(3) Reporting total list size:** keep it, but report it next to active subscribers, or the number will mislead you.
- **The target:** 10k by end of Q2 is probably out of reach on 6 hours a month. Re-baseline it with your VP in month 1 (see "The math").

## Why not the bulk import

- **ToS acceptance is not marketing consent.** Under GDPR and ePrivacy, and under CASL in Canada, a newsletter needs its own opt-in. Some jurisdictions allow a "soft opt-in" for existing customers, but it is narrow. It generally covers business addresses, similar products, and an opt-out offered at collection. Trial accounts on personal emails usually fall outside it.
- **Legal check first:** have counsel confirm what your ToS and privacy policy actually say. I can't see them, and this is not legal advice.
- **Deliverability risk:** mailing 14,000 cold-ish addresses at once means spam complaints, bounces, and possible ESP suspension. That would also damage the 2,300 people who actually want the digest, and you've shipped every issue on time.
- **It inflates the number without adding readers.** Your VP would see 16,300, but engagement would collapse and the real audience would not change.

**Replacement: a consented invite to trial accounts.**

1. Check the ToS and privacy policy against the jurisdictions your trial users live in.
2. Segment the 14,000: active in the last 90 days, corporate vs personal domain, EU vs non-EU.
3. Send a one-time, product-side email (not the newsletter) with a single button: "Get hmig release news". The button leads to a double opt-in.
4. Test on a sample of about 1,000 first, then send the rest in waves. If complaints or bounces rise, stop.
5. Treat 5-10% opt-in (about 700-1,400 people) as a rough planning range. This is my assumption, not a benchmark. Replace it with your sample result.
6. Add an unchecked "Send me release news" checkbox to cloud signup from now on. Unchecked checkboxes keep the list clean.

## Fixing the in-CLI prompt

The one-liner after every migrate is the risky part. `hmig` runs in CI and in production pipelines, where unwanted output annoys people and can break scripts.

- Print to **stderr**, never stdout.
- Show it **only in an interactive terminal**: skip it when there is no TTY, when `CI` is set, or when output is piped.
- Show it **rarely**: once per install, then again after 30 days or on a major version. Keep state in a small local file, not a network call.
- Add opt-outs: `HMIG_NO_PROMPT=1`, `DO_NOT_TRACK`, and a `hmig config` setting.
- Have `hmig subscribe` **print a URL** (and optionally open the browser). Don't make the CLI send an email address or any other data. A migration tool that phones home will upset security-conscious users.
- Use **double opt-in** on the landing page, and add a UTM or `?src=cli` parameter. That lets you attribute signups.
- Use a short message, for example: `Release news for hmig: https://driftmoor.example/hmig-news (hide: HMIG_NO_PROMPT=1)`. The domain is a placeholder.
- The engineering work is about 1-2 days from the hmig team. It should not come out of your 6 hours.

## The math

- **Today:** 2,300 subscribers after 18 months, about 128 net per month.
- **Required:** assuming Q2 ends 2027-06-30, that's 8 months and about 7,700 net new. That is about 960 per month, roughly 7.5x your current rate.
- **What the CLI can deliver:** `signups per month ≈ unique interactive users per month × share who see the prompt × click-through × completed opt-in`. With 2% click-through and 50% completion, 960 per month needs about 100k unique interactive users per month. Check your real number before promising anything.
- **One-time trial invite:** about 700-1,400 (an assumption, see above).
- **Likely outcome:** a few thousand total, not 10k, unless hmig's user base is much bigger than the newsletter suggests.

**Proposal for your VP in month 1:**

- Share the model above with the real inputs filled in.
- Agree on two numbers: total subscribers, and **active subscribers** (clicked at least one issue in the last 90 days).
- Reset the Q2 target once the first 60 days of data are in.

## Reporting (item 3, upgraded)

Send one short monthly table:

| Metric | Why |
|---|---|
| Total subscribers | The VP's headline number |
| Net new, with source (CLI, docs, cloud signup, trial invite, other) | Shows which channel works |
| Active subscribers (90-day click) | The audience that exists |
| Click rate per issue | Use clicks, not opens: Apple Mail Privacy Protection inflates opens |
| Unsubscribes and spam complaints | Early warning for the invite and the prompt |
| Projected date to reach target at the current rate | Keeps the VP's expectations honest |

Always show the total next to the active number. If the total grows and the active number doesn't, the list is getting bigger without getting more useful.

## Timeline (6 hours a month)

| Month | Work | Your hours |
|---|---|---|
| Nov 2026 | Baseline the metrics. Get the legal check on the ToS. Spec the prompt for engineering. Put the numbers and the target discussion to your VP. | 6 |
| Dec | Launch the prompt (behind a flag if possible). Add a signup page with a source parameter and double opt-in. Send the 1,000-account sample invite. | 6 |
| Jan | Read the sample results. Fix problems. Send the trial invite in waves. Add the unchecked cloud-signup checkbox. | 6 |
| Feb | Review prompt conversion. Tune the frequency and wording. Add signup links in docs, the release-notes page, and GitHub release footers. | 6 |
| Mar | Add a "forward to a colleague" link and a web archive of past issues for search traffic. | 6 |
| Apr-Jun | Maintenance mode: monthly report, one experiment per month (such as wording or placement), and a Dario-run issue if you need the time back. | 6 |

I don't know how many of the 6 hours the digest itself takes, so the table above assumes setup fits alongside it. If the issues use most of your time, have Dario write one issue per quarter and move those hours to growth.

## Questions for you

1. **Jurisdiction:** where are your trial users based, and does your ToS or privacy policy mention marketing email?
2. **Users:** how many unique people run `hmig migrate` interactively per month? This determines whether the CLI prompt can reach the target.
3. **Hours:** how many of your 6 hours does the digest already use each month?
4. **Quarter:** does "end of Q2" mean 2027-06-30, or is your fiscal year different?
5. **Channel:** which ESP do you use, and does it enforce double opt-in and handle suppression lists?
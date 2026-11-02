# Brackenmoor State of Edge Functions: raffle announcement and draw procedure

## Read this first

- ⚠️ **The raffle probably won't close the gap.**
  - You're at about 9 completes a day and need about 78 a day for the next 18 days.
  - A single big prize usually lifts response rates. It rarely lifts them 9×.
  - Run it, but also pick a fallback now: a lower target (about 400 completes gives usable segment cuts), a deadline extension, or a partner or newsletter push. Decide by about day 5 of the raffle.
- ⚠️ **Don't put the email field inside the survey form.**
  - Send finishers to a separate entry form after submit, stored apart from the answers and with no shared ID. Your survey stays anonymous and your GDPR exposure stays small.
  - The announcement promises anonymity, so build it that way.
- ⚠️ **Have counsel review the rules before you post.** I'm not a lawyer. The sections below flag what to check.

Assumptions you can change: the survey closes Tue 2026-11-10 at 23:59 UTC, and the draw is Thu 2026-11-12 at 14:00 UTC.

## 1. Announcement copy

### Twitter/X (single post, under 280 characters)

> The Brackenmoor State of Edge Functions survey is open until Nov 10.
>
> 10 minutes, anonymous answers, free public results.
> Finish it and you can enter a draw to win a [PRIZE, up to €X].
>
> Survey: [LINK]
> Rules: [RULES URL]

Reply to it with:

> No purchase necessary. One entry per person. Open to residents of the EU/EEA, UK and US, 18+. Your email goes in a separate form and is never linked to your answers.

### Reddit (title and body)

**Title:** `We're surveying how people actually use edge functions (10 min). One respondent wins a [PRIZE]`

**Body:**

> Hi all, I'm [NAME] at Brackenmoor. We're running the State of Edge Functions survey: runtimes, cold starts, limits, what breaks in production, what you'd change.
>
> - 10 minutes, no account needed
> - Answers are anonymous. The prize entry is a separate form at the end, and we don't link the two
> - Full results and the raw aggregate data will be published free, whether or not you take part
> - Closes Nov 10
>
> As a thank-you, one respondent wins a [PRIZE, up to €X]. The draw is public and verifiable: the method is in the rules.
>
> Survey: [LINK]
> Official rules: [RULES URL]
>
> Questions about the survey or the draw: happy to answer in the comments.

Don't make retweeting, following or upvoting a condition of entry. It attracts spam entries and platform enforcement, and it adds nothing to completes.

## 2. Official rules (publish at [RULES URL])

Include each of these:

1. **Organizer:** Brackenmoor, [legal form, address, France].
2. **No purchase necessary.** Entry is free and costs only your time.
3. **Eligibility:** 18 or older, resident of the EU/EEA, UK or US. Exclude employees and their households, and sanctioned countries. Add "void where prohibited". Counsel should decide on Quebec and any other jurisdiction you want to exclude.
4. **Dates:** Oct 23 to Nov 10, 2026 (23:59 UTC). Draw on Nov 12, 2026.
5. **How to enter:** complete the survey, then submit the separate entry form. One entry per person, deduplicated by normalized email.
6. **Alternate free entry:** email [ADDRESS] with the subject "Entry" to get one entry without taking the survey. This protects you in the US, where survey effort can be argued to be consideration.
7. **Valid entries only:** the survey counts only if it passes your data-quality checks. Fix the checks now and publish them. For example: a minimum completion time, one attention-check question, and no duplicate submissions. Quality checks never depend on what someone answered.
8. **Prize:** one [model], retail value up to €[X]. No cash alternative. Keep the value under US$5,000 so you avoid New York and Florida registration and bonding. Counsel should confirm.
9. **Winner selection:** random draw as described in section 3. Odds depend on the number of valid entries.
10. **Notification:** the winner is emailed within 48 hours. If there's no reply in 7 days, the prize goes to the next alternate.
11. **Shipping and taxes:** you ship to the winner. Any duties, VAT and income tax are the winner's responsibility.
12. **Data protection (GDPR):**
    - Controller: Brackenmoor.
    - Purpose: running the draw and contacting the winner only.
    - Legal basis: consent.
    - Retention: delete all entry emails within 30 days after prize delivery. Delete the winner's data when the prize is delivered and the tax paperwork closes.
    - Rights: access, erasure and withdrawal via [ADDRESS]. Withdrawal removes the entry.
    - Never used for marketing without a separate opt-in.
13. **Governing law:** French law. Name the competent courts.

French law allows a free-entry prize draw if the rules are clear and available at no cost. Depositing the rules with a commissaire de justice is optional but common. Ask counsel whether you want it.

## 3. How to run the draw

The goal is that anyone can check you didn't pick the winner. Use a public randomness beacon (drand) and commit to the entry list before the random value exists.

### Before the draw (Nov 10 to 12)

1. **Close the survey** and export the entry form.
2. **Build the eligible list:**
   - Normalize each email: lowercase, trimmed.
   - Remove duplicates.
   - Remove ineligible countries and employees.
   - Remove entries whose linked survey failed the published quality checks.
   - Keep the removed rows and the reason for each.
3. **Sort the list** alphabetically and write it to `entries.txt`, one email per line.
4. **Commit publicly.** Compute `sha256sum entries.txt` and post only the hash and the entry count N. This fixes the list before the random value is known. Don't post the emails.
5. **Pick a drand round in the future** (at least an hour after you post the commitment) and post its round number and time.

### At the draw

The script below fetches that round's randomness from drand's `quicknet` chain and turns it into a winner and two alternates.

```python
#!/usr/bin/env python3
"""Usage: draw.py entries.txt <drand_round>"""
import hashlib, json, sys, urllib.request

CHAIN = "52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971"  # drand quicknet
entries_path, rnd = sys.argv[1], int(sys.argv[2])

raw = open(entries_path, "rb").read()
entries = raw.decode().splitlines()
assert entries == sorted(entries), "list must be sorted"
assert len(set(entries)) == len(entries), "list has duplicates"
print("entries:", len(entries), "sha256:", hashlib.sha256(raw).hexdigest())

url = f"https://api.drand.sh/{CHAIN}/public/{rnd}"
with urllib.request.urlopen(url, timeout=15) as r:
    beacon = json.load(r)
randomness = beacon["randomness"]
print("round:", rnd, "randomness:", randomness)

# Winner, then two alternates, without replacement. Each pick hashes the
# randomness with a counter, so the three picks are independent.
pool = list(range(len(entries)))
for label in ("winner", "alternate 1", "alternate 2"):
    k = len(label) + len(pool)  # any fixed, published counter works; keep this line unchanged
    h = int(hashlib.sha256(f"{randomness}:{label}".encode()).hexdigest(), 16)
    idx = pool.pop(h % len(pool))
    print(f"{label}: line {idx + 1} of {len(entries)}")
```

Delete the unused `k = ...` line before publishing the script. It does nothing.

Publish the script, the commitment hash, the drand round and the output. Anyone with `entries.txt` can rerun it. Only you hold the file, so recheck it yourself and have a second person (a colleague, or a commissaire de justice if you used one) run it on their machine and compare.

Check the chain hash and API URL against drand's current documentation (drand.love) before the draw. Run the script on a dummy list a few days earlier to confirm it works.

### After the draw

1. Email the winner from a company address. Don't DM them from social media first.
2. Ask them to confirm eligibility and shipping details. Wait 7 days. If there's no reply, move to alternate 1, then alternate 2.
3. Post "Winner drawn" with the line number and the hash. Never post the winner's name without their consent.
4. Ship the prize. Keep the paperwork for your accountant.
5. Delete all entry emails within the 30 days promised, then post a one-line confirmation.

## 4. Quality risks to plan for

- A big prize attracts people who rush through the survey just to enter. Keep the attention check and the minimum-time rule from point 7 above, and report in the results how many entries you dropped.
- Don't weight the draw or the prize by answers. Keep the draw fully independent of what people said.
- The 90 completes you already have predate the raffle. Compare them with the later ones on country, role and company size, and note any shift in the write-up.

## 5. Next steps

1. Tell me the prize model and value cap, and I'll fix the placeholders.
2. Send the rules to counsel today.
3. Build the separate entry form this week.
4. Post once the rules are live. The sooner the post goes out, the more of the 18 days it gets.
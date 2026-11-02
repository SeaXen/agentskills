# Renewal, retake and retirement (draft)

I changed two of your three decisions. The reasons come first so you can overrule me. The section follows.

## What I changed, and why

1. **Re-certify every release → renew per major.**
   - Releases ship every two weeks, which is about 26 a year. Operators would re-test every two weeks.
   - Your two contracts require named certified operators. With this rule, each account would drop out of compliance every time a release shipped, until its operators retested.
   - The thing that changes the operator's job is the major version, so the credential should track the major.
2. **Void v3 holders at v4 → don't.**
   - v3 stays supported for 24 months after its own release, so it outlives v4's arrival by about a year.
   - Customers running supported v3 clusters would have no valid certified operator. That puts the two enterprise contracts at risk, and your own policy would cause it.
   - It also burns the people who paid for v3. Retire a credential when support for its major ends, not when the next major ships.
3. **Copy the cloud vendors' 2–3 years and $300 full retake → partly.**
   - From memory, and unchecked: AWS and Google Cloud use roughly 2–3 years with a full retake. Microsoft role-based credentials renew through a free online assessment.
   - So "full-price retake" is not universal. Verify the numbers before quoting them internally.
   - Your 24-month validity matches their range and your support window, so I kept it.
   - The full-price retake doesn't fit your product. A yearly major means a retake would mostly re-test unchanged material. I replaced it with a cheaper delta renewal.

## Section text

### 1. Credential model

- A credential names its major: "Keldrick Certified Operator, v3".
- It is valid for **24 months from the pass date**, capped at the **end of support (EOL) of that major**.
- Minor and biweekly releases never affect validity. Release notes cover them.

### 2. States

| State | Meaning | Counts for contracts |
|---|---|---|
| Active | Within validity, major supported | Yes |
| Grace | Expired less than 90 days ago | Yes, flagged in the registry |
| Lapsed | Expired more than 90 days ago | No. Renewal via delta exam only until 12 months after expiry, then full exam |
| Retired | Major reached EOL | No. Stays on record as "v3 (retired)" |

Nobody is ever "voided".

### 3. Renewal (the normal path)

- A renewal is a **delta exam** covering changes since the holder's major. It can target any supported major.
- Candidates can renew in the 6 months before expiry. The new term starts at expiry, so early renewal costs no validity.
- A v3 holder can sit the v4 delta exam any time after v4 GA. They get a v4 credential with a fresh 24-month term.
- A holder may keep both credentials while both majors are supported.
- Price: a fraction of the full exam, set from your measured exam cost. Don't fix a number until you know the cost per sitting.
- Reminders go out at 180, 90 and 30 days before expiry, to the holder and to the account owner.

### 4. Retake (the failure path)

- A failed attempt can be retaken after a 14-day wait, at the same price as a first attempt.
- A third failure within 12 months adds a 60-day wait. Use the wait for a training pointer, not a punishment.
- A lapsed holder past the 12-month window takes the full exam.

### 5. Retirement of a major

- Dates are anchored to the major's GA date. v3 EOL is v3 GA + 24 months, so about spring 2028 if v3 shipped in spring 2026. Confirm the real date.
- At v(N+1) GA, the v(N) exam keeps selling for **6 months**, then closes. This stops people buying a credential that expires almost immediately.
- At v(N) EOL, every v(N) credential becomes Retired. Holders have had at least 12 months of overlap to take the delta.
- Publish the full retirement schedule at each GA, not at EOL.

### 6. Contract compliance

- Contracts should say "a valid credential on a supported major". They should not name a version.
- Recommend that accounts name at least two certified operators, so one lapse never breaks compliance.
- The registry offers public verification, a per-account roster, and substitution of a named operator without a contract amendment.

## Decisions for you

1. Does a v4-certified operator count for a customer still on v3? I assumed yes, since the delta covers it. If not, the overlap rules above need a per-major clause.
2. What are the real initial-exam price and per-sitting cost? Renewal pricing depends on them.
3. Is the delta exam in scope for the two-year funding? The extra cost is one delta per major plus one base exam update. I'd budget it now. Revenue from retirement cycles is what sustains the program after the funded period.
4. Is a 90-day grace period acceptable to the two enterprise customers? Check their contract wording before publishing.
# Percentage rollouts

Release a flag to a percentage of your production users. Raise the percentage over time, or turn the flag off if something goes wrong.

## Before you begin

- You need to be an Admin.
- The flag must already exist. If it doesn't, see [Creating flags](/docs/flags/creating-flags).
- Choose the environment you are rolling out in. This page assumes Production. See [Managing environments](/docs/environments/managing-environments).

These steps are the same on Tidewell Cloud and on self-hosted installations.

## Rollout options

Each option is set on the flag, in the environment you are editing.

| Option | What it does | Notes |
|---|---|---|
| Percentage | Share of users who receive the flag's "on" variation, from 0% to 100%. | Raising it only adds users. Lowering it only removes users. |
| Sticky bucketing key | The user attribute Tidewell hashes to place each user in a bucket. | Use a stable ID such as the user ID. An attribute that changes between sessions, such as a session ID, moves users in and out of the rollout. |
| Seed | A string mixed into the hash together with the bucketing key. | Keep it the same to keep the same users. Change it to reshuffle who is in the rollout. |
| Schedule | Raises the percentage automatically at the dates and times you set. | Each step sets the target percentage for its start time. |
| Kill switch | Turns the flag off for everyone in the environment immediately. | It overrides the percentage and the schedule. The percentage is kept, so you can turn the flag back on at the same level. |

## How bucketing works

Tidewell does not roll a die for each request. It combines the flag's seed with the user's bucketing key and runs the result through a hash function. The hash maps every user to a fixed position between 0 and 99.99%. The flag is on for a user when their position falls below the rollout percentage. The same user, key, and seed always give the same position, so a user sees the same variation on every request, every device, and every SDK. This holds on Cloud and self-hosted, and no state is stored per user.

This is consistent hashing in the sense that matters for rollouts. Moving the percentage from 10% to 25% moves the threshold and leaves every position where it was. Everyone in the first 10% stays in, and 15% more users join them. Nobody flips off and back on during a ramp-up. Changing the seed gives every user a new position. Do this only when you want a fresh sample, for example to run a second experiment on a different group.

## Steps

1. In the dashboard, open **Flags**, select your flag, and switch to the **Production** environment.
2. Under **Rollout**, set **Percentage** to the share of users you want, for example `10`. Change the sticky bucketing key, seed, or schedule only if you need to (see the table above).
3. Select **Save**. The change reaches your SDKs within moments.

## Learn more

- [Creating flags](/docs/flags/creating-flags)
- [Managing environments](/docs/environments/managing-environments)
- [Inviting teammates](/docs/teams/inviting-teammates)
- [Targeting rules](/docs/flags/targeting-rules)
- [Scheduling flag changes](/docs/flags/scheduling-changes)
- [Using the kill switch](/docs/flags/kill-switch)
- [Evaluating flags in your SDK](/docs/sdks/evaluating-flags)
- [Self-hosting Tidewell](/docs/self-hosted/overview)

---

Notes for you, not part of the page:
- I invented the link paths. Replace them with your real URLs.
- I assumed the details below. Check each one against the product.
  - The 0–99.99% hash range.
  - The "within moments" propagation time.
  - Kill switch keeping the percentage.
  - Lowering the percentage only removing users.
  - The dashboard labels **Rollout** and **Save**.
- I did not state a default for the bucketing key. Add one if the product has it.
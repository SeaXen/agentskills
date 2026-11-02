# Post-incident report: elevated write failures on August 3

**Status:** Resolved. **Duration:** 51 minutes. **Impact:** Write requests failed.

## Summary

On August 3, a configuration change to our request routing tier caused it to reject about 34% of write requests for 51 minutes, starting at [14:02 TZ]. Reads were not affected. [Confirm this before publishing.] We estimate about 1.2 million write requests failed. About 118 customers were affected.

We apologize. Failed writes break your applications and your trust in us, and this should not have happened.

## What happened

At [14:02 TZ], we deployed a change to the routing tier. The change touched how the tier reloads its configuration. After the reload, the tier read a value from the wrong configuration key and began failing a share of incoming writes. [One sentence on what the wrong value caused, for example misrouting to unavailable backends.]

Service returned to normal at [HH:MM TZ] after we [rolled back the change / shipped a fix].

## Impact

- **Duration:** 51 minutes.
- **Scope:** About 34% of write requests failed during the window.
- **Customers:** About 118 customers saw failed writes.
- **Volume:** About 1.2 million failed requests in total.
- **Data:** Failed writes were rejected, not partially applied. [Confirm. If any write could have been acknowledged and then lost, say so here.]

Clients that retry on errors may have recovered some writes. If you didn't retry, you may need to resend writes made during this window.

## Root cause

The routing tier's configuration reload path read the wrong key. This error was introduced by the change deployed at [14:02]. Our pre-release testing didn't exercise a configuration reload under production-like conditions, so it didn't catch the bug.

## What we are doing

1. **Reload-path tests:** [Add tests that exercise configuration reload and check which keys are read.]
2. **Staged rollout:** [Roll out routing-tier changes to a small share of traffic first, with automatic rollback on error-rate increases.]
3. **Faster detection:** [Alert on write-error rate at the routing tier. Add the detection time here: how long the problem ran before we noticed.]
4. **Config validation:** [Validate configuration on load and refuse to apply a reload that fails the check.]

We will update this page when each item ships. [Add dates or a commitment to a follow-up.]

## Questions

If you were affected and need help identifying failed writes, contact [support channel].

---

## What I changed from the internal version

- **Removed:** the engineer's name, the PROJ ticket, the change number, the `go/` wiki link, and the "two enterprise accounts" detail. Public blameless postmortems describe the system, not the person. Naming enterprise accounts risks identifying customers.
- **Kept:** the 34%, 51 minutes, 118 customers, and 1.2M requests. If legal or the account team prefers, change "about 118 customers" to "a small percentage of customers".
- **"Falcon":** I wrote "routing tier" instead. If the name is already in your public docs or status page, swap it back in.
- **Year:** I left it out. Add it if the page needs it.

## You need to fill in (the internal text didn't say)

- The timezone, the recovery time, and the fix or rollback action.
- Whether reads were unaffected, and whether any failed write could have been partially applied.
- The detection timeline, and the remediation items. The four items I listed are placeholders, not commitments from your team, so replace them with the real action items from the wiki.
- Have someone with the full postmortem check the root-cause paragraph. I only had one sentence, so I kept it deliberately thin.
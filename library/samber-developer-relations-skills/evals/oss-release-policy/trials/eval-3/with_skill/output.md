**Verdict:** I can't write "last three majors, all fixes". It costs about 5 h/month against your 3 h. Below is a policy that fits: 6.x gets all fixes, 5.x gets security fixes only for 12 months after 6.0.0, and 4.x ends when 6.0.0 ships.

## Capacity check (your numbers)

- Budget is 3 h/month. Ordinary releases take 2 × 1 h = 2 h, which leaves 1 h/month. At 2 h per backport, that is 6 backports a year across all old lines.
- **Your ask (all fixes on 4.x and 5.x):** 9 fixes × 2 lines × 2 h = 36 h/yr = 3 h/month. Total is 5 h/month, 167% of capacity.
- **Security-only on 4.x and 5.x:** 3 × 2 lines × 2 h = 12 h/yr = 1 h/month. Total is 3 h/month, 100% with zero slack. One extra advisory misses the promise.
- **Security-only on 5.x alone (recommended):** 3 × 2 h = 6 h/yr = 0.5 h/month. Total is 2.5 h/month, with 0.5 h of slack.

Two caveats:
- I used 4.x's 9 patches as the rate for every line. Backport volume may be lower than that, but the 3 security fixes a year is solid.
- The 6.0 launch itself (release candidates, migration guide) is not in these numbers. Expect November to run over.

## RELEASES.md sections

```markdown
## Supported versions

| Line | Status      | Fixes         | Supported until                                                       |
| ---- | ----------- | ------------- | --------------------------------------------------------------------- |
| 6.x  | current     | all           | while current                                                         |
| 5.x  | maintenance | security only | the earlier of 12 months after 6.0.0 and the release of 7.0.0         |
| 4.x  | unsupported | none          | ended with the release of 6.0.0                                       |
| ≤3.x | unsupported | none          | ended                                                                 |

Until 6.0.0 ships, 5.x is the current line and receives all fixes.

We keep at most one maintenance line at a time. When 7.0.0 ships, 6.x becomes
the maintenance line and 5.x ends.

Issues on unsupported lines are closed with a link to this table unless they
reproduce on a supported line.

## Backports

Only security fixes are backported, and only to the line marked maintenance. A
security fix is any issue we publish an advisory for. We do not backport bug
fixes, performance work or features.

Fix order and numbering:

- The fix lands on the current line first.
- The backport ships as a patch release on the maintenance line (for example
  5.3.2), cut from the `release-5.x` branch and published with
  `--tag release-5.x`, so `latest` always stays on the current line.
- We publish the advisory only after both lines have a patched release. It lists
  the patched version of every supported line, so update bots propose the
  backport instead of a major upgrade.

Either maintainer decides whether an issue is a security fix. If we are not
sure, we treat it as one.

A contributor may open a pull request that backports a non-security fix to the
maintenance line, with tests. We review it as time allows and do not promise to
merge or release it.
```

## Decisions for you

1. **4.x ends at 6.0.0.** Announce it now, about a month ahead, and link the 5.x to 6.x migration guide. A 3-month security-only tail for 4.x adds about 0.5 h/month while it overlaps with 5.x, which brings you to 100% again. I'd skip it.
2. **"Earlier of 12 months or 7.0.0."** This rule keeps you at one maintenance line. If you ship 7.0 less than 12 months after 6.0, 5.x users get less than a year. Drop the 7.0.0 clause only if you ship majors less than once a year.
3. **Enterprise users.** If they need all fixes on older majors or a longer window, that is a paid extended-support line. It is a monetization decision, so I left it out of the policy.

## Next steps

1. Confirm or correct the 4.x and 5.x split above.
2. Then send me the two things the other sections need: your runtime floor (the Node.js versions you support) and who holds npm publish rights.
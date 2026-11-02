**Order: F3, F2, F4, F5, F1**

| Rank | Finding | Priority | Tie-break (monthly readers) |
|---|---|---|---|
| 1 | F3: auth page embeds a live-format API key | P0 | n/a, only P0 (9,000) |
| 2 | F2: batch-ingest sample calls a renamed method | P1 | 18,000 |
| 3 | F4: C++ quickstart sample never compiled | P1 | 700 |
| 4 | F5: 210 samples with no documented expected output | P2 | 120,000 |
| 5 | F1: 61 SDK reference fences with no language identifier | P2 | 40,000 |

**How I broke the ties**
- The P-level is the severity. It fully orders F3 first, the two P1s next, and the two P2s last.
- F2/F4 and F5/F1 share a P-level, so the P-level can't separate them. I ordered each pair by monthly readers affected, since that's the only severity-related number you gave for both findings in each pair.
- I did not use fix effort. Effort affects scheduling, not severity. Using it would put F1 (2 hours) ahead of F5 (6 engineer-days) and F4 (3 engineer-weeks) ahead of nothing.

**Caveats**
- **F3:** Rotate the key first, before you edit the page. The key is exposed until it's rotated, and removing it from the page doesn't undo that.
- **F4:** It ranks above F5 and F1 only because it is P1. It's the largest effort (about 3 engineer-weeks) and has the smallest audience (700 readers). If you want it started in parallel, that is a capacity call, not a severity call.
- **F5 vs F1:** F1's fix is cheap and scripted, so someone could do it as a side task. It would still rank last on severity.
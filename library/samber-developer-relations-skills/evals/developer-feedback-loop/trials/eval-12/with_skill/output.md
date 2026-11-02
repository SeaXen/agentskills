# Ashbourne review: count sort-out

Don't rank by votes plus mentions. It adds three different units and double-counts the audit and Discord overlap. Rank blockers first, then distinct requesters. Report votes beside the requester count, never inside it. Product weighs the rest.

## Corrected counts

| Item | Wrong count | Right count | Rule |
|---|---|---|---|
| (a) Offline mode | 152 votes, "150-plus" | Votes: 152, with a note "140 of the 152 came from one newsletter link on [date]". Requesters: only people who stated a use case, about 12 at most from before the spike. | A vote spike traced to one outside link is one event, not 140 independent requesters. Votes are a separate signal. |
| (b) DX audit | 6 items, plus the Discord complaints on top | 6 records, one per friction point, type "DX friction". The advocate is a requester on each. | A DX audit becomes one record per friction point. |
| (b) the 2 that match Discord | Audit mention plus Discord mentions | One record each: the advocate plus each distinct Discord person, counted once. | Merge on the same problem. Count a requester once per record, across channels. |
| (b) the other 4 | n/a | 1 requester each (the advocate), plus anyone who confirms later. | The advocate counts as a requester. |
| (c) Multi-currency settlement | "Enterprise: 3 customers" | Segment is "prospect", not enterprise and not customers. Count 3 requesters, and the number of distinct orgs (1 to 3). The opportunity reference stays private. | Prospects from sales calls get the segment "prospect". The AE's label would erase that mix. |

The AE's "3 customers" is the one to push back on. These are prospects who haven't bought. If the three are people at the same company, that is 3 people and 1 org.

## What I can't count yet

- **Offline mode:** I don't know how many of the 12 pre-spike votes came with a use case. I don't know if offline mode is a blocker for anyone.
- **The two Discord matches:** I don't have the number of distinct people.
- **Multi-currency:** I don't know if it is a blocker for those deals. I also don't know if it is a problem or a solution. "Multi-currency settlement" is a solution. Ask each prospect "what were you trying to do when you needed this?" and title the record with the problem.

## Agenda order

1. **Blockers first.** Check severity on every record. A blocker with no workaround goes above anything popular. Multi-currency may qualify if it blocks those three deals.
2. **Then distinct requesters.** Show these columns beside each record: requesters, orgs, segment mix, severity, workaround, and the vote count with the spike noted.
3. **Show private account value and prospect opportunity value beside each record, not folded into a score.** Product decides how to weigh them.

On the figures you have, offline mode is not clearly first. Its real requester count is probably far below 150. The two Discord-matched DX records and multi-currency may rank at or above it.

## Next actions

1. Reply in the offline mode thread asking voters "what were you trying to do when you needed this?" The answers turn the spike into counted requesters.
2. Pull the distinct Discord people behind the two matching friction points and merge them into the audit records.
3. Ask the AE for the three prospects' names, orgs and the deal impact. Log them as segment "prospect".
4. Label each record's severity (blocker, slows down, cosmetic) per requester.
5. Send me the counts from steps 1 to 4 and I'll finalize the agenda order.

I applied the counting and merging rules from the skill (Step 4 and the weighting worksheet). I didn't run the full interview, the leak trace or the contract steps, since you asked only to sort out the counts. If this is a one-off pile, cluster it into problems and log only the largest clusters before the review, up to what the review can decide.
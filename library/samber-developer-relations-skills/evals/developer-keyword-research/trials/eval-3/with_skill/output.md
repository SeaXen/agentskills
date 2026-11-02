# Keyword map: Corvid Cache — post-4.2 error-entry targets

Scope of this run: two ticket-subject clusters plus matching telemetry, supplied directly by the requester (no interview needed — this matches the "turn tickets into troubleshooting targets" pattern, error family only).

## Scope

**Axes.** Client languages: Go, Java. Deployment: self-hosted cluster, nodes addressed as `corvid://<host>:7946`, token-based auth between client and node. Version: 4.2 (shipped "the 3rd"); prior version(s) still in the field, since one of the two clusters is not version-specific.

**Adoption mode.** Not stated. Both clusters are things an operator/developer hits directly while running the client (a connection failure, an auth failure) — individual/operator adoption, not a company-adoption signal. Proceeding without asking, per the request's own framing ("turn this into doc page targets").

**Owned surfaces.** Not stated; assuming a docs site is the intended target since that's what was asked for. Confirm ownership of a changelog/status surface too — one recommendation below belongs there, not on a keyword-targeted page.

**Sources used** (both covering the same ~2-week window, User-provided — counts came from the requester's message, not from a pull I ran myself):
- Tier 3, support-ticket subjects: 31 connection-refused, 24 token-expired.
- Tier 4, product error telemetry: 812 refused events, 1,140 auth-expired events.

**Sources unavailable this cycle** (tier 1 search-console query data, tier 2 docs-search logs, a raw issue-tracker export beyond the given subjects, tier 5 Q&A, tier 6 ecosystem counters, tier 7 autocomplete, tier 8 keyword tools) — mark N/A, don't guess. This is why the map below is one ranked cluster, not a full quarter's set: only two subject groups were supplied. Pull tiers 1–2 next to confirm whether an error entry already ranks, and to surface reference-lookup/how-to candidates for the Go and Java clients that this pull has no evidence for.

**70% floor.** Met trivially (1 of 1 ranked cluster draws top evidence from tiers 3–4 = 100%), but flagged as thin evidence breadth rather than a strong pass — re-run with a fuller export before treating this as the complete cycle.

**Timeline read (inferred, not measured):** 31 refused tickets spread evenly across both weeks while 24 auth tickets are 100% dated after the 3rd only makes sense if the release sits at the week-1/week-2 boundary. Treating week 1 as pre-4.2 and week 2 as post-4.2 for this analysis; flag if the actual boundary differs.

## Ranked clusters

Sorted by outcome per page-hour, highest first. Only one cluster clears the evidence gate this cycle — the other named pattern is refused below rather than ranked, per the workflow's own instruction not to score an unwinnable category low.

| Cluster | Primary query | Variants | Family | Evidence (source, count, date) | Incumbent | Target surface | Existing URL or "new" | Priority |
|---|---|---|---|---|---|---|---|---|
| Connection refused reaching a Corvid node (port 7946) | `connection to corvid://<node>:7946 refused after 20s` | `dial tcp <ip>:7946: connect: connection refused` (Go); `CorvidConnectionException: caused by java.net.ConnectException: Connection refused` (Java); "go client cannot reach cluster, connection refused"; "cache unreachable in staging, connection refused" | Error string | 31 tickets / 2wk, evenly split across both weeks — i.e. not release-tied (User-provided); 812 error-telemetry events / same window (User-provided) | Not verified — no first-party ranking data supplied this cycle; treat as an unconfirmed gap, don't publish "new" until checked | Error entry | Unknown — verify before publishing | P1 |

Why P1 despite thin evidence breadth: error-string family is the cheapest to write (the fix is already implicit in the tickets), the pattern is steady-state rather than release-driven (worth writing once, keeps paying off), and it spans both client languages plus prod/staging/EU — one page, several environments.

**What the page needs for completeness** (the four things that win a technical query, per the winnability check): exact string reproduced for both Go and Java, note the client's own ~20s connect timeout as a documented default rather than a mystery number, and cover the distinct failure conditions separately rather than one generic "check your network" line — node down/crashed, security-group or firewall not open for 7946 in both directions, DNS/hostname not resolving, wrong cluster address, and (called out separately, since `cache-eu-2` is the only cross-region example given) cross-region VPC peering/firewall rules as their own subsection. Ship one page with Go/Java tabs rather than two pages — the root cause and remediation are infrastructure-level, not language-level; only the pasted error text differs.

## Company-adoption set

Not populated this cycle. No evaluation, comparison, migration, or integration evidence — and no sales/solutions-engineering question log — was supplied. This pull is scoped to two support/telemetry-sourced error clusters only; ask sales/SE for their question list before the next cycle so this section isn't silently empty again.

## Fix first

Cannibalization/update-vs-create screening (step 2) couldn't run — no docs-site search data or search-console export was available. Before shipping the connection-refused page as "new," check for an existing FAQ/troubleshooting entry mentioning "connection refused" or port 7946; if one exists, fold the normalized variants above into it rather than creating a second page competing for the same query.

## Do not target

- **Token expired after upgrading to 4.2** — `auth failed: token expired for node <node>`, `CorvidAuthException: credential rejected, token expired`, "node rejects our client: token expired since upgrade to 4.2", "token expired errors started after 4.2 rollout" (24 tickets, 100% dated after the 3rd; 1,140 telemetry events over the same window — the single largest count in this pull, despite fewer tickets than the refused cluster, meaning it under-reports relative to its true frequency). **Refused as a docs target**: a cluster that appears only after a release is a regression signal to route to engineering, not a knowledge gap — the real fix is a product change or a corrected error message, and a doc page here would either paper over a bug or go stale the moment it's patched. Recommend flagging to engineering as a P0 investigation given the telemetry volume and that it's an auth path.

## Backlog

- **"Reissue/rotate tokens after upgrading to Corvid 4.2"** (migration entry, contingent) — parked, not written. Promote only if engineering confirms 4.2 intentionally changed token TTL/rotation and the fix is a documented customer action, not a bug; drop entirely if it's confirmed a defect fixed in a patch release. Parked as of this pull (window: two weeks following the 4.2 release on the 3rd).

---

**Pass threshold check.** (1) The one ranked cluster carries sourced, dated, labeled evidence — pass. (2) 100% of ranked clusters draw top evidence from tiers 1–4 — pass, though on a sample of one. (3) Nothing is ranked on tool volume — pass, no tool volume was used. (4) One cluster, one canonical target, no collision — pass. (5) Do-not-target is non-empty — pass. (6) Sort is stated above the table; nothing was demoted by the ratio since there's only one ranked row, and the company-adoption set is explicitly marked unfilled rather than silently empty — pass. Net: passes on the narrow question asked, but the map itself is intentionally thin — it covers exactly the two subject groups supplied, not a full quarter's demand.
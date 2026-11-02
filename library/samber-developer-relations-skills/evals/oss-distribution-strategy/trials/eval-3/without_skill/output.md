## Distribution plan: probe-lens

Biggest lever first: **publish to Open VSX registry.** Cursor, Windsurf, VSCodium, Trae, Gitpod, code-server all pull extensions from Open VSX, not Microsoft's VS Code Marketplace — Microsoft's marketplace terms forbid other editors from using it. If probe-lens sits only on the VS Code Marketplace, every Cursor user hits a wall: search finds nothing, install fails silently. That is near-certainly what those issue-tracker mentions are. One registry, invisible to a whole segment, for 7 months.

(Verify this still holds — open Cursor's extension panel, search probe-lens, confirm it's absent. Editor extension-sourcing policies shift; I can't check live from here.)

### Month 1 — unlock (~7h combined)

1. Create Eclipse Foundation account, claim your publisher namespace, generate a PAT. (30 min)
2. `npx ovsx publish -p <token>` from your extension root. Confirm it shows up on open-vsx.org and inside Cursor's extension panel. (1h)
3. Add `ovsx publish` as a step in your existing release CI, alongside `vsce publish`, so every future release auto-dual-publishes. One-time cost, removes this forever. (1h)
4. Reply to every open issue mentioning Cursor/Windsurf/"can't install" with the fix. Close the loop, thank them, ask them to try again. (1h)
5. Marketplace listing polish: tighten description with real search terms (opentelemetry, otel, tracing, spans, distributed tracing, observability), set 5-10 relevant tags/categories, refresh the README GIF to show spans rendering inline. Ratings and search-relevance both weigh this. (2h)
6. DM or email 10-15 known happy users (GitHub stargazers, closed issues with thanks) asking for a marketplace review. Few ratings on a 7-month-old extension is itself suppressing search rank. (1h)

### Month 2 — compounding assets (~6h)

1. One real post: "Visualizing OpenTelemetry spans inline in your editor" — the problem, a before/after GIF, a 5-line quick start. Publish on your own blog, cross-post to dev.to. This one asset feeds everything below. (3h)
2. PR probe-lens into `awesome-vscode`, `awesome-opentelemetry`, `awesome-observability`. Durable discovery surface, near-zero maintenance after merge. (1h)
3. Share the post in 2-3 places your actual users already are: CNCF Slack observability channel, r/opentelemetry, r/vscode. Mention the Cursor/Open VSX fix by name — the people who hit that wall will recognize themselves. (1h)
4. Email 1-2 complementary (non-competing) OTel backend projects — Honeycomb, Grafana, SigNoz, Uptrace — pitching probe-lens as an editor-side companion to their backend. Ask for a doc mention or blog cross-link, not a partnership deck. (1h)

### Month 3 — ship, then check the signal (~flexible)

1. Ship one fix/feature that's a recurring issue-tracker request. Write a 4-line changelog post, publish as a GitHub Release, share in the same 2-3 communities from Month 2. Consistency beats a one-time spike. (~1h on top of the dev work itself)
2. Pull VS Code Marketplace install stats and Open VSX download stats separately — they don't share a dashboard. Compare against what you posted that month. Let that steer Month 4, not gut feel. (30 min)
3. Stretch, optional, skip if tight: one CFP submission to an observability or DevRel meetup. Only if 1-2 does it.

### Skip this on purpose (8h/month has no room for it)

1. Paid ads — no CAC data, no budget to learn on.
2. A Discord/community platform — two people can't moderate it.
3. Product Hunt relaunch — already launched, marginal return now.
4. A content calendar across many platforms — pick GitHub + one content surface, not five.
5. Programmatic SEO pages — payoff horizon too long for this team size.

### Standing habit, no extra hours

Treat every issue mentioning "Cursor," "Windsurf," or "can't install" as your top-priority reply. These are already-convinced users blocked by one missing registry — highest intent traffic you have, and now (post Month 1) an easy fix to point them at.

### Next action

Create the Eclipse Foundation account and claim your namespace at open-vsx.org — 30 minutes, unblocks everything else in Month 1.
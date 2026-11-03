# Systor Speed page patterns

Use this when polishing a speed-test page inside a dark, compact dashboard UI.

## User preference signals from this session
- Keep the main Speed page simple and native-looking.
- Avoid mixed-provider clutter in the primary UI.
- Do not embed bright/white third-party blocks that clash with the app shell.
- Prefer official Ookla CLI for the primary WAN test path.
- If cross-region server presets are not guaranteed by the live host-discovered Ookla list, label them honestly as fixed-ID / experimental instead of implying reliability.

## UI patterns that worked
- Add one-click region preset buttons above the main content for the common locations the user asked for.
- Keep the actual server select as the source of truth; preset buttons should only set/select a server ID.
- Style scheduler inputs explicitly. Native browser inputs in dark dashboards default to white backgrounds and break visual consistency.
- For speed-test runs, add a native themed live runner surface:
  - phase label (`ping`, `download`, `upload`, `complete` / `failed`)
  - animated center ring / gauge
  - live DL + UL readouts
  - DL/UL progress bars
- Preserve a separate current-result panel and history table/chart; do not overload the page with too many test modes.

## Provider/selection pitfall
- Official Ookla CLI may only live-discover nearby servers from the current host/IP.
- Public or historical Speedtest server IDs from third-party lists can fail with `NoServersException` even if the ID looks valid.
- Therefore:
  1. Keep live-discovered local servers as the default/reliable path.
  2. Mark foreign fixed-ID presets as best-effort or experimental.
  3. If the user wants truly reliable multi-country presets, build a verified registry by testing candidate IDs from the exact host and keep only passing IDs.

## Product/UX direction taken here
- Keep scheduler/settings inline, compact, and app-themed.
- Avoid pretending that every provider can offer the same metrics or the same kind of server selection.
- Prefer honest caveats in small helper text over fake parity.

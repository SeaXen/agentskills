# Local Web Service Port Inspection (5-step recipe)

Use when the user says "check X on port Y", "what's on port N", "is service X running", or "show me dashboard Y". Verified against SeaDash on `:9090`, but applies to any locally-served web UI.

## When to use

- "I have a dashboard / service on port N, check it"
- "Is SeaDash / CasaOS / Homepage / N8N up?"
- "What's running on :NNNN?"
- "Show me what's on this dashboard" (port already known)

## The 5-step sequence

### 1. Identify listener + PID

```bash
ss -tlnp 2>/dev/null | grep ":9090" || netstat -tlnp 2>/dev/null | grep ":9090"
```

- Confirms the port is actually bound (not just firewall-open or route-forwarded).
- Gives the PID, which lets you locate the binary/script via `/proc/<pid>/exe` or `systemctl status`.

### 2. Get service unit metadata

```bash
systemctl show seadash --no-pager 2>/dev/null | grep -E "ExecStart|WorkingDirectory|User|Environment|FragmentPath"
```

- `ExecStart` -> exact script path (often the source of truth beats the readme).
- `WorkingDirectory` -> real source root.
- `FragmentPath` -> service unit location (e.g. `/etc/systemd/system/seadash.service`).
- If no systemd unit, fall back to `ps -fp <PID>` + `cat /proc/<PID>/cmdline`.

### 3. Probe HTTP

```bash
curl -sS -o /tmp/svc.html -w "HTTP %{http_code} | %{size_download} bytes | %{time_total}s\n" http://localhost:9090/
```

- Always redirect to a file when the page is >16KB; piping to `head` causes `curl: (23) Failure writing output to destination, passed 16384 returned 4096` once head closes early.
- After downloading, inspect first ~100 lines for: `<title>`, theme color (`<meta name="theme-color">`), manifest link, and any PWA markers.
- For SPA pages, the title and theme color are often the cheapest signal of which service this actually is.

### 4. Get interactive snapshot

```python
browser_navigate(url="http://localhost:9090/")
```

- Returns a compact accessibility tree with ref IDs (`@e1`, `@e2`, ...) for buttons, textboxes, and clickable generics.
- Use this for: button labels, search boxes, view-mode toggles, action clusters.
- The accessibility tree is often more useful than a screenshot for "what can I do here".

### 5. Enumerate visible elements / cards

```python
browser_vision(question="Describe what apps/services are shown as cards/tiles. List each card, its port/URL, and any status indicator colors (green=up, red=down, amber=warning).")
```

- Use this for: app inventory tables, status color interpretation, alert banner text, header KPI strip.
- Screenshot path is returned in the response -- include it as `MEDIA:<path>` in the user reply so they can see it.
- For "10/10" claims on a dashboard, the visual is the proof -- text snapshots miss color-coded status.

## Output format the user expects

When reporting inspection results, structure as:

1. **Service** -- service unit, PID, bind, public URL + local URL
2. **System snapshot** (if visible) -- load, RAM, disk, container count, temp
3. **Active alerts** (if visible) -- count + breakdown
4. **App inventory** -- table with name / port / URL / status
5. **Caveats** -- orphans, duplicates, exposed endpoints, anything that smells wrong

Plus the screenshot attached as `MEDIA:/root/.hermes/cache/screenshots/browser_screenshot_*.png`.

## Common pitfalls

- **`curl | head` fails on large pages.** Always `-o /tmp/file` first, then read with `read_file` or `head /tmp/file`.
- **`find / -name "*.py" -path "*seadash*"` often times out at 60s.** Narrow with `-path` or use the `WorkingDirectory` from step 2 to search that specific tree.
- **Multiple processes on the same port across reboots.** Always check the PID is the live one, not a leftover from a previous install. The PID in `ss -tlnp` is authoritative.
- **"Samefile" trap.** On this host, `/root/.hermes/...` and `/mnt/tb/hermes/...` can be the same live directory. When reporting paths, prefer the canonical one (`/root/.hermes/...`) unless the user references the `/mnt/` path explicitly.
- **Status-color interpretation is fuzzy.** Browser vision can see green/red/amber left borders, but a missing border is ambiguous (could be down, unmonitored, or just unstyled). Don't claim a service is "down" from a missing border alone -- verify with a direct `curl -o /dev/null -w "%{http_code}"` probe to the service's port.
- **PWA / single-page apps.** The `index.html` may be small but the actual UI is in JS bundles. The interactive snapshot from `browser_navigate` is more honest than the raw HTML in that case.

## Cross-references

- `references/hermes-telemetry-dashboard-token-panels.md` -- same inspection pattern applied to `:8009`.
- `references/dashboard-connected-platforms-env-mismatch.md` -- what to do when `/api/status` lies about platform connectivity.
- `references/hermes-bitwarden-custom-providers.md` -- for cases where the inspected service is a custom OpenAI-compatible provider.

# Public read-only dashboard and storage mount pitfalls

## When to apply

Use this pattern when a self-hosted dashboard has to be safely exposed through Cloudflare Tunnel / reverse proxy while LAN or Tailscale users still need full admin controls.

## Public hardening pattern

Goal: **public users get a read-only dashboard only**.

### Route gating

At request-entry, branch on client trust (`client_private` / local-LAN-Tailscale detection).

For **public** clients:
- allow only `/`
- allow only minimal read-only APIs needed by the public dashboard
- return `404` for private/admin HTML pages so they disappear from navigation discovery
- return `403` for sensitive APIs so admin actions and introspection are blocked even if called directly

Typical public `404` pages:
- `/apps`
- `/network`
- `/speed`
- `/alerts`
- `/logs`
- `/settings`
- `/storage`

Typical public `403` APIs:
- `/api/system`
- `/api/runtime`
- `/api/access`
- `/api/notifications`
- `/api/top-processes`
- `/api/apps`
- restart / save / storage / settings APIs

### Template/UI gating

Do not rely on backend blocking alone.

Also hide from public:
- non-dashboard navigation tabs
- restart buttons
- save/apply buttons
- process tables
- recent alerts if they reveal operational detail

Browser-verify the public surface after backend changes. The expected public navigation is often just:
- `Dashboard`

## Public performance pattern

If the public dashboard needs several charts, do **not** make the browser fetch many separate series endpoints over Cloudflare.

Instead add one bundled read-only endpoint, e.g. `/api/public-dashboard`, that returns:
- current snapshot
- all chart series needed for the current page
- network series if needed

Why:
- fewer RTTs through tunnel/proxy
- less client-side coordination
- fewer opportunities for mixed public/private API mistakes

Public page JS should use the bundled endpoint and should **not** continue polling private APIs in shared base/header code.

## Storage/mount pitfall

Do not auto-enumerate arbitrary mounts into a public or operator file-manager surface on boxes that have:
- `autofs`
- `fuse`
- `rclone`
- cloud-drive mounts

`shutil.disk_usage()` and similar filesystem probes can block indefinitely on hung autofs/FUSE targets.

### Safer pattern

- keep the visible root list small and explicit when the box has problematic mounts
- wrap disk-usage probes in a bounded timeout path
- if a mount probe times out, return `unavailable: true` instead of hanging the whole request

For this user’s Systor case, the durable safe root choice was:
- `/`
- `/mnt/tb`
- `/root`

while excluding autofs/FUSE-discovered mounts from the UI.

## Apps/process performance lesson

If `/api/apps` or equivalent process inventory is expensive:
- do not compute it fresh on every request
- keep a short-lived cache
- pre-warm/refresh that cache in a background thread or collector pass

A 2-second cold process inventory makes page navigation feel broken even if the rest of the app is fast.

## Release-claim rule

Do not call a dashboard "10/10", "bug-free", or "public-ready" without both:
- LAN verification
- public-tunnel verification

For public-readiness specifically verify:
- public HTML route matrix
- public API allow/block matrix
- hidden admin controls in the browser
- no console errors on the public page

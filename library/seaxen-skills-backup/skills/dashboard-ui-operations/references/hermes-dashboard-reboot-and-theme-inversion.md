# Hermes dashboard reboot service + theme inversion pitfalls

## Reboot service diagnostic pattern

Check the managed service, not only a one-shot dashboard command:

```bash
systemctl is-enabled hermes-dashboard.service
systemctl is-active hermes-dashboard.service
systemctl status hermes-dashboard.service --no-pager -l
journalctl -u hermes-dashboard.service -n 80 --no-pager
```

```bash
```

Interpretation:
- `enabled` + `active` means it should start after reboot and is currently running.
- `enabled` + `activating (auto-restart)` means systemd will try after reboot but the command is crash-looping.
- `connection refused` on the port with an enabled service usually means the service process exits before binding.

## Dashboard CLI flag drift

Always verify live CLI help before putting flags into a service unit:

```bash
hermes dashboard --help
```

Observed durable failure shape:
- service unit used `hermes dashboard ... --tui --skip-build --no-open`
- installed Hermes dashboard CLI did not accept dashboard-local `--tui`
- journal showed `hermes: error: unrecognized arguments: --tui`
- port `9120` never bound after reboot

Repair shape:
1. edit the service unit to remove the unsupported flag
2. reload systemd
3. restart service
4. verify listener and HTTP 200 from both localhost and LAN IP

Example fixed service command:

```ini
ExecStart=/usr/local/bin/hermes dashboard --host 0.0.0.0 --port 9120 --insecure --skip-build --no-open
```

Then:

```bash
systemctl daemon-reload
systemctl restart hermes-dashboard.service
ss -ltnp | grep ':9120'
curl -I http://127.0.0.1:9120/
```

## Custom theme looks light when it should be dark

Hermes dashboard themes can use a foreground `difference` inversion layer. A custom dark theme may become light if its palette sets foreground alpha to `1`.

Example bad-for-dark shape:

```yaml
palette:
  background:
    hex: "#0A0E1A"
    alpha: 1
  midground:
    hex: "#E6EAF2"
    alpha: 1
  foreground:
    hex: "#E6EAF2"
    alpha: 1
```

For a normal dark theme, set foreground alpha to `0` so the inversion layer is transparent:

```yaml
foreground:
  hex: "#E6EAF2"
  alpha: 0
```

Browser verification:

```js
(() => {
  const cs = getComputedStyle(document.documentElement);
  return {
    theme: localStorage.getItem('hermes-dashboard-theme'),
    foreground: cs.getPropertyValue('--foreground'),
    foregroundAlpha: cs.getPropertyValue('--foreground-alpha'),
    backgroundBase: cs.getPropertyValue('--background-base'),
    midgroundBase: cs.getPropertyValue('--midground-base'),
  };
})()
```

Expected for a dark Reflect-like theme:
- active theme is the custom theme name
- `--foreground-alpha` is `0`
- `--background-base` is the dark navy/black value
- live browser screenshot/vision shows dark navy surfaces, not pale inverted panels

## Reporting shape

Tell the user separately:
- whether the service is enabled for reboot
- whether it is active now
- what port/IP returned HTTP 200
- what exact theme value caused the visual inversion

Do not say “auto-start is fixed” unless `is-enabled`, `is-active`, listener, and HTTP probe all agree.

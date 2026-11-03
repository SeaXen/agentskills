# Cloudflare Tunnel + ttyd blank terminal triage

## Symptom
- ttyd exposed on LAN/Tailscale works enough to connect
- same ttyd origin exposed via Cloudflare Tunnel appears blank or "shows nothing"
- user suspects tunnel/websocket problem

## Durable diagnostic pattern
Treat these as separate checks:
1. **Origin port responds** — `curl` the local ttyd port and confirm the HTML shell returns `200`
2. **Tunnel serves the hostname** — confirm the public hostname returns the ttyd page
3. **Browser websocket opens** — inspect browser console for ttyd websocket-open messages
4. **Backend PTY command renders output** — visually confirm the terminal shows a prompt/banner, not just a blank canvas

Do not stop at step 3. HTML + websocket success does **not** prove the launched command is usable.

## Case lesson
In this session:
- Cloudflare Tunnel config for `tty.xuup.top` correctly pointed to `http://192.168.0.222:2222`
- Cloudflare tunnel status was healthy
- browser console showed ttyd websocket connections opening successfully
- ttyd logs showed `/ws` connections and child processes starting
- but the terminal canvas stayed blank

Root cause: ttyd was launching `login` (`START_COMMAND=login`) via the `cp0204/ttydbridge` wrapper. The tunnel path was fine; the command behind ttyd was not rendering a usable session.

Proof pattern that isolated it:
- start a temporary ttyd instance on another port with a known-good shell command, for example:

```bash
/opt/ttyd -p 2233 -W bash -lc 'echo READY_FROM_TEST; exec bash -l'
```

- open that temporary port in a browser
- if it renders prompt/output normally, the ttyd binary and websocket path are healthy
- then the original command (`login`) is the fault surface, not Cloudflare Tunnel

## Fix shape
Prefer a direct shell command for ttyd:
- `bash -l`
- or `sh -l`

Avoid using `login` as the ttyd command unless you have a specific reason and have verified it renders correctly in this PTY/browser context.

## Reporting rule
Say this precisely:
- **Tunnel is healthy** if HTML and websocket reach the origin successfully
- **Terminal command is broken** if the page stays blank but an alternate shell command on the same ttyd path renders normally

Do not collapse those into a vague "Cloudflare not working" diagnosis.

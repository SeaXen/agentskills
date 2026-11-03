# Gateway restart TEMPFAIL + Gemini doctor false-alarm notes

Two practical troubleshooting lessons from a live NAS/DietPi Hermes deployment.

## 1) `hermes gateway restart` can leave the service down with `status=75/TEMPFAIL`

Observed pattern:
- `hermes gateway restart` reported success (`✓ User service restarted`)
- immediately after, `hermes gateway status` showed the unit in `activating (auto-restart)` or stopped
- `journalctl --user -u hermes-gateway` showed:
  - `Gateway restart requested`
  - `Main process exited, code=exited, status=75/TEMPFAIL`
  - interrupted long-running provider activity / heavy context compression

Context that made this more likely:
- the old gateway process was still inside a long provider call
- the active session had very large context (`~214k tokens`) and repeated preflight compression
- the restart signal interrupted work mid-flight

Reliable recovery:
```bash
hermes gateway status
systemctl --user reset-failed hermes-gateway
systemctl --user start hermes-gateway
journalctl --user -u hermes-gateway -n 80 --no-pager
```

Verification cues:
- `Active: active (running)` in `hermes gateway status`
- platform logs such as:
  - `Connecting to telegram...`
  - `Connected to Telegram (polling mode)`
  - `✓ telegram connected`

Do not stop at "restart requested" — verify the post-restart unit state.

## 2) `hermes doctor` may report Gemini `invalid API key` even when the key is valid

Observed pattern:
- `hermes doctor` showed:
  - `gemini (invalid API key)`
  - recommendation to check `GOOGLE_API_KEY`
- but the live environment had both `GOOGLE_API_KEY` and `GEMINI_API_KEY` set in the active `.env`
- direct API probe against Google's Gemini endpoint succeeded and returned model listings

Verification recipe:
```bash
hermes config path
hermes config env-path
python3 - <<'PY'
from pathlib import Path
import urllib.parse, urllib.request, json
p = Path('/mnt/tb/hermes/.env')
key = None
for line in p.read_text().splitlines():
    if line.startswith('GOOGLE_API_KEY='):
        key = line.split('=', 1)[1].strip(); break
url = 'https://generativelanguage.googleapis.com/v1beta/models?key=' + urllib.parse.quote(key)
with urllib.request.urlopen(url, timeout=15) as r:
    data = json.loads(r.read().decode())
print({'models_count': len(data.get('models', [])), 'first_model': (data.get('models') or [{}])[0].get('name')})
PY
```

Interpretation:
- if the direct probe succeeds, the key itself is valid
- treat the doctor output as a false alarm or codepath mismatch unless another failing Gemini call proves otherwise
- when Telegram/Discord also show intermittent DNS or connection errors, prefer the network explanation over key rotation

## Related network clue

In the same environment, gateway logs showed intermittent DNS failures such as:
- `Temporary failure in name resolution`
- Telegram reconnect timeouts
- Discord websocket DNS failures

So an auth-looking symptom may really be a host network stability issue.
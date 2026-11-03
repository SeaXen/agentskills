# Port Conflict Behavior — run.sh Auto-increment Logic

Source: `/root/.hermes/products/hermes-personal-dashboard/run.sh` lines 327-396

## Behavior

1. **Default port**: 9120 (hardcoded in `PORT="9120"`)
2. **Port check**: `port_available()` uses Python socket bind test
3. **On conflict**: If `STRICT_PORT=0` (default), `choose_port()` increments by 1 up to +20
4. **Output**: Prints "Port 9120 is busy; using 9121." to stdout
5. **No warning** if the busy port is left untouched (by design)

## Code Flow

```bash
choose_port() {
  candidate=$PORT
  limit=$((PORT + 20))
  while ! port_available "$HOST" "$candidate"; do
    owner=$(port_owner "$candidate")
    if [ "$STRICT_PORT" -eq 1 ]; then
      exit 1  # fail fast
    fi
    if [ "$candidate" = "$PORT" ]; then
      echo "Port $candidate is busy ($owner); leaving it untouched and looking for next free port."
    fi
    candidate=$((candidate + 1))
    [ "$candidate" -gt "$limit" ] && exit 1
  done
  [ "$candidate" != "$PORT" ] && echo "Port $PORT is busy; using $candidate."
  PORT=$candidate
}
```

## Implications

| Scenario | Result |
|----------|--------|
| Main Hermes on 9120, install personal dashboard default | Personal dashboard gets **9121** |
| Personal dashboard on 9121, install another product default | Next product gets **9122** |
| `systemctl restart` after port change | Uses **new port** (PID file tracks old) |
| Explicit `--port 9122` given | Uses 9122 or fails if `STRICT_PORT=1` |

## Best Practice

**Always specify `--port <PORT>` explicitly** in:
- `install.sh --port <PORT>`
- `run.sh --port <PORT>`
- systemd `ExecStart` line

Never rely on default 9120 when multiple Hermes services run on same host.

## Port Owner Detection

`port_owner()` uses `lsof` or `ss`:
```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN | awk 'NR==2 {print $1 " pid " $2}'
# or
ss -ltnp "sport = :<port>" | awk 'NR==2 {print $0}'
```

Used only for informational message; doesn't kill the owner.
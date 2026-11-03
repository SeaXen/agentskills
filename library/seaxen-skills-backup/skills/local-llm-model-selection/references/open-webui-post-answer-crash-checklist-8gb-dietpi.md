# Open WebUI post-answer "crash" checklist on 8 GB DietPi + Ollama

Condensed findings from a live troubleshooting session where the user reported that the local LLM seemed to crash in Open WebUI after completing an answer.

## What was verified live

- `open-webui` container was still up and healthy
- container restart count was `0`
- `ollama.service` was still active/running
- `systemctl show ollama -p NRestarts,...` showed `NRestarts=0`
- current-boot `dmesg` / kernel journal showed no `OOM`, `Killed process`, or `segfault`
- Open WebUI container memory usage was low (~214 MiB at check time)
- Open WebUI SQLite history showed completed assistant messages with `done=1` and `error=null`

Practical takeaway:
- on this hardware, a user-perceived "crash after answer" may actually be a heavy-model memory/runner-eviction problem rather than Open WebUI itself dying

## Useful live checks

### Verify Open WebUI did not actually restart
```bash
docker inspect open-webui --format 'RestartCount={{.RestartCount}} StartedAt={{.State.StartedAt}} FinishedAt={{.State.FinishedAt}} Health={{if .State.Health}}{{.State.Health.Status}}{{end}}'
docker logs --tail 200 open-webui 2>&1
```

### Verify Ollama did not actually restart
```bash
systemctl --no-pager --full status ollama
systemctl show ollama -p NRestarts,ExecMainStatus,ExecMainCode,ActiveEnterTimestamp,ActiveState,SubState
journalctl --no-pager -u ollama -n 200
```

### Check for kernel-level memory kills
```bash
dmesg -T | egrep -i 'killed process|out of memory|oom|segfault|ollama|open-webui' | tail -n 120
journalctl --no-pager -k --since '24 hours ago' | egrep -i 'out of memory|oom|killed process|segfault|ollama|docker'
```

### Check whether Open WebUI actually marked the response complete
Open WebUI data mount in this setup:
- `/mnt/tb/1Apps/open-webui-data/webui.db`

Python probe example:
```python
import sqlite3, json
conn = sqlite3.connect('/mnt/tb/1Apps/open-webui-data/webui.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("""
SELECT chat_id, role, model_id, done, created_at, updated_at,
       substr(CAST(content AS TEXT),1,120) as content,
       substr(CAST(error AS TEXT),1,200) as error,
       substr(CAST(usage AS TEXT),1,200) as usage
FROM chat_message
ORDER BY updated_at DESC
LIMIT 20
""")
print(json.dumps([dict(r) for r in cur.fetchall()], indent=2, default=str))
```

If recent assistant rows show:
- `done = 1`
- `error = null`

then the backend completed normally even if the user perceived a crash/hang immediately after.

## Memory-fit findings from this machine

### `llama3.2:3b`
- completed successfully in direct Ollama test
- runner RSS after load was about **2.5 GB**
- safer day-to-day choice on this machine

### `qwen3.5:2b`
- also completed successfully
- much heavier in live Ollama logs than the name suggests
- Ollama reported total memory around **3.8 GiB** with:
  - weights ~`3.0 GiB`
  - KV cache ~`529.6 MiB`
  - compute graph ~`260.1 MiB`
- direct process RSS after load was about **3.9 GB**

### `gemma4:e2b` / `gemma4:e4b`
- should be treated as poor fits for steady Open WebUI usage on this hardware class

## Important interpretation

A symptom like "it crashes after the answer completes" can happen when:
1. the answer itself finishes
2. Open WebUI records the message successfully
3. Ollama then keeps or reloads a heavy runner
4. memory pressure spikes during/after completion
5. the user experiences freeze, delay, or model disappearance and interprets it as a crash

## Safer configuration direction

For this hardware class:
- prefer `llama3.2:3b`
- use `phi4-mini` or `qwen2.5-coder:3b` selectively
- treat `qwen3.5:2b` as heavier than expected
- avoid `gemma4:*` for routine Open WebUI use
- reduce Ollama context length from `4096` to `2048` when stability matters more than long context
- optionally shorten `OLLAMA_KEEP_ALIVE` so memory is released sooner after replies

## Environment detail from the live session

Ollama service file at the time of investigation:
- `/etc/systemd/system/ollama.service`
- only custom environment line was PATH
- no explicit `OLLAMA_CONTEXT_LENGTH` override was set yet

Ollama runtime reported:
- `OLLAMA_NUM_PARALLEL=1`
- default context `4096`
- CPU-only inference on a machine with total memory ~`7.7 GiB`

## Pitfall

Do not diagnose this class of issue from the user's wording alone. On low-RAM laptops, "Open WebUI crashes after the answer" often means:
- no container restart
- no Ollama service restart
- no kernel OOM log in the current boot
- just a model that is too heavy or too sticky for the available RAM budget.

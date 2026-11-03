# Ollama + Open WebUI uninstall cleanup after custom HDD offload

Use this when Ollama/Open WebUI are being removed from a machine that previously used custom storage paths.

## Why this matters

Removing `ollama.service`, `/usr/local/bin/ollama`, or the default `/usr/share/ollama` tree is not enough if models were previously offloaded to another disk.

A real cleanup found a leftover HDD model store at:
- `/mnt/tb/ollama` — about 22G, containing Ollama `blobs/` and `manifests/`

Open WebUI also had a bind-mounted data directory at:
- `/mnt/tb/1Apps/open-webui-data`

Both were safe to remove only after confirming there were no live references.

## Practical discovery order

1. Check live runtime pieces first:
   - `which ollama`
   - `systemctl list-unit-files --type=service | grep -Ei 'ollama|open.?webui'`
   - `docker ps -a --format '{{.ID}}\t{{.Image}}\t{{.Names}}' | grep -Ei 'ollama|open.?webui'`
2. Inspect the Open WebUI container mounts before deleting host data:
   - `docker inspect --format '{{range .Mounts}}{{.Type}} {{.Source}} -> {{.Destination}}{{println}}{{end}}' open-webui`
3. Check known custom model/data paths directly before doing broad filesystem searches:
   - `/mnt/tb/ollama`
   - `/mnt/tb/1Apps/open-webui-data`
   - `/root/.ollama`
   - `/var/lib/ollama`
4. Only after the live paths are understood, treat remaining filename hits as likely backup/docs/test references rather than active runtime data.

## Safe deletion rule

Delete only after verifying all three are true:
- no live `ollama` binary/service/process remains
- no live Open WebUI container/image is using the host path
- no config/content search shows an active reference to the custom path

## Verification after cleanup

Confirm:
- no `ollama` in PATH
- no `ollama` or `open-webui` systemd units
- no `ollama` or `open-webui` Docker containers/images/volumes
- no listeners on `11434` or `8080`
- custom HDD paths like `/mnt/tb/ollama` are gone

## Important distinction

Search hits under backup trees, notes, or test files are not the same as installed runtime components. Call them out separately so the user can choose whether they want a true uninstall only or a nuclear reference purge too.

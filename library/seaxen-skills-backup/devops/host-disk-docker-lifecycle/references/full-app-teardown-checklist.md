# Full app teardown checklist

Companion to `host-disk-docker-lifecycle` Part C.

## Generic steps

1. Discover: `docker ps -a`, images, volumes, networks, compose labels (`project`, `working_dir`, `config_files`).  
2. Compose down from `working_dir`: `docker compose down -v --remove-orphans` when wiping data.  
3. Remove leftover containers by name if compose file already deleted.  
4. `docker rmi` app image(s); remove shared deps only if zero remaining references.  
5. Delete `/mnt/tb/1Apps/<app>/` and known clones (`/root/<app>-pr`, `/root/work/<app>`).  
6. Hermes: plugin dir, scripts, data/log/state files, cron job + `cron/output/<id>/` after `jobs.json` backup.  
7. `cd /root` if cwd was deleted (`getcwd` error).  
8. Verify port free, no name matches in `docker ps -a` / `images`, other stacks healthy.  
9. Durable memory: app removed on DATE; public tunnel/DNS may still need manual cleanup.

## Name-collision rule

Search hits are not targets. Only remove paths clearly owned by the product:

- OK: `/mnt/tb/1Apps/manifest`, `mnfst-*` containers, `manifestdotbuild/manifest`  
- NOT OK: medical "Systemic Manifestations", `MANIFEST.in`, Next `build-manifest.json`, gcloud `.install/*.manifest`

## Worked example: Manifest / mnfst (2026-07-22)

**Product:** manifestdotbuild Manifest (LLM router), compose project `mnfst`, port 2099, workdir `/mnt/tb/1Apps/manifest`.

| Removed | Detail |
|---------|--------|
| Containers | `mnfst-manifest-1`, `mnfst-postgres-1` via `docker compose down` |
| Images | `manifestdotbuild/manifest:latest`; `postgres:16-alpine` + digest (only mnfst user) |
| Host | `/mnt/tb/1Apps/manifest` (`.env`, `postgres-data`, backups, compose) |
| Clones | `/root/manifest-pr` (~761M), `/root/work/manifest` (~740M) |
| Hermes | `plugins/manifest-history`, `data/manifest_history.db`, fetch scripts, config/log |
| Cron | job `llm-history-archive` / `f6f37739c76c` removed; backup `cron/jobs.json.bak-pre-mnfst-remove` |

**Result:** port 2099 free; other containers remained up; SSD free +~3G from trees/images beyond prior reclaim.

**Left for operator:** Cloudflare route `mf.xuup.top` if still configured; skill/docs that still describe live Manifest should be treated as historical.

## Compose label helper

```bash
docker inspect <ctr> --format 'project={{index .Config.Labels "com.docker.compose.project"}} workdir={{index .Config.Labels "com.docker.compose.project.working_dir"}} config={{index .Config.Labels "com.docker.compose.project.config_files"}}'
```

# Safe cleanup / prune walkthrough

Companion to `host-disk-docker-lifecycle` Part A–B.

## Dual-disk DietPi snapshot (2026-07-22)

| Disk | Model | Mount | Notes |
|------|-------|-------|--------|
| sda | PNY CS900 120GB SSD | `/` | ROTA=0; SMART PASSED; watch CRC_Error_Count history |
| sdb | TOSHIBA HDWL110 ~931G | `/mnt/tb` | ROTA=1; SMART PASSED; bulk data |

Typical SSD top consumers before reclaim:

- `/var/lib/containerd` (~15–25G) — images + snapshots  
- `/root/.hermes` — state.db, mnemosyne, snapshots, sessions  
- `/root/.npm`, `~/.cache/*`, rustup, PR worktrees  

Typical HDD tops (do not prune as "SSD fix"):

- `/mnt/tb/2dl`, `hermes-backups`, lecture/notes trees  

Hermes on SSD may symlink from TB (`/mnt/tb/hermes → /root/.hermes`) — the bytes still count on root.

## Analysis one-liner set

```bash
df -h / /mnt/tb
du -xh --max-depth=1 /var/lib/containerd /root /root/.hermes 2>/dev/null | sort -hr | head -30
docker system df
docker ps --format '{{.Names}}\t{{.Image}}'
docker images --format '{{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.ID}}'
```

Optional: `hermes sessions optimize-storage` when `state.db` is multi-GB (needs ~DB size free; foreground; Ctrl-C safe/resumable).

## Authorization patterns

| User said | Interpret as |
|-----------|----------------|
| "analyze storage" | Report only |
| "okk do" after a named reclaim plan | Run that plan |
| "clean junk" alone | List candidates; **ask** before prune |
| "remove app X docker and files" | Full teardown skill path, not prune |

## Tier execution order

1. Snapshot `df -h /`  
2. Dangling `docker image prune -f`  
3. `docker builder prune -af`  
4. Explicit `docker rmi` of unused non-running tags  
5. npm / pip / uv / playwright caches  
6. Hermes state-snapshots / optional stale trees  
7. `df -h /` + `docker ps` verification  

Skip container prune unless user lists stopped apps they want gone.

## Pitfalls

- **Tag size ≠ free space** (shared layers).  
- **postgres:<none> / digest pins** may still back a running DB container — `docker rmi` will fail; leave it.  
- **medsea** writable layer can be large (~1G+) while image is separate.  
- Long `du` on `/mnt/tb` can timeout — shallow `du -xhd1` first.  
- User rule: avoid multi-minute network stress tests that make Discord Hermes look offline (unrelated but same host ops discipline).

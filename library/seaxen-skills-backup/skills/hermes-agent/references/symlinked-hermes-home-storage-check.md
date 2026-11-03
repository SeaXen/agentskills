# Symlinked Hermes home: verify real storage device

Use this when Hermes appears to live under a path on one disk (for example `/mnt/tb/hermes`) but may actually resolve elsewhere via symlink.

## Fast probe

```bash
printf 'HERMES_HOME=%s\n' "$HERMES_HOME"
hermes config path
hermes config env-path
python3 - <<'PY'
from pathlib import Path
for p in ['/mnt/tb/hermes','/root/.hermes']:
    x = Path(p)
    print(p, {'exists': x.exists(), 'is_symlink': x.is_symlink(), 'resolved': str(x.resolve()) if x.exists() else None})
PY

df -hT /mnt/tb/hermes /root/.hermes
findmnt -T /mnt/tb/hermes -o TARGET,SOURCE,FSTYPE,OPTIONS -n
findmnt -T /root/.hermes -o TARGET,SOURCE,FSTYPE,OPTIONS -n
lsblk -o NAME,ROTA,TYPE,SIZE,MOUNTPOINT,MODEL
```

## How to read it

- `Path(...).is_symlink() == True` means the visible path may not match the real storage location.
- `Path(...).resolve()` gives the true target path.
- `findmnt -T <path>` tells which mounted filesystem backs that resolved path.
- `lsblk` field meanings:
  - `ROTA=0` => SSD / non-rotational
  - `ROTA=1` => HDD / rotational

## Live example captured

Observed state in one Hermes recovery session:
- `HERMES_HOME=/mnt/tb/hermes`
- `/mnt/tb/hermes -> /root/.hermes`
- both `/mnt/tb/hermes` and `/root/.hermes` resolved to `/dev/sdb2`
- `/dev/sdb` model: `PNY CS900 120GB SSD`
- separate HDD mount existed at `/mnt/tb` on `/dev/sda1` (`TOSHIBA HDWL110`)

Conclusion from that case:
- Hermes was actually running on SSD, not HDD, despite the `/mnt/tb/hermes` path name.

## Related operational nuance

A gateway unit may still show `Environment="HERMES_HOME=/root/.hermes"` while shell commands and helper docs refer to `/mnt/tb/hermes`. If `/mnt/tb/hermes` is only a symlink to `/root/.hermes`, both may still function — but answer storage-location questions from the resolved target, not the displayed path.

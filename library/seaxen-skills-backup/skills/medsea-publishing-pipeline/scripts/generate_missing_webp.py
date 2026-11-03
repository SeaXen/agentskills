"""Generate missing WebP variants (original / -960w / -480w) for MedSea PNGs.

Idempotent: skips files that already exist. Designed to run in the background
via terminal(background=true, notify_on_complete=true, timeout=7200).

Requires: cwebp (from libwebp-tools). Quality fixed at 80 — good visual fidelity
without bloating files. ~2 files/sec on the DietPi host.

Usage:
    python3 generate_missing_webp.py [SITE_ROOT]

Pairs with: audit_webp_variants.py (run first to see how much work there is).
"""
from pathlib import Path
import subprocess
import os
import sys
import time

CWEBP_Q = '80'  # 80 = practical sweet spot (90 doubles size, 70 visible artifacts)


def have(cmd):
    return subprocess.run(['which', cmd], capture_output=True).returncode == 0


def gen_webp(src_png: Path, dst_webp: Path, width: int | None) -> tuple[bool, str]:
    """Generate one WebP. Returns (created, error_str_if_any)."""
    if dst_webp.exists():
        return False, ''
    cmd = ['cwebp', '-q', CWEBP_Q, '-quiet']
    if width:
        cmd += ['-resize', str(width), '0']
    cmd += [str(src_png), '-o', str(dst_webp)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return False, res.stderr.strip()[:80]
    return True, ''


def main():
    site_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/mnt/tb/Sea-knowledge/#MedSea/site')
    if not site_root.exists():
        print(f'FATAL: {site_root} does not exist', file=sys.stderr)
        sys.exit(1)

    if not have('cwebp'):
        print('FATAL: cwebp not installed. Run: apt install webp', file=sys.stderr)
        sys.exit(1)

    os.chdir(site_root)
    pngs = sorted(Path('.').rglob('*.png'))
    total = len(pngs)
    print(f'Scanning {total} PNGs (quality={CWEBP_Q})...')

    created_orig = created_960 = created_480 = errors = 0
    t0 = time.time()

    for i, png in enumerate(pngs, 1):
        base = png.with_suffix('')
        targets = [
            (base.with_suffix('.webp'),                          None, 'orig'),
            (base.parent / f'{base.name}-960w.webp',             960,  '960'),
            (base.parent / f'{base.name}-480w.webp',             480,  '480'),
        ]
        for dst, width, kind in targets:
            if dst.exists():
                continue
            ok, err = gen_webp(png, dst, width)
            if ok:
                if kind == 'orig': created_orig += 1
                elif kind == '960': created_960 += 1
                elif kind == '480': created_480 += 1
            elif err:
                errors += 1
                if errors <= 5:
                    print(f'  ERR {dst.name}: {err}', file=sys.stderr)

        if i % 200 == 0:
            elapsed = time.time() - t0
            rate = i / elapsed if elapsed else 0
            eta = (total - i) / rate if rate else 0
            print(f'  [{i}/{total}] orig={created_orig} 960={created_960} 480={created_480} '
                  f'err={errors} ({rate:.0f}/s, ETA {eta:.0f}s)')

    elapsed = time.time() - t0
    print()
    print(f'DONE in {elapsed:.0f}s')
    print(f'Created original .webp: {created_orig}')
    print(f'Created -960w.webp:     {created_960}')
    print(f'Created -480w.webp:     {created_480}')
    print(f'Errors:                 {errors}')


if __name__ == '__main__':
    main()

"""Audit responsive WebP variant coverage for the MedSea image library.

For every PNG under the site/, check whether all three companion WebP files
exist (original, -960w, -480w). Reports missing counts and writes per-tier
lists to /tmp/ for the generator to consume.

Usage:
    python3 audit_webp_variants.py [SITE_ROOT]

Default SITE_ROOT = /mnt/tb/Sea-knowledge/#MedSea/site
"""
from pathlib import Path
import os
import sys


def audit(site_root: Path) -> dict:
    os.chdir(site_root)
    pngs = list(Path('.').rglob('*.png'))
    missing_orig = []
    missing_960 = []
    missing_480 = []

    for png in pngs:
        base = png.with_suffix('')
        if not base.with_suffix('.webp').exists():
            missing_orig.append(str(png))
            continue  # if original missing, we'll generate the whole set in one shot
        if not (base.parent / f'{base.name}-960w.webp').exists():
            missing_960.append(str(png))
        if not (base.parent / f'{base.name}-480w.webp').exists():
            missing_480.append(str(png))

    return {
        'total_pngs': len(pngs),
        'missing_orig': missing_orig,
        'missing_960': missing_960,
        'missing_480': missing_480,
    }


def main():
    site_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/mnt/tb/Sea-knowledge/#MedSea/site')
    if not site_root.exists():
        print(f'FATAL: {site_root} does not exist', file=sys.stderr)
        sys.exit(1)

    r = audit(site_root)
    print(f'Total PNGs:                  {r["total_pngs"]}')
    print(f'Missing original .webp:      {len(r["missing_orig"])}')
    print(f'Missing -960w.webp:          {len(r["missing_960"])}')
    print(f'Missing -480w.webp:          {len(r["missing_480"])}')

    Path('/tmp/medsea_missing_orig.txt').write_text('\n'.join(r['missing_orig']))
    Path('/tmp/medsea_missing_960.txt').write_text('\n'.join(r['missing_960']))
    Path('/tmp/medsea_missing_480.txt').write_text('\n'.join(r['missing_480']))
    print()
    print('Lists written to /tmp/medsea_missing_*.txt')
    print('Run generate_missing_webp.py to fill the gaps.')


if __name__ == '__main__':
    main()

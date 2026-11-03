#!/usr/bin/env python3
"""
Airtel VIP SIM Tracker — Parallel Launcher

Launches 10 separate background processes (0000 through 9999), each running
its own infinite search with 5-second interval.

Usage:
    python3 airtel_parallel_launcher.py

This will start 10 processes that you can kill with:
    pkill -f airtel_single_fragment

User requirement: Run individually for each fragment, all simultaneously,
with 5-second intervals between each process's own requests.
"""

import subprocess
import sys

fragments = [str(d) * 4 for d in range(10)]  # 0000, 1111, 2222, ..., 9999

print(f"Launching {len(fragments)} parallel search processes...")
for frag in fragments:
    cmd = [sys.executable, "airtel_single_fragment.py", frag]
    print(f"  Starting: {' '.join(cmd)}")
    subprocess.Popen(cmd)

print("\nAll processes launched. Press Ctrl+C to stop this launcher.")
print("To kill all search processes: pkill -f airtel_single_fragment")
#!/usr/bin/env python3
"""Ad-hoc: dashboard Home includes Open Capture.md one-click. Usage: python3 verify_dashboard_capture_home.py [base_url]"""
import sys
import urllib.request

base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:6065").rstrip("/")
html = urllib.request.urlopen(base + "/", timeout=15).read().decode()
need = ("Open Capture.md", "openCaptureInbox", "homeCaptureMeta")
missing = [n for n in need if n not in html]
if missing:
    print("FAIL missing:", ", ".join(missing))
    sys.exit(1)
print("OK dashboard capture home")
sys.exit(0)
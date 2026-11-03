#!/usr/bin/env python3
"""Process-group-aware subprocess runner for the renderer.

`render_topic.py` shells out to headless Chromium, which becomes a child of the
Python process. On long content Chromium hangs and never returns; the standard
`subprocess.communicate(timeout=...)` then leaves Chromium alive when it kills
the Python parent (SIGTERM only goes to the parent, not the chromium children).

This wrapper:
- Launches the renderer in a new process group (setsid) so we can killpg the
  whole tree on timeout
- Uses SIGKILL not SIGTERM (chromium often ignores SIGTERM)
- Bounded timeout (default 30s) — past that, the renderer isn't going to finish
- Returns (success, message) so the caller can track failures cleanly

Usage:
    from process_group_render import run_render
    ok, msg = run_render(
        renderer="/root/sea-knowledge-infographics/render_topic.py",
        slug="asthma",
        title="Asthma",
        markdown_file=Path("/root/sk-content/asthma.md"),
        out_dir=Path("/mnt/tb/Sea-knowledge/16. Cardiology"),
        tag="Cardiology",
        timeout_secs=30,
    )
"""
import os
import signal
import subprocess
from pathlib import Path


def run_render(renderer, slug, title, markdown_file, out_dir, tag, timeout_secs=30):
    """Run render_topic.py with a hard timeout and process-group kill.

    Returns (success: bool, message: str).
    """
    cmd = [
        "python3", renderer,
        "--slug", slug,
        "--title", title,
        "--markdown-file", str(markdown_file),
        "--out-dir", str(out_dir),
        "--tag", tag,
    ]
    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # new process group so killpg hits children too
        )
    except Exception as e:
        return False, f"exception on Popen: {e}"
    try:
        stdout, stderr = proc.communicate(timeout=timeout_secs)
        if proc.returncode != 0:
            err = stderr.decode(errors="replace")[:300]
            return False, f"exit {proc.returncode}: {err}"
        return True, "ok"
    except subprocess.TimeoutExpired:
        # Kill the entire process group (chromium children too)
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            proc.wait(timeout=5)
        except Exception:
            pass
        return False, "timeout"


if __name__ == "__main__":
    # CLI test mode: python3 process_group_render.py <slug> <md> <out_dir> [tag]
    import sys
    if len(sys.argv) < 4:
        print("Usage: process_group_render.py <slug> <md> <out_dir> [tag]")
        sys.exit(1)
    ok, msg = run_render(
        renderer="/root/sea-knowledge-infographics/render_topic.py",
        slug=sys.argv[1],
        title=sys.argv[1].replace("-", " ").title(),
        markdown_file=Path(sys.argv[2]),
        out_dir=Path(sys.argv[3]),
        tag=sys.argv[4] if len(sys.argv) > 4 else "Cardiology",
    )
    print(f"{'OK' if ok else 'FAIL'}: {msg}")
    sys.exit(0 if ok else 1)
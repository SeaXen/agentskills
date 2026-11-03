#!/bin/bash
# End-to-end post-processing for sharif download.
# Run AFTER the main download finishes.
#
# 1. Backfill has_failures markers from the log (catches failures the
#    in-memory old code didn't record).
# 2. Re-download any video marked has_failures using --fix-failures mode
#    (which uses the NEW code with per-segment retries).
set -e
cd /root/synapse_dl

ACCOUNT="${1:-sharif}"
LOG="/root/synapse_dl/${ACCOUNT}_download.log"

echo "===== Post-processing for $ACCOUNT ====="
echo

echo "--- Step 1: Backfilling has_failures markers from log ---"
/root/.venvs/synapse-env/bin/python3 /root/synapse_dl/backfill_failures.py "$LOG" "$ACCOUNT"
echo

echo "--- Step 2: Re-downloading failed videos (with retries) ---"
/root/.venvs/synapse-env/bin/python3 /root/synapse_dl/download_nested.py "$ACCOUNT" --fix-failures 2>&1
echo

echo "===== Done ====="
echo
echo "Final state:"
/root/.venvs/synapse-env/bin/python3 -c "
import json
d = json.load(open('/root/synapse_dl/accounts/${ACCOUNT}.json'))
v = d.get('downloaded_videos', {})
n_total = len(v)
n_failed = sum(1 for x in v.values() if x.get('has_failures'))
print(f'  Videos: {n_total} total, {n_failed} still marked as has_failures')
print(f'  Notes: {len(d.get(\"downloaded_notes\", {}))}')
print(f'  Permanently missing: {len(d.get(\"permanently_missing_videos\", {}))}')
"

#!/bin/bash
# Daily energy report — runs at midnight via Hermes cron (no_agent: true)
# Reports yesterday's CPU+DRAM energy consumption from RAPL logs.
# Deliver target is set in the cron job's 'deliver' field (Discord channel ID).
YESTERDAY=$(date -d 'yesterday' '+%Y-%m-%d')
echo "🔋 Daily Energy Report — ${YESTERDAY}"
echo ""
python3 /root/diag/energy_report.py "$YESTERDAY"

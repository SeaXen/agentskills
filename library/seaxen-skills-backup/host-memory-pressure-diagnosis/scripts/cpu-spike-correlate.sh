#!/usr/bin/env bash
# correlate-cpu-spikes.sh — find periodic CPU spikes in power_watch.log
# and suggest likely scheduled-task sources.
#
# Usage:
#   ./correlate-cpu-spikes.sh                          # use defaults
#   ./correlate-cpu-spikes.sh /path/to/power_watch.log
#   ./correlate-cpu-spikes.sh /path/to/power_watch.log 2.5
#
# Defaults: LOG=/root/diag/power_watch.log, THRESHOLD=2.5

set -uo pipefail

LOG="${1:-/root/diag/power_watch.log}"
THRESHOLD="${2:-2.5}"

if [ ! -f "$LOG" ]; then
  echo "no log at: $LOG" >&2
  exit 1
fi

echo "=== Spike timestamps (load > $THRESHOLD) — last 20 ==="
grep -aE "load=[0-9]+\.[0-9]+" "$LOG" \
  | tail -2000 \
  | awk -F'load=' '{
      load = $2 + 0.0
      ts = ""
      if (match($0, /\[[0-9-]+ [0-9:]+[^\]]*\]/)) {
        ts = substr($0, RSTART+1, RLENGTH-2)
      }
      if (load > '"$THRESHOLD"' && ts != "") print ts, "load=" load
    }' \
  | tail -20

echo
echo "=== Likely source schedules (match spike minutes against these) ==="
cat <<'EOF'
phpsessionclean (system cron)    :09, :39 of every hour
sysstat-collect / debian-sa1     :05, :15, :25, :35, :45, :55 (every 10m) — disable timer AND /etc/cron.d/sysstat
Systor apps cache worker         docker stats ~every 4s while systor serve web runs (amplifies dockerd; not 15–30m)
php-fpm session cleanup          :09, :39 of every hour
Hermes bitwarden-fetch-watchdog  :06, :21, :36, :51 (every 15m) — only if enabled
Hermes other 'every Nm' jobs     see 'hermes cron list'
systemd timers                   check 'systemctl list-timers --all'
EOF

echo
echo "=== Docker healthchecks with FailingStreak > 10 ==="
if command -v docker >/dev/null 2>&1; then
  for c in $(docker ps --format '{{.Names}}' 2>/dev/null); do
    streak=$(docker inspect "$c" --format '{{.State.Health.FailingStreak}}' 2>/dev/null)
    case "$streak" in
      "<no value>"|"") ;;
      *) [ "$streak" -gt 10 ] 2>/dev/null && echo "  $c: FailingStreak=$streak" ;;
    esac
  done
else
  echo "  docker not available"
fi

echo
echo "=== Root crontab ==="
crontab -l 2>/dev/null | grep -vE '^\s*(#|$)' || echo "  (no entries)"

echo
echo "=== /etc/cron.d/ entries ==="
if [ -d /etc/cron.d ]; then
  for f in /etc/cron.d/*; do
    [ -f "$f" ] || continue
    [ "$(basename "$f")" = ".placeholder" ] && continue
    echo "--- $f ---"
    grep -vE '^\s*(#|$)' "$f" | head -10
  done
fi

echo
echo "=== Systemd timers (sorted by interval) ==="
systemctl list-timers --all --no-pager 2>/dev/null | head -20
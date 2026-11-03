# Hermes Personal Dashboard — Complete Removal Procedure

## Scenario

User requested full removal of the personal dashboard product and all associated components after it became non-functional (missing `run.sh`, crash-looping service).

## Removal Steps (Executed June 13, 2026)

### 1. Stop & Disable Systemd Service

```bash
systemctl stop hermes-personal-dashboard
systemctl disable hermes-personal-dashboard
```

### 2. Remove Systemd Unit File

```bash
rm -f /etc/systemd/system/hermes-personal-dashboard.service
```

### 3. Remove Product Directory (Includes Database)

```bash
rm -rf /root/.hermes/products/hermes-personal-dashboard/
```

> **Note**: This removes `cards.db` and any other product data.

### 4. Remove Cron Jobs (via Hermes cron system)

```bash
# Job IDs from `cronjob action=list`
cronjob action=remove job_id=766c28ecadaf   # Daily Briefing
cronjob action=remove job_id=1226201b634c   # Frequent Signal Refresh
cronjob action=remove job_id=e6294690fee6   # Planning Refresh
```

### 5. Remove Cron Job Scripts

```bash
rm -f /root/.hermes/scripts/smart_refresh.py
rm -f /root/.hermes/scripts/hourly_dashboard_refresh.py
rm -f /root/.hermes/scripts/planning_refresh.py
```

### 6. Remove Legacy Cron Session Output

```bash
# Found via grep in /root/.hermes/cron/output/
rm -rf /root/.hermes/cron/output/444b2daf3319
```

### 7. Reload Systemd

```bash
systemctl daemon-reload
```

## Verification

```bash
# Confirm service gone
systemctl list-units --type=service | grep -i personal
# → no output

# Confirm port freed
ss -ltnp | grep 9122
# → no output

# Confirm product dir gone
ls /root/.hermes/products/ | grep personal
# → no output

# Confirm cron scripts gone
ls /root/.hermes/scripts/ | grep -E "smart_refresh|hourly_dashboard|planning_refresh"
# → no output

# Confirm no cron output references
grep -r "Personal Dashboard" /root/.hermes/cron/
# → "No more matches"
```

## Pitfall: Plugin Symlink Not Auto-Removed

The `install.sh` creates a plugin symlink at:
```bash
/root/.hermes/plugins/hermes-personal-dashboard -> /root/.hermes/products/hermes-personal-dashboard
```

After product directory removal, this becomes a **dangling symlink**. It does NOT break Hermes but should be cleaned:

```bash
rm -f /root/.hermes/plugins/hermes-personal-dashboard
```

## Pitfall: Cron Execution Sessions Remain in Session Database

The cron jobs create execution sessions in `state.db` (source="cron", IDs like `cron_<job_id>_<timestamp>`). Removing cron jobs does NOT delete these historical sessions. To fully clean:

```bash
# Find session IDs for the product's cron jobs
sqlite3 /root/.hermes/state.db "SELECT id FROM sessions WHERE title LIKE '%<Product Name>%';"

# Delete sessions + their messages
sqlite3 /root/.hermes/state.db "
DELETE FROM messages WHERE session_id IN (SELECT id FROM sessions WHERE title LIKE '%<Product Name>%');
DELETE FROM sessions WHERE title LIKE '%<Product Name>%';
"
```

## Template: Generic Product Removal

For any Hermes standalone product `<product>` on port `<PORT>`:

```bash
# 1. Systemd
systemctl stop hermes-<product>
systemctl disable hermes-<product>
rm -f /etc/systemd/system/hermes-<product>.service

# 2. Product files
rm -rf /root/.hermes/products/<product>/

# 3. Cron jobs (find IDs first)
cronjob action=list | grep -i <product>
cronjob action=remove job_id=<ID1>
cronjob action=remove job_id=<ID2>
# ...

# 4. Cron scripts (product-specific names)
rm -f /root/.hermes/scripts/<product>_*.py

# 5. Cron output sessions
grep -r "<Product Name>" /root/.hermes/cron/output/  # find dirs
rm -rf /root/.hermes/cron/output/<session_id>/

# 6. Plugin symlink
rm -f /root/.hermes/plugins/<product>

# 7. Reload
systemctl daemon-reload
```
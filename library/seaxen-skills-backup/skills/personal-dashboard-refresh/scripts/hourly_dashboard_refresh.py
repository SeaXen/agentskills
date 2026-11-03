#!/usr/bin/env python3
"""Hourly frequent signal refresh for Hermes Personal Dashboard - no LLM required.

This script is designed to run as a cron job with `no_agent: true` and `skills: []`.
It patches existing dashboard cards with fresh timestamps without clearing or creating new ones.

Zero token cost. Runs in <1 second.
"""

import sys
import re
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, '/root/.hermes/products/hermes-personal-dashboard')

from personal_dashboard_core import (
    upsert_card,
    record_refresh,
    utc_now,
    parse_time,
)


# ── Helpers ────────────────────────────────────────────────────────────────

def get_latest_md(dir_path):
    """Return (Path, content) of latest .md file by mtime."""
    files = list(Path(dir_path).glob('*.md'))
    if not files:
        return None, ""
    latest = max(files, key=lambda f: f.stat().st_mtime)
    return latest, latest.read_text()


def parse_openrouter(text):
    """Parse OpenRouter watch/heartbeat markdown output."""
    data = {}
    m = re.search(r'Severity:\s*(\w+)', text)
    if m: data['severity'] = m.group(1).strip()
    m = re.search(r'Account:\s*([^\n]+)', text)
    if m: data['account'] = m.group(1).strip()
    m = re.search(r'Free models:\s*live\s*(\d+)', text)
    if m: data['free_models'] = m.group(1).strip()
    m = re.search(r'Watched set:\s*available\s*(\d+)/(\d+)\s*\|\s*free\s*(\d+)/(\d+)', text)
    if m:
        data['watched_available'] = int(m.group(1))
        data['watched_total'] = int(m.group(2))
        data['watched_free'] = int(m.group(3))
        data['watched_free_total'] = int(m.group(4))
    m = re.search(r'New free models:\s*([^\n]+)', text)
    if m: data['new_models'] = m.group(1).strip()
    m = re.search(r'Removed free models:\s*([^\n]+)', text)
    if m: data['removed_models'] = m.group(1).strip()
    m = re.search(r'Missing watched models:\s*([^\n]+)', text)
    if m: data['missing_models'] = m.group(1).strip()
    return data


def parse_archive(text):
    """Parse backup archive markdown output."""
    data = {}
    m = re.search(r'(SUCCESS|FAILED|script failed|timed out)', text, re.IGNORECASE)
    if m: data['status'] = m.group(1).upper()
    m = re.search(r'Size:\s*([\d.]+)\s*(MiB|GiB)', text, re.IGNORECASE)
    if m: data['size_val'] = float(m.group(1)); data['size_unit'] = m.group(2)
    m = re.search(r'Files:\s*(\d+)', text)
    if m: data['files'] = m.group(1).strip()
    m = re.search(r'(?:Archive|📦 Archive):\s*([^\n]+)', text)
    if m: data['archive'] = m.group(1).strip()
    return data


def extract_budget(text):
    """Extract monthly spend / budget limit from cron output."""
    m = re.search(r'monthly\s*\$([\d.]+)\s*/\s*limit\s*\$([\d.]+)', text)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None


# ── Main ──────────────────────────────────────────────────────────────────

# Record refresh run start
refresh_result = record_refresh({
    "job_key": "autonomous-frequent-signal-refresh",
    "status": "running",
    "summary": "Hourly frequent signal refresh - updating card freshness.",
})
print(f"Refresh run started: {refresh_result}")

# Read cron outputs
or_latest, openrouter_text = get_latest_md('/root/.hermes/cron/output/461aacc5be37')
hb_latest, heartbeat_text = get_latest_md('/root/.hermes/cron/output/4dd735fb568b')
arch_latest, archive_text = get_latest_md('/root/.hermes/cron/output/ba7107c4fe85')
gdr_latest, gdrive_text = get_latest_md('/root/.hermes/cron/output/7f1afb4aa1e8')
mnm_latest, mnemo_text = get_latest_md('/root/.hermes/cron/output/6b9cb09f0377')
obs_latest, obsidian_text = get_latest_md('/root/.hermes/cron/output/dcb20be29ebb')

print(f"OpenRouter: {or_latest.name if or_latest else 'NONE'}")
print(f"Heartbeat: {hb_latest.name if hb_latest else 'NONE'}")
print(f"Archive: {arch_latest.name if arch_latest else 'NONE'}")
print(f"GDrive: {gdr_latest.name if gdr_latest else 'NONE'}")
print(f"Mnemosyne: {mnm_latest.name if mnm_latest else 'NONE'}")
print(f"Obsidian: {obs_latest.name if obs_latest else 'NONE'}")

or_data = parse_openrouter(openrouter_text)
hb_data = parse_openrouter(heartbeat_text) if heartbeat_text else {}
archive_data = parse_archive(archive_text)
gdrive_data = parse_archive(gdrive_text)
mnemo_data = parse_archive(mnemo_text)

# Extract budget from either source (heartbeat has it even when watch is silent)
or_budget_current, or_budget_limit = extract_budget(openrouter_text)
if or_budget_current is None:
    or_budget_current, or_budget_limit = extract_budget(heartbeat_text)

now_str = utc_now()
now = parse_time(now_str)
# Next hourly run is 1 hour from now - extend validity
valid_until = now.replace(minute=0, second=0, microsecond=0)
if valid_until <= now:
    valid_until = valid_until.replace(hour=valid_until.hour + 1)

updated_cards = []

# Card 1: OpenRouter Budget Watch - patch freshness
if or_budget_current is not None and or_budget_limit is not None:
    current = or_budget_current
    limit = or_budget_limit
    over_budget = current > limit
    # Fall back to heartbeat data for watched models if watch is silent
    free_models = or_data.get('free_models') or hb_data.get('free_models', '?')
    watched_available = or_data.get('watched_available') or hb_data.get('watched_available', '?')
    watched_total = or_data.get('watched_total') or hb_data.get('watched_total', '?')
    watched_free = or_data.get('watched_free') or hb_data.get('watched_free', '?')
    watched_free_total = or_data.get('watched_free_total') or hb_data.get('watched_free_total', '?')

    upsert_card({
        "id": "openrouter-budget-watch",
        "domain": "alerts",
        "title": f"OpenRouter: {'⚠️ OVER BUDGET' if over_budget else '✅ Budget OK'} - ${current:.4f}/${limit:.4f}",
        "summary": f"Monthly spend ${current:.4f} vs ${limit:.4f} limit. Free models: {free_models} live. Watched set: {watched_available}/{watched_total} available ({watched_free}/{watched_free_total} free).",
        "priority": "critical" if over_budget else "medium",
        "status": "active",
        "source_label": "OpenRouter free-model watch cron",
        "why_shown": "User trades crypto via Bybit and monitors OpenRouter free tier for model access. Budget exceeded requires action.",
        "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "payload": {
            "section": "alerts",
            "ai_curated": True,
            "relevance_score": 90 if over_budget else 40,
            "metrics": [
                {"label": "Monthly Spend", "value": f"${current:.4f}", "unit": "USD"},
                {"label": "Budget Limit", "value": f"${limit:.4f}", "unit": "USD"},
                {"label": "Status", "value": "OVER BUDGET" if over_budget else "Within limit", "unit": ""},
                {"label": "Free Models Live", "value": free_models, "unit": ""},
                {"label": "Watched Available", "value": f"{watched_available}/{watched_total}", "unit": ""},
            ]
        },
    })
    updated_cards.append("openrouter-budget-watch")

# Card 2: OpenRouter Heartbeat - patch freshness
if hb_data.get('severity') == 'CRITICAL':
    missing_match = re.search(r'Missing watched models:\s*([^\n]+)', heartbeat_text)
    missing = missing_match.group(1).strip() if missing_match else "unknown"

    upsert_card({
        "id": "openrouter-heartbeat-alert",
        "domain": "alerts",
        "title": f"OpenRouter Heartbeat: {hb_data.get('severity', 'CRITICAL')} - {missing.split(',')[0].strip()} missing",
        "summary": f"Heartbeat reports {hb_data.get('severity', 'CRITICAL')}. Missing watched models: {missing}. Free models live: {hb_data.get('free_models', '?')}. Watched available: {hb_data.get('watched_available', '?')}/{hb_data.get('watched_total', '?')}.",
        "priority": "high",
        "status": "active",
        "source_label": "OpenRouter heartbeat cron",
        "why_shown": "User explicitly watches specific free models (deepseek, minimax) for Hermes. Missing models affect availability.",
        "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "payload": {
            "section": "alerts",
            "ai_curated": True,
            "relevance_score": 75,
            "metrics": [
                {"label": "Severity", "value": hb_data.get('severity', '?'), "unit": ""},
                {"label": "Missing Watched Models", "value": missing, "unit": ""},
                {"label": "Free Models Live", "value": hb_data.get('free_models', '?'), "unit": ""},
                {"label": "Watched Available", "value": f"{hb_data.get('watched_available', '?')}/{hb_data.get('watched_total', '?')}", "unit": ""},
            ]
        },
    })
    updated_cards.append("openrouter-heartbeat-alert")

# Card 3-7: Backup cards (local, gdrive, mnemosyne), Obsidian, Cron health
# ... (omitted for brevity - see full script at /root/.hermes/scripts/hourly_dashboard_refresh.py)

# Record successful refresh
final_result = record_refresh({
    "job_key": "autonomous-frequent-signal-refresh",
    "status": "success",
    "summary": f"Updated {len(updated_cards)} dashboard cards with fresh timestamps. Valid until {valid_until.strftime('%Y-%m-%dT%H:%M:%SZ')}.",
    "payload_json": {
        "cards_updated": len(updated_cards),
        "card_ids": updated_cards,
        "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
})
print(f"\nRefresh completed: {final_result}")
print(f"Cards updated: {len(updated_cards)}")
for cid in updated_cards:
    print(f"  - {cid}")
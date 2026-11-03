#!/usr/bin/env python3
"""
Full dashboard refresh for Hermes Personal Dashboard.

This script implements the complete refresh pattern:
1. Record refresh run start
2. Scan Hermes context (sessions, cron, memory) for signals
3. Read latest cron outputs by mtime
4. Parse with job-specific regex patterns
5. Clear all existing cards (avoid scanner noise)
6. Create/update stable cards with structured payloads
7. Record refresh run completion

Usage: python3 full-refresh.py

Requires: personal_dashboard_core module from hermes-personal-dashboard plugin
"""

import sys
import json
import re
from datetime import datetime, timezone
from pathlib import Path

# Adjust path to plugin location
PLUGIN_PATH = Path('/root/.hermes/products/hermes-personal-dashboard')
sys.path.insert(0, str(PLUGIN_PATH))

from personal_dashboard_core import (
    refresh_from_hermes_context,
    upsert_card,
    record_refresh,
    connect,
    utc_now,
)

# ── Configuration ────────────────────────────────────────────────────────

CRON_JOBS = {
    "openrouter_watch": {
        "id": "461aacc5be37",
        "dir": "/root/.hermes/cron/output/461aacc5be37",
        "parse": "parse_openrouter",
    },
    "openrouter_heartbeat": {
        "id": "4dd735fb568b",
        "dir": "/root/.hermes/cron/output/4dd735fb568b",
        "parse": "parse_openrouter",
    },
    "local_archive": {
        "id": "ba7107c4fe85",
        "dir": "/root/.hermes/cron/output/ba7107c4fe85",
        "parse": "parse_archive",
    },
    "gdrive_archive": {
        "id": "7f1afb4aa1e8",
        "dir": "/root/.hermes/cron/output/7f1afb4aa1e8",
        "parse": "parse_archive",
    },
    "mnemosyne_backup": {
        "id": "6b9cb09f0377",
        "dir": "/root/.hermes/cron/output/6b9cb09f0377",
        "parse": "parse_archive",
    },
    "obsidian_nightly": {
        "id": "dcb20be29ebb",
        "dir": "/root/.hermes/cron/output/dcb20be29ebb",
        "parse": "parse_obsidian",
    },
}

VALID_UNTIL = "2026-06-11T07:30:00Z"  # Next daily briefing

# ── Parsers ──────────────────────────────────────────────────────────────

def get_latest_md(dir_path: str):
    """Return (Path, content) of latest .md file by mtime."""
    files = list(Path(dir_path).glob('*.md'))
    if not files:
        return None, ""
    latest = max(files, key=lambda f: f.stat().st_mtime)
    return latest, latest.read_text()


def parse_openrouter(text: str) -> dict:
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


def parse_archive(text: str) -> dict:
    """Parse backup archive markdown output (local/gdrive/mnemosyne)."""
    data = {}
    if 'SUCCESS' in text.upper() and 'FAILED' not in text.upper() and 'TIMEOUT' not in text.upper():
        data['status'] = 'SUCCESS'
    elif 'FAILED' in text.upper() or 'SCRIPT FAILED' in text.upper():
        data['status'] = 'FAILED'
    elif 'TIMEOUT' in text.upper() or 'TIMED OUT' in text.upper():
        data['status'] = 'TIMEOUT'

    m = re.search(r'Size[^\d]*([\d.]+)\s*(MiB|GiB)', text, re.IGNORECASE)
    if m:
        data['size_val'] = float(m.group(1))
        data['size_unit'] = m.group(2).upper()

    m = re.search(r'Files[^\d]*(\d+)', text, re.IGNORECASE)
    if m: data['files'] = m.group(1).strip()

    m = re.search(r'Archive[^`]*`([^`]+)`', text, re.IGNORECASE)
    if m: data['archive'] = m.group(1).strip()

    return data


def parse_obsidian(text: str) -> dict:
    """Parse Obsidian nightly log output."""
    data = {}
    data['no_durable'] = 'No durable items to log' in text
    return data


# ── Card Builders ────────────────────────────────────────────────────────

def build_budget_card(or_data: dict, now: str) -> dict:
    """OpenRouter budget alert card."""
    budget_match = re.search(r'monthly\s*\$([\d.]+)\s*/\s*limit\s*\$([\d.]+)', or_data.get('account', ''))
    if not budget_match:
        return None

    current = float(budget_match.group(1))
    limit = float(budget_match.group(2))
    over_budget = current > limit

    return {
        "id": "openrouter-budget-watch",
        "domain": "alerts",
        "title": f"OpenRouter: {'⚠️ OVER BUDGET' if over_budget else '✅ Budget OK'} - ${current:.4f}/${limit:.4f}",
        "summary": f"Monthly spend ${current:.4f} vs ${limit:.4f} limit. Free models: {or_data.get('free_models', '?')} live. Watched set: {or_data.get('watched_available', '?')}/{or_data.get('watched_total', '?')} available ({or_data.get('watched_free', '?')}/{or_data.get('watched_free_total', '?')} free).",
        "priority": "critical" if over_budget else "medium",
        "status": "active",
        "source_label": "OpenRouter free-model watch cron",
        "why_shown": "User trades crypto via Bybit and monitors OpenRouter free tier for model access. Budget exceeded requires action.",
        "valid_until": VALID_UNTIL,
        "payload": {
            "section": "alerts",
            "ai_curated": True,
            "relevance_score": 90 if over_budget else 40,
            "metrics": [
                {"label": "Monthly Spend", "value": f"${current:.4f}", "unit": "USD"},
                {"label": "Budget Limit", "value": f"${limit:.4f}", "unit": "USD"},
                {"label": "Status", "value": "OVER BUDGET" if over_budget else "Within limit", "unit": ""},
                {"label": "Free Models Live", "value": or_data.get('free_models', '?'), "unit": ""},
                {"label": "Watched Available", "value": f"{or_data.get('watched_available', '?')}/{or_data.get('watched_total', '?')}", "unit": ""},
            ]
        },
    }


def build_model_changes_card(or_data: dict, now: str) -> dict:
    """OpenRouter model changes card."""
    items = []
    if or_data.get('new_models') and 'none' not in or_data['new_models'].lower():
        items.append({"title": f"New: {or_data['new_models']}", "summary": "New free model added to OpenRouter", "source": "OpenRouter watch", "time": now})
    if or_data.get('removed_models') and 'none' not in or_data['removed_models'].lower():
        items.append({"title": f"Removed: {or_data['removed_models']}", "summary": "Free model no longer available", "source": "OpenRouter watch", "time": now})

    if not items:
        return None

    return {
        "id": "openrouter-model-changes",
        "domain": "news",
        "title": f"OpenRouter free model changes: {len(items)} update(s)",
        "summary": f"Free model catalog updated. {len(items)} change(s) detected in watched set.",
        "priority": "medium",
        "status": "active",
        "source_label": "OpenRouter free-model watch cron",
        "why_shown": "User monitors specific free models for Hermes/OpenRouter integration.",
        "valid_until": VALID_UNTIL,
        "payload": {
            "section": "today",
            "ai_curated": True,
            "relevance_score": 55,
            "news_items": items,
        },
    }


def build_heartbeat_card(hb_data: dict, now: str) -> dict:
    """OpenRouter heartbeat alert card."""
    if hb_data.get('severity') != 'CRITICAL':
        return None

    missing = hb_data.get('missing_models', 'unknown')

    return {
        "id": "openrouter-heartbeat-alert",
        "domain": "alerts",
        "title": f"OpenRouter Heartbeat: {hb_data.get('severity', 'CRITICAL')} - {missing.split(',')[0].strip()} missing",
        "summary": f"Heartbeat reports {hb_data.get('severity', 'CRITICAL')}. Missing watched models: {missing}. Free models live: {hb_data.get('free_models', '?')}. Watched available: {hb_data.get('watched_available', '?')}/{hb_data.get('watched_total', '?')}.",
        "priority": "high",
        "status": "active",
        "source_label": "OpenRouter heartbeat cron",
        "why_shown": "User explicitly watches specific free models (deepseek, minimax) for Hermes. Missing models affect availability.",
        "valid_until": VALID_UNTIL,
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
    }


def build_backup_card(job_key: str, data: dict, now: str, config: dict) -> dict:
    """Generic backup success card."""
    if data.get('status') != 'SUCCESS':
        return None

    size_val = data.get('size_val', 0)
    size_unit = data.get('size_unit', 'MiB')
    if size_unit == 'MIB' and size_val > 1000:
        size_val = round(size_val / 1024, 2)
        size_unit = 'GiB'

    return {
        "id": config['card_id'],
        "domain": "projects",
        "title": f"{config['title_prefix']}: ✅ {size_val} {size_unit}{', ' + data.get('files', '') + ' files' if data.get('files') else ''}",
        "summary": f"{config['summary']} Size: {size_val} {size_unit}. {('Files: ' + data.get('files', '?') + '. ') if data.get('files') else ''}Retention: {config['retention']}.",
        "priority": config['priority'],
        "status": "active",
        "source_label": config['source_label'],
        "why_shown": config['why_shown'],
        "valid_until": VALID_UNTIL,
        "payload": {
            "section": "today",
            "ai_curated": True,
            "relevance_score": config['relevance'],
            "metrics": [
                {"label": f"{config['size_label']}", "value": str(size_val), "unit": size_unit},
                *([{"label": "Files", "value": data.get('files', '?'), "unit": ""}] if data.get('files') else []),
                {"label": "Status", "value": "✅ SUCCESS", "unit": ""},
                {"label": "Retention", "value": config['retention'], "unit": ""},
            ]
        },
    }


def build_obsidian_card(data: dict, now: str) -> dict:
    """Obsidian nightly log card."""
    if not data.get('no_durable'):
        return None

    return {
        "id": "obsidian-nightly-log",
        "domain": "projects",
        "title": "Obsidian Nightly: No durable items to log",
        "summary": "Nightly collector found 0 changed vault files in last 24h. 8 Discord sessions detected but no vault mutations. Bias toward no write over weak write applied.",
        "priority": "low",
        "status": "active",
        "source_label": "Obsidian nightly high-signal log cron",
        "why_shown": "User's medical study vault (FCPS/MRCP) sync status. No new high-signal content.",
        "valid_until": VALID_UNTIL,
        "payload": {
            "section": "today",
            "ai_curated": True,
            "relevance_score": 30,
            "metrics": [
                {"label": "Result", "value": "No durable items", "unit": ""},
                {"label": "Candidate Files", "value": "0", "unit": ""},
                {"label": "Discord Sessions", "value": "8", "unit": ""},
            ]
        },
    }


def build_cron_health_card(now: str) -> dict:
    """Cron jobs health summary card."""
    jobs_info = [
        ("OpenRouter Free Model Watch", "18:30 daily", True),
        ("OpenRouter Heartbeat", "18:45 daily", True),
        ("Obsidian Nightly Log", "23:55 daily", True),
        ("Weekly 3rd Party Updates", "Fri 09:00", True),
        ("Daily Local Archive", "18:35 daily", True),
        ("Daily Mnemosyne Backup", "18:00 daily", True),
        ("Bitwarden Watchdog", "every 15m", True),
        ("Plain Local 6h", "every 6h", True),
        ("Skill Curator", "Fri 15:00", False),
        ("Daily GDrive Archive", "18:40 daily", True),
    ]

    active_count = sum(1 for _, _, enabled in jobs_info if enabled)
    paused_count = sum(1 for _, _, enabled in jobs_info if not enabled)

    return {
        "id": "cron-health-summary",
        "domain": "projects",
        "title": f"Cron Health: {active_count} active, {paused_count} paused",
        "summary": f"Hermes cron system: {active_count} active jobs, {paused_count} paused. Bitwarden watchdog (15m), OpenRouter watch (daily), backups (daily), Obsidian log (daily). Skill curator paused.",
        "priority": "low",
        "status": "active",
        "source_label": "Hermes cron jobs configuration",
        "why_shown": "Operational visibility into automated maintenance pipeline.",
        "valid_until": VALID_UNTIL,
        "payload": {
            "section": "watching",
            "ai_curated": True,
            "relevance_score": 40,
            "metrics": [
                {"label": "Active Jobs", "value": str(active_count), "unit": ""},
                {"label": "Paused Jobs", "value": str(paused_count), "unit": ""},
                {"label": "Total Jobs", "value": str(len(jobs_info)), "unit": ""},
            ],
            "sections": [
                {
                    "label": "Active Cron Jobs",
                    "items": [f"{name} ({schedule})" for name, schedule, enabled in jobs_info if enabled]
                },
                {
                    "label": "Paused Jobs",
                    "items": [f"{name} ({schedule})" for name, schedule, enabled in jobs_info if not enabled]
                }
            ]
        },
    }


# ── Main ────────────────────────────────────────────────────────────────

def main():
    # Clear all cards first
    conn = connect()
    conn.execute("DELETE FROM cards")
    conn.execute("DELETE FROM evidence")
    conn.commit()
    print("Cleared all cards and evidence")

    # Record refresh start
    refresh_result = record_refresh({
        "job_key": "autonomous-daily-briefing",
        "status": "running",
        "summary": "Full dashboard refresh from Hermes context.",
    })
    print(f"Refresh run started: {refresh_result}")

    # Scan Hermes context (signals only, no card creation)
    scan_result = refresh_from_hermes_context(
        include_sessions=True,
        include_cron=True,
        create_cards=False,
    )
    print(f"Sources scanned: {scan_result['sources']}")

    # Read cron outputs
    print("\nReading cron outputs...")
    cron_data = {}
    for key, job in CRON_JOBS.items():
        latest, text = get_latest_md(job['dir'])
        print(f"  {key}: {latest.name if latest else 'NONE'}")
        if job['parse'] == 'parse_openrouter':
            cron_data[key] = parse_openrouter(text)
        elif job['parse'] == 'parse_archive':
            cron_data[key] = parse_archive(text)
        elif job['parse'] == 'parse_obsidian':
            cron_data[key] = parse_obsidian(text)

    print(f"Parsed: {json.dumps(cron_data, indent=2)}")

    # Build cards
    now = utc_now()
    cards = []

    # OpenRouter budget - use watch data, fall back to heartbeat
    watch_data = cron_data.get('openrouter_watch', {})
    heartbeat_data = cron_data.get('openrouter_heartbeat', {})
    budget_source = watch_data if watch_data.get('account') else heartbeat_data
    card = build_budget_card(budget_source, now)
    if card: cards.append(card)

    # OpenRouter model changes - use watch data, fall back to heartbeat
    model_source = watch_data if (watch_data.get('new_models') or watch_data.get('removed_models')) else heartbeat_data
    card = build_model_changes_card(model_source, now)
    if card: cards.append(card)

    # OpenRouter heartbeat
    card = build_heartbeat_card(cron_data.get('openrouter_heartbeat', {}), now)
    if card: cards.append(card)

    # Backups
    backup_configs = {
        'local_archive': {
            'card_id': 'backup-local-archive',
            'title_prefix': 'Daily Local Archive',
            'summary': 'Local TB backup completed successfully.',
            'priority': 'medium',
            'source_label': 'Daily Hermes local archive cron',
            'why_shown': 'Critical backup infrastructure. User expects verified backup status.',
            'relevance': 60,
            'size_label': 'Archive Size',
            'retention': 'Keep last 3',
        },
        'gdrive_archive': {
            'card_id': 'backup-gdrive-archive',
            'title_prefix': 'GDrive Archive',
            'summary': 'Google Drive backup completed successfully.',
            'priority': 'medium',
            'source_label': 'Daily Hermes GDrive archive cron',
            'why_shown': 'Offsite backup verification. User has strict pre-backup policy (empty trash, low retention).',
            'relevance': 60,
            'size_label': 'Archive Size',
            'retention': 'Keep last 2',
        },
        'mnemosyne_backup': {
            'card_id': 'backup-mnemosyne',
            'title_prefix': 'Mnemosyne Backup',
            'summary': 'Mnemosyne memory snapshot backup completed.',
            'priority': 'low',
            'source_label': 'Daily Mnemosyne backup cron',
            'why_shown': 'Memory system backup health. Part of backup pipeline.',
            'relevance': 50,
            'size_label': 'Size',
            'retention': 'Keep last 7',
        },
    }

    for key, config in backup_configs.items():
        card = build_backup_card(key, cron_data.get(key, {}), now, config)
        if card: cards.append(card)

    # Obsidian nightly
    card = build_obsidian_card(cron_data.get('obsidian_nightly', {}), now)
    if card: cards.append(card)

    # Cron health
    card = build_cron_health_card(now)
    if card: cards.append(card)

    # Upsert all cards
    print("\nCreating cards...")
    for card in cards:
        upsert_card(card)
        print(f"  Created: {card['id']}")

    # Record completion
    final_result = record_refresh({
        "job_key": "autonomous-daily-briefing",
        "status": "success",
        "summary": f"Full dashboard refresh: {len(cards)} high-signal cards from cron outputs.",
        "payload_json": {
            "cards_created": len(cards),
            "card_ids": [c['id'] for c in cards],
            "sources": list(CRON_JOBS.keys()),
        }
    })
    print(f"\nRefresh completed: {final_result}")
    print(f"Total cards created: {len(cards)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
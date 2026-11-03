#!/usr/bin/env python3
"""Weekly planning refresh for Hermes Personal Dashboard - no LLM required."""

import sys
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, '/root/.hermes/products/hermes-personal-dashboard')

from personal_dashboard_core import (
    upsert_card,
    record_refresh,
    utc_now,
    parse_time,
    connect,
)

# Helper to get latest file by mtime
def get_latest_md(dir_path):
    files = list(Path(dir_path).glob('*.md'))
    if not files:
        return None, ""
    latest = max(files, key=lambda f: f.stat().st_mtime)
    return latest, latest.read_text()

# Start: record refresh run
refresh_result = record_refresh({
    "job_key": "autonomous-planning-refresh",
    "status": "running",
    "summary": "Weekly planning refresh - updating long-horizon cards.",
})
print(f"Refresh run started: {refresh_result}")

# Read relevant cron outputs
obs_latest, obsidian_text = get_latest_md('/root/.hermes/cron/output/dcb20be29ebb')
print(f"Obsidian: {obs_latest.name if obs_latest else 'NONE'}")

now_str = utc_now()
now = parse_time(now_str)

# Planning horizon: 2 weeks out
valid_until = (now + timedelta(weeks=2)).replace(hour=23, minute=59, second=0, microsecond=0)

updated_cards = []

# Card 1: Obsidian Study Plan (FCPS/MRCP)
has_study_content = 'No durable items to log' not in obsidian_text

upsert_card({
    "id": "planning-medical-study",
    "domain": "planning",
    "title": "Medical Study: FCPS/MRCP Weekly Plan",
    "summary": f"Obsidian vault sync: {'Active - new content logged' if has_study_content else 'No new content this week'}. Review FCPS Part 1 topics and MRCP Part 1 question banks. Target: 10-15 hours/week.",
    "priority": "medium",
    "status": "active",
    "source_label": "Obsidian nightly log + user profile",
    "why_shown": "User is a Bangladeshi doctor (Dr. Sagar) preparing for FCPS/MRCP exams. Weekly study plan is a core planning item.",
    "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "payload": {
        "section": "week",
        "ai_curated": True,
        "relevance_score": 70,
        "items": [
            {"title": "FCPS Part 1 - Medicine", "summary": "Review core medicine topics: CVS, RS, GI, Neurology", "source": "User profile", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "MRCP Part 1 - Question Bank", "summary": "Complete 50-100 questions weekly from Pastest/MRCPUK", "source": "User profile", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Obsidian Vault Sync", "summary": f"Weekly review of medical notes in Obsidian", "source": "Obsidian nightly cron", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
        ]
    },
})
updated_cards.append("planning-medical-study")

# Card 2: Hermes Infrastructure Maintenance Window
upsert_card({
    "id": "planning-infra-maintenance",
    "domain": "planning",
    "title": "Hermes Infra: Weekly Maintenance Window (Fri-Sat)",
    "summary": "Scheduled maintenance window for Hermes stack: backup verification, log rotation, skill curation, plugin updates. Best run Fri 15:00 - Sat 23:00 UTC.",
    "priority": "low",
    "status": "active",
    "source_label": "Hermes cron schedule analysis",
    "why_shown": "Operational planning for self-hosted Hermes infrastructure. User runs multiple cron jobs and plugins.",
    "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "payload": {
        "section": "week",
        "ai_curated": True,
        "relevance_score": 40,
        "items": [
            {"title": "Backup Verification", "summary": "Verify local + GDrive + Mnemosyne backups completed", "source": "Backup cron jobs", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Skill Curator Review", "summary": "Check paused skill-curator cron for pending proposals", "source": "Skill curator cron (paused)", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Plugin Updates", "summary": "Check hermes-personal-dashboard, mnemosyne-dashboard, telemetry for updates", "source": "Third-party tracker", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Log Rotation", "summary": "Clean old cron output files (>30 days)", "source": "Operational hygiene", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
        ]
    },
})
updated_cards.append("planning-infra-maintenance")

# Card 3: OpenRouter Model Watch - Planning
or_latest, openrouter_text = get_latest_md('/root/.hermes/cron/output/461aacc5be37')
hb_latest, heartbeat_text = get_latest_md('/root/.hermes/cron/output/4dd735fb568b')

has_model_changes = ('New free models:' in openrouter_text and 'none' not in openrouter_text.lower()) or \
                    ('Removed free models:' in openrouter_text and 'none' not in openrouter_text.lower())

upsert_card({
    "id": "planning-openrouter-models",
    "domain": "planning",
    "title": "OpenRouter: Free Model Catalog Planning",
    "summary": f"Free tier model availability: {'Changes detected this week' if has_model_changes else 'Stable'}. Monitor deepseek/deepseek-v4-flash:free, z-ai/glm-4.5-air:free, minimax/minimax-m2.5:free for return.",
    "priority": "low",
    "status": "active",
    "source_label": "OpenRouter watch + heartbeat cron",
    "why_shown": "Hermes uses OpenRouter free models. Missing watched models affect availability planning.",
    "valid_until": valid_until.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "updated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "payload": {
        "section": "week",
        "ai_curated": True,
        "relevance_score": 50,
        "items": [
            {"title": "Watched Models Missing", "summary": "deepseek-v4-flash, glm-4.5-air, minimax-m2.5 — monitor for return", "source": "Heartbeat cron", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Budget Planning", "summary": "Monthly $0.1120 spend vs $0.1000 limit — evaluate paid tier or usage reduction", "source": "Watch cron", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
            {"title": "Free Tier Alternatives", "summary": "27 free models live — test alternatives for missing watched models", "source": "Watch cron", "time": now.strftime("%Y-%m-%dT%H:%M:%SZ")},
        ]
    },
})
updated_cards.append("planning-openrouter-models")

# Record successful refresh
final_result = record_refresh({
    "job_key": "autonomous-planning-refresh",
    "status": "success",
    "summary": f"Updated {len(updated_cards)} planning cards. Valid until {valid_until.strftime('%Y-%m-%dT%H:%M:%SZ')}.",
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
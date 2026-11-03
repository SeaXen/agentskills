"""Account + state I/O for Synapse LMS downloads.

Manages per-account:
  - credentials  (accounts/<name>.creds, chmod 600)
  - state file   (accounts/<name>.json)

State schema:
  {
    "account_name": str,
    "username": str,
    "output_dir": str,
    "notes_subdir": str,
    "created_at": iso8601,
    "last_run": iso8601,
    "downloaded_videos": {stream_id: {...}},
    "downloaded_notes":  {file_id:    {...}},
  }
"""
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Default accounts directory (override with SYNAPSE_ACCOUNTS_DIR env var)
ACCOUNTS_DIR = Path(os.environ.get("SYNAPSE_ACCOUNTS_DIR", "/root/synapse_dl/accounts"))


def account_dir(name: str) -> Path:
    """Flat: each account is a file prefix under ACCOUNTS_DIR, not a subdirectory."""
    return ACCOUNTS_DIR


def creds_path(name: str) -> Path:
    return ACCOUNTS_DIR / f"{name}.creds"


def state_path(name: str) -> Path:
    return ACCOUNTS_DIR / f"{name}.json"


def list_accounts() -> list[str]:
    if not ACCOUNTS_DIR.exists():
        return []
    out = []
    for p in ACCOUNTS_DIR.iterdir():
        if p.is_file() and p.suffix == ".creds":
            name = p.stem
            if (ACCOUNTS_DIR / f"{name}.json").exists():
                out.append(name)
    return sorted(out)


def ensure_account(name: str, username: str, output_dir: str) -> Path:
    """Create creds + state files if missing. Returns the state file path."""
    ACCOUNTS_DIR.mkdir(parents=True, exist_ok=True)
    cp = creds_path(name)
    if not cp.exists():
        raise FileNotFoundError(
            f"Missing creds for '{name}' at {cp}\n"
            f"  Create: printf '%s' 'YOUR_PASSWORD' > {cp} && chmod 600 {cp}"
        )
    sp = state_path(name)
    if not sp.exists():
        now = datetime.now(timezone.utc).isoformat()
        sp.write_text(json.dumps({
            "account_name": name,
            "username": username,
            "output_dir": output_dir,
            "notes_subdir": "notes",
            "created_at": now,
            "last_run": now,
            "downloaded_videos": {},
            "downloaded_notes": {},
        }, indent=2))
    return sp


def load_state(name: str) -> dict:
    sp = state_path(name)
    if not sp.exists():
        raise FileNotFoundError(f"No state file for account '{name}' at {sp}")
    return json.loads(sp.read_text())


def save_state(name: str, state: dict) -> None:
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    state_path(name).write_text(json.dumps(state, indent=2, ensure_ascii=False))


def is_video_downloaded(state: dict, stream_id: str) -> bool:
    return stream_id in state.get("downloaded_videos", {})


def is_note_downloaded(state: dict, file_id: str) -> bool:
    return file_id in state.get("downloaded_notes", {})


def record_video(state: dict, **fields) -> None:
    state.setdefault("downloaded_videos", {})[fields["stream_id"]] = {
        "chapter_id": fields.get("chapter_id"),
        "chapter_name": fields.get("chapter_name"),
        "stream_id": fields["stream_id"],
        "title": fields.get("title"),
        "filename": fields.get("filename"),
        "size_bytes": fields.get("size_bytes"),
        "duration_s": fields.get("duration_s"),
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
    }


def record_note(state: dict, **fields) -> None:
    state.setdefault("downloaded_notes", {})[fields["file_id"]] = {
        "chapter_id": fields.get("chapter_id"),
        "chapter_name": fields.get("chapter_name"),
        "title": fields.get("title"),
        "filename": fields.get("filename"),
        "s3_key": fields.get("s3_key"),
        "size_bytes": fields.get("size_bytes"),
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
    }


def get_password(name: str) -> str:
    cp = creds_path(name)
    if not cp.exists():
        raise FileNotFoundError(
            f"No creds for account '{name}' at {cp}\n"
            f"  Create it: printf '%s' 'YOUR_PASSWORD' > {cp} && chmod 600 {cp}"
        )
    return cp.read_text().strip()

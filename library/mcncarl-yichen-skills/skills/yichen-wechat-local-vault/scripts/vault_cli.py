#!/usr/bin/env python3
"""
Unified read-only query CLI for the decrypted wechat-local-vault.

Mac commands read the local decrypted vault produced by decrypt_all_dbs.py.
The explicit snapshot subcommand uses a separately validated plaintext snapshot.
It does not touch the WeChat UI, send messages, or modify WeChat databases.
"""

from __future__ import annotations

import argparse
from collections import Counter
from contextvars import ContextVar
from datetime import datetime
import hashlib
import html
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import time
from xml.etree import ElementTree as ET

from wechat_schema import message_columns as shared_message_columns
from wechat_schema import message_table as shared_message_table
from message_display import ENVELOPE, HIDDEN_ID, PLACEHOLDER_TYPES, file_attachment_size, format_message_content, public_value, redact_text

try:
    import zstandard as zstd
except Exception:  # pragma: no cover - optional runtime dependency
    zstd = None


CONFIG_FILE = Path("~/.config/wechat-local-vault.json").expanduser()
DEFAULT_VAULT_DIR = Path("~/Library/Application Support/wechat-local-vault").expanduser()
DEFAULT_DECRYPTED_DIR = DEFAULT_VAULT_DIR / "decrypted/current"
DEFAULT_EXPORTS_DIR = Path("~/Documents/wechat-local-vault/exports").expanduser()
STATE_FILE = DEFAULT_VAULT_DIR / "state/vault_cli_last_check.json"
INCLUDE_IDENTIFIERS = ContextVar("include_identifiers", default=False)

ZSTD_MAGIC = b"\x28\xb5\x2f\xfd"
ZSTD_DECODER = zstd.ZstdDecompressor() if zstd else None
# Received files are kept per month; another file with the same name is saved as name(1).ext.
RENAMED_COPY_LIMIT = 20

MESSAGE_TYPE_FILTERS = {
    "text": (1,),
    "image": (3,),
    "voice": (34,),
    "video": (43,),
    "sticker": (47,),
    "location": (48,),
    "link": (49,),
    "file": (49, 6),
    "call": (50,),
    "system": (10000,),
}

TYPE_LABELS = {
    1: "文本",
    3: "图片",
    34: "语音",
    42: "名片",
    43: "视频",
    47: "表情",
    48: "位置",
    49: "链接/文件",
    50: "通话",
    10000: "系统",
    10002: "撤回",
}

FAVORITE_TYPE_MAP = {
    1: "文本",
    2: "图片",
    5: "文章",
    19: "名片",
    20: "视频号",
}

FAVORITE_TYPE_FILTERS = {
    "text": 1,
    "image": 2,
    "article": 5,
    "card": 19,
    "video": 20,
}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def load_config() -> dict:
    return load_json(CONFIG_FILE)


def resolve_decrypted_dir(value: str | None = None) -> Path:
    config = load_config()
    return Path(value or config.get("decrypted_dir") or DEFAULT_DECRYPTED_DIR).expanduser()


def resolve_exports_dir(value: str | None = None) -> Path:
    config = load_config()
    return Path(value or config.get("exports_dir") or DEFAULT_EXPORTS_DIR).expanduser()


def resolve_db_dir() -> Path | None:
    config = load_config()
    if config.get("db_base_path"):
        return Path(config["db_base_path"]).expanduser()
    if config.get("wxid"):
        return (
            Path("~/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files").expanduser()
            / config["wxid"]
            / "db_storage"
        )
    return None


def connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con


def table_columns(con: sqlite3.Connection, table: str) -> set[str]:
    try:
        return {row["name"] for row in con.execute(f"PRAGMA table_info([{table}])")}
    except sqlite3.Error:
        return set()


def table_exists(con: sqlite3.Connection, table: str) -> bool:
    row = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table,),
    ).fetchone()
    return bool(row)


def safe_name(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|]+", "_", value).strip()
    value = re.sub(r"\s+", "_", value)
    return value[:100] or "wechat_export"


def parse_time(value: str | None, *, end_of_day: bool = False) -> int | None:
    if not value:
        return None
    value = value.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(value, fmt)
            if fmt == "%Y-%m-%d" and end_of_day:
                dt = dt.replace(hour=23, minute=59, second=59)
            return int(dt.timestamp())
        except ValueError:
            pass
    raise SystemExit(f"时间格式不支持: {value}")


def split_msg_type(local_type: int | None) -> tuple[int, int]:
    try:
        value = int(local_type or 0)
    except (TypeError, ValueError):
        return 0, 0
    if value > 0xFFFFFFFF:
        return value & 0xFFFFFFFF, value >> 32
    return value, 0


def type_label(local_type: int | None) -> str:
    base_type, _ = split_msg_type(local_type)
    return TYPE_LABELS.get(base_type, f"type={local_type}")


def matches_type(local_type: int | None, filter_name: str | None) -> bool:
    if not filter_name:
        return True
    base_type, sub_type = split_msg_type(local_type)
    expected = MESSAGE_TYPE_FILTERS[filter_name]
    if base_type != expected[0]:
        return False
    return len(expected) == 1 or sub_type == expected[1]


def decode_bytes(value, compression_flag=None) -> bytes | None:
    """Stored body as bytes, zstd-decompressed when marked; None if decompression fails."""
    data = bytes(value)
    should_try_zstd = data.startswith(ZSTD_MAGIC) or compression_flag == 4
    if should_try_zstd and ZSTD_DECODER:
        try:
            return ZSTD_DECODER.decompress(data, max_output_size=1_000_000)
        except Exception:
            return None
    return data


def decode_value(value, compression_flag=None) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    data = decode_bytes(value, compression_flag)
    if data is None:
        return "[压缩消息解码失败]"
    try:
        return data.decode("utf-8", errors="replace")
    except Exception:
        return "[二进制内容]"


def output(data, fmt: str, render=None) -> None:
    # Text is rendered from the same public copy as JSON, so it hides the same identifiers.
    data = public_value(data, include_identifiers=INCLUDE_IDENTIFIERS.get())
    if fmt == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render(data) if render else data)


def visible(value) -> bool:
    return bool(value) and value != HIDDEN_ID


def load_contacts(decrypted_dir: Path) -> tuple[dict[str, dict], dict[int, str]]:
    contact_db = decrypted_dir / "contact/contact.db"
    if not contact_db.exists():
        return {}, {}
    contacts: dict[str, dict] = {}
    id_to_username: dict[int, str] = {}
    with connect(contact_db) as con:
        if not table_exists(con, "contact"):
            return {}, {}
        for row in con.execute("SELECT * FROM contact"):
            item = dict(row)
            username = item.get("username") or item.get("userName") or ""
            if not username:
                continue
            username = str(username)
            contact_id = item.get("id")
            if contact_id is not None:
                try:
                    id_to_username[int(contact_id)] = username
                except (TypeError, ValueError):
                    pass
            nick = str(item.get("nick_name") or item.get("nickname") or "")
            remark = str(item.get("remark") or "")
            alias = str(item.get("alias") or "")
            display = remark or nick or alias or username
            contacts[username] = {
                "username": username,
                "display_name": display,
                "remark": remark,
                "nick_name": nick,
                "alias": alias,
                "description": str(item.get("description") or ""),
                "avatar": str(item.get("small_head_url") or item.get("big_head_url") or ""),
                "is_group": "@chatroom" in username,
                "is_subscription": username.startswith("gh_"),
                "raw": item,
            }
    return contacts, id_to_username


def display_name(username: str, contacts: dict[str, dict]) -> str:
    return contacts.get(username, {}).get("display_name") or username


def resolve_chat(query: str, contacts: dict[str, dict]) -> dict | None:
    if query in contacts:
        return contacts[query]
    if query.startswith("wxid_") or "@chatroom" in query or query.startswith("gh_"):
        return {
            "username": query,
            "display_name": contacts.get(query, {}).get("display_name", query),
            "is_group": "@chatroom" in query,
        }
    q = query.lower()
    exact = [c for c in contacts.values() if q == c["display_name"].lower()]
    if exact:
        return exact[0]
    fuzzy = [
        c
        for c in contacts.values()
        if any(q in str(c.get(field) or "").lower() for field in ("display_name", "remark", "nick_name", "alias", "username"))
    ]
    return fuzzy[0] if fuzzy else None


def message_dbs(decrypted_dir: Path) -> list[Path]:
    return sorted((decrypted_dir / "message").glob("message_*.db"))


def message_table(username: str) -> str:
    return shared_message_table(username)


def load_name2id(con: sqlite3.Connection) -> dict[int, str]:
    mapping: dict[int, str] = {}
    if not table_exists(con, "Name2Id"):
        return mapping
    try:
        for row in con.execute("SELECT rowid, user_name FROM Name2Id"):
            if row["user_name"]:
                mapping[int(row["rowid"])] = str(row["user_name"])
    except sqlite3.Error:
        return {}
    return mapping


def username_for_table_from_contacts(table: str, contacts: dict[str, dict]) -> str:
    if not table.startswith("Msg_"):
        return ""
    target = table[4:]
    for username in contacts:
        if hashlib.md5(username.encode()).hexdigest() == target:
            return username
    return ""


def message_columns(con: sqlite3.Connection, table: str) -> dict[str, str]:
    return shared_message_columns(table_columns(con, table), legacy_mac=True)


def build_select_sql(table: str, cols: dict[str, str], start_ts: int | None, end_ts: int | None, keyword: str | None, type_name: str | None, limit: int | None, offset: int = 0, decode_compressed: bool = False) -> tuple[str, list]:
    select_parts = []
    aliases = {
        "local_id": "local_id",
        "server_id": "server_id",
        "local_type": "local_type",
        "create_time": "create_time",
        "real_sender_id": "real_sender_id",
        "message_content": "message_content",
        "compress_content": "compress_content",
        "compression_flag": "compression_flag",
    }
    for key, alias in aliases.items():
        col = cols.get(key)
        if col:
            select_parts.append(f"{col} AS {alias}")
        else:
            select_parts.append(f"NULL AS {alias}")
    clauses = []
    params: list = []
    if start_ts is not None and cols.get("create_time"):
        clauses.append(f"{cols['create_time']} >= ?")
        params.append(start_ts)
    if end_ts is not None and cols.get("create_time"):
        clauses.append(f"{cols['create_time']} <= ?")
        params.append(end_ts)
    if keyword and cols.get("message_content"):
        match = f"{cols['message_content']} LIKE ?"
        if decode_compressed and cols.get("local_type"):
            # LIKE never sees inside zstd BLOBs (long texts, links, files, forwards);
            # the caller decodes those rows and matches their readable text instead.
            skipped = ", ".join(str(base) for base in sorted(PLACEHOLDER_TYPES))
            match = f"({match} OR (typeof({cols['message_content']}) = 'blob' AND ({cols['local_type']} & 4294967295) NOT IN ({skipped})))"
        clauses.append(match)
        params.append(f"%{keyword}%")
    if type_name and cols.get("local_type"):
        expected = MESSAGE_TYPE_FILTERS[type_name]
        base = expected[0]
        clauses.append(f"({cols['local_type']} & 4294967295) = ?")
        params.append(base)
        if len(expected) > 1:
            sub = expected[1]
            clauses.append(f"(({cols['local_type']} >> 32) & 4294967295) = ?")
            params.append(sub)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    sql = f"SELECT {', '.join(select_parts)} FROM [{table}] {where} ORDER BY create_time DESC"
    if limit is not None:
        sql += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])
    return sql, params


def parse_sender_prefix(content: str) -> tuple[str, str]:
    if ":\n" not in content:
        return "", content
    sender, text = content.split(":\n", 1)
    # A stored group prefix is one username, not arbitrary prose or XML.
    # XML payloads can themselves end with ':\n'; treating the whole payload
    # as a sender used to erase their content. Keep an ambiguous body intact.
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}(?:@openim)?", sender):
        return sender, text
    return "", content


def received_file_path(month_dir: Path, title: str, expected_size: int | None) -> Path | None:
    """Locate a received file, including WeChat's renamed copies such as name(1).zip.

    The size recorded in the message decides between same-named files. Without it,
    only the exact name is trusted: a renamed copy may belong to another chat.
    """
    if Path(title).name != title or not month_dir.exists():
        return None
    stem, suffix = os.path.splitext(title)
    names = [title] + [f"{stem}({n}){suffix}" for n in range(1, RENAMED_COPY_LIMIT + 1)]
    root = month_dir.resolve()
    for name in names:
        candidate = month_dir / name
        try:
            if not candidate.is_file() or not candidate.resolve().is_relative_to(root):
                continue
            if expected_size is None:
                if name == title:
                    return candidate
            elif candidate.stat().st_size == expected_size:
                return candidate
        except OSError:
            continue
    return None


def media_hint(local_type: int | None, content: str, resolve_media: bool, db_dir: Path | None, chat_username: str, ts: int) -> str | None:
    base_type, _ = split_msg_type(local_type)
    if base_type == 3:
        return "[图片]"
    if base_type == 34:
        match = re.search(r'voicelength="(\d+)"', content or "")
        if match:
            return f"[语音，约 {int(match.group(1)) / 1000:.1f} 秒]"
        return "[语音]"
    if base_type == 43:
        return "[视频]"
    if base_type == 47:
        return "[表情]"
    if base_type == 48:
        return "[位置]"
    if base_type == 42:
        return "[名片]"
    if base_type == 50:
        return "[通话]"
    if base_type != 49 or not resolve_media or not db_dir:
        return None
    readable = format_message_content(local_type, content)
    if not readable.startswith("[文件] "):
        return None
    title = readable.removeprefix("[文件] ").strip()
    if not title:
        return None
    file_dir = db_dir.parent / "msg/file"
    if not file_dir.exists():
        return f"[文件] {title}"
    month_dir = file_dir / datetime.fromtimestamp(ts).strftime("%Y-%m")
    path = received_file_path(month_dir, title, file_attachment_size(content))
    return f"[文件] {title}\n{path}" if path else f"[文件] {title}"


def format_content(local_type: int | None, content: str, resolve_media: bool, db_dir: Path | None, chat_username: str, ts: int) -> str:
    hint = media_hint(local_type, content, resolve_media, db_dir, chat_username, ts)
    if hint:
        return format_message_content(1, hint)
    return format_message_content(local_type, content)


def row_to_message(row: sqlite3.Row, db_name: str, table: str, chat: dict, contacts: dict[str, dict], name2id: dict[int, str], resolve_media: bool = False, db_dir: Path | None = None) -> dict:
    local_type = row["local_type"]
    ts = int(row["create_time"] or 0)
    content = decode_value(row["message_content"], row["compression_flag"]) or decode_value(row["compress_content"], row["compression_flag"])
    prefix_sender, content = parse_sender_prefix(content)
    sender_username = ""
    sender_id = row["real_sender_id"]
    try:
        sender_username = name2id.get(int(sender_id), "")
    except (TypeError, ValueError):
        sender_username = ""
    if not sender_username:
        sender_username = prefix_sender
    if chat.get("is_group"):
        sender = display_name(sender_username, contacts) if sender_username else ""
    elif sender_username and sender_username != chat["username"]:
        sender = display_name(sender_username, contacts)
    elif str(sender_id) == "2":
        sender = "我"
    else:
        sender = chat["display_name"]
    text = format_content(local_type, content, resolve_media, db_dir, chat["username"], ts)
    return {
        "db": db_name,
        "table": table,
        "local_id": row["local_id"],
        "server_id": row["server_id"],
        "type": type_label(local_type),
        "local_type": local_type,
        "sender": sender,
        "sender_username": sender_username,
        "timestamp": ts,
        "time": datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S") if ts else "",
        "content": text,
    }


def find_chat_tables(decrypted_dir: Path, chat: dict) -> list[tuple[Path, str]]:
    target = message_table(chat["username"])
    matches = []
    for db_path in message_dbs(decrypted_dir):
        with connect(db_path) as con:
            if table_exists(con, target):
                matches.append((db_path, target))
    return matches


def collect_history(decrypted_dir: Path, chat: dict, start_ts: int | None, end_ts: int | None, limit: int, offset: int, type_name: str | None, resolve_media: bool = False) -> list[dict]:
    contacts, _ = load_contacts(decrypted_dir)
    db_dir = resolve_db_dir()
    rows = []
    candidate_limit = limit + offset
    for db_path, table in find_chat_tables(decrypted_dir, chat):
        with connect(db_path) as con:
            cols = message_columns(con, table)
            sql, params = build_select_sql(table, cols, start_ts, end_ts, None, type_name, candidate_limit, 0)
            name2id = load_name2id(con)
            for row in con.execute(sql, params):
                msg = row_to_message(row, db_path.name, table, chat, contacts, name2id, resolve_media, db_dir)
                if matches_type(msg["local_type"], type_name):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
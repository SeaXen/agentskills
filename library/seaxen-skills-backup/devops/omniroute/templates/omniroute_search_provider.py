"""OmniRoute Search — Hermes web search plugin.

Routes web_search through OmniRoute's /v1/search endpoint with automatic
failover across serper, brave, exa, tavily, searxng, and more.

Config: web.search_backend = "omniroute-search"
Env: OMNIRROUTE_SEARCH_URL, OMNIRROUTE_API_KEY (auto-discovered from DB)
"""

from __future__ import annotations
import logging
import os
from typing import Any, Dict
from agent.web_search_provider import WebSearchProvider

logger = logging.getLogger(__name__)
_DEFAULT_URL = "http://192.168.0.222:20128"


def _omniroute_search_url() -> str:
    try:
        from hermes_cli.config import get_env_value
        val = get_env_value("OMNIRROUTE_SEARCH_URL")
    except Exception:
        val = None
    if not val:
        val = os.getenv("OMNIRROUTE_SEARCH_URL", "")
    return (val or "").strip().rstrip("/") or _DEFAULT_URL


def _omniroute_api_key() -> str:
    try:
        from hermes_cli.config import get_env_value
        val = get_env_value("OMNIRROUTE_API_KEY")
    except Exception:
        val = None
    if val:
        return val.strip()
    val = os.getenv("OMNIRROUTE_API_KEY", "").strip()
    if val:
        return val
    try:
        import sqlite3
        db_path = "/mnt/tb/1Apps/omniroute/data/storage.sqlite"
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            row = conn.execute(
                "SELECT key FROM api_keys WHERE is_active=1 ORDER BY created_at LIMIT 1"
            ).fetchone()
            conn.close()
            if row and row[0]:
                return row[0]
    except Exception as exc:
        logger.debug("OmniRoute API key auto-discovery failed: %s", exc)
    return ""


class OmniRouteSearchProvider(WebSearchProvider):
    @property
    def name(self) -> str:
        return "omniroute-search"

    @property
    def display_name(self) -> str:
        return "OmniRoute Search"

    def is_available(self) -> bool:
        return bool(_omniroute_api_key())

    def supports_search(self) -> bool:
        return True

    def supports_extract(self) -> bool:
        return False

    def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        import httpx
        base_url = _omniroute_search_url()
        api_key = _omniroute_api_key()
        if not api_key:
            return {"success": False, "error": "OmniRoute API key not found."}
        url = f"{base_url}/v1/search"
        try:
            resp = httpx.post(url, json={"query": query, "max_results": min(limit, 20)},
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                timeout=15)
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            return {"success": False, "error": f"OmniRoute HTTP {exc.response.status_code}"}
        except httpx.RequestError as exc:
            return {"success": False, "error": f"Could not reach OmniRoute: {exc}"}
        try:
            data = resp.json()
        except Exception:
            return {"success": False, "error": "Could not parse OmniRoute response"}
        if "error" in data and isinstance(data["error"], dict):
            return {"success": False, "error": f"OmniRoute: {data['error'].get('message', '')}"}
        raw = data.get("results", [])
        web_results = [
            {"title": str(r.get("title", "")), "url": str(r.get("url", "")),
             "description": str(r.get("snippet", r.get("content", ""))),
             "position": r.get("position", i + 1)}
            for i, r in enumerate(raw[:limit])
        ]
        return {"success": True, "data": {"web": web_results}}

    def get_setup_schema(self) -> Dict[str, Any]:
        return {
            "name": "OmniRoute Search",
            "badge": "free · multi-provider failover",
            "tag": "Routes through OmniRoute /v1/search with auto-failover.",
            "env_vars": [
                {"key": "OMNIRROUTE_SEARCH_URL", "prompt": "OmniRoute URL", "url": None},
                {"key": "OMNIRROUTE_API_KEY", "prompt": "API key (auto-discovered)", "url": None},
            ],
        }

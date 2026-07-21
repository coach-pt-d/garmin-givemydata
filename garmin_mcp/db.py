"""
SQLite database layer for Garmin MCP server.

Provides connection management, schema initialization, upsert helpers for each
data type, a save_to_db() router, and a generic query helper.

35 dedicated tables — every Garmin endpoint maps to exactly one table.
"""

import json
import logging
import sqlite3
from pathlib import Path
from typing import Any, Optional


def _default_db_path() -> str:
    """Find the database using the same logic as the CLI."""
    import os

    env_dir = os.environ.get("GARMIN_DATA_DIR")
    if env_dir:
        return str(Path(env_dir) / "garmin.db")

    cwd = Path.cwd()
    if (cwd / "garmin.db").exists() or (cwd / ".env").exists() or (cwd / "garmin_givemydata.py").exists():
        return str(cwd / "garmin.db")

    home_dir = Path.home() / ".garmin-givemydata"
    home_dir.mkdir(parents=True, exist_ok=True)
    return str(home_dir / "garmin.db")


DB_PATH = _default_db_path()

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Connection helpers
# ---------------------------------------------------------------------------


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Return a sqlite3 connection with WAL mode and Row factory enabled."""
    conn = sqlite3.connect(db_path or DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

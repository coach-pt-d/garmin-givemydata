"""
Import script: loads garmin_data_for_ai.json into the SQLite database.

Uses save_to_db() to route each dataset to the correct table.

Usage:
    python -m garmin_mcp.import_json [json_path]

If json_path is omitted, defaults to garmin_data_for_ai.json in the project root.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from garmin_mcp.db import get_connection, init_db, save_to_db

PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_JSON_PATH = PROJECT_ROOT / "garmin_data_for_ai.json"

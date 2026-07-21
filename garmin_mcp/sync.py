"""
Incremental sync module for Garmin MCP server.

Fetches today's and yesterday's data from Garmin Connect and saves it
directly to SQLite via save_to_db().
"""

import logging
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from garmin_mcp.db import DB_PATH, get_connection, init_db, save_to_db

logger = logging.getLogger(__name__)

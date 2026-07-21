#!/usr/bin/env python3
"""
garmin-givemydata: Get your Garmin Connect data back.

Smart sync: if the database is empty, fetches all historical data year by year.
If the database already has data, fetches only what's new since the last sync.

Data goes straight to SQLite — each batch is committed immediately so a crash
never loses previously fetched data.

Usage:
    python garmin_givemydata.py                    # Smart sync (all data)
    python garmin_givemydata.py --profile health   # Only health metrics
    python garmin_givemydata.py --profile activities  # Only activities
    python garmin_givemydata.py --export ./output  # Export from DB to CSV+JSON
    python garmin_givemydata.py --export-all ./out  # Export CSV+JSON+FIT
"""

import argparse
import logging
import os
import sys
import time
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from garmin_client import GarminClient
from garmin_mcp.db import DB_PATH, get_connection, init_db, record_fit_parse, save_to_db
from garmin_mcp.db import query as db_query

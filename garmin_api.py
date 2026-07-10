#!/usr/bin/env python3
import sqlite3
import json
from datetime import datetime, timedelta

DB_PATH = "garmin.db"

def get_latest_sleep(days=7):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT calendar_date, sleep_score_overall, deep_sleep_seconds, light_sleep_seconds, rem_sleep_seconds,
               average_hr_sleep, average_spo2, body_battery_change, sleep_need_minutes, resting_heart_rate
        FROM sleep 
        ORDER BY calendar_date DESC 
        LIMIT ?
    """, (days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_latest_hrv(days=7):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT calendar_date, weekly_avg, last_night, status, feedback_phrase, baseline_low, baseline_upper
        FROM hrv 
        ORDER BY calendar_date DESC 
        LIMIT ?
    """, (days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_recovery_metrics(days=7):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT calendar_date, score, level, feedback_short, hrv_factor_percent, sleep_history_factor_percent,
               stress_history_factor_percent, recovery_time
        FROM training_readiness 
        ORDER BY calendar_date DESC 
        LIMIT ?
    """, (days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_body_battery(days=7):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT calendar_date, charged, drained, highest, lowest, most_recent, at_wake, during_sleep
        FROM body_battery 
        ORDER BY calendar_date DESC 
        LIMIT ?
    """, (days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_daily_summary(days=7):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT calendar_date, total_steps, total_kilocalories, active_kilocalories, 
               min_heart_rate, max_heart_rate, resting_heart_rate, average_stress_level,
               moderate_intensity_minutes, vigorous_intensity_minutes, body_battery_most_recent
        FROM daily_summary 
        ORDER BY calendar_date DESC 
        LIMIT ?
    """, (days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

if __name__ == "__main__":
    print("=== Latest Sleep Data ===")
    print(json.dumps(get_latest_sleep(3), indent=2, default=str))
    
    print("\n=== Latest HRV ===")
    print(json.dumps(get_latest_hrv(3), indent=2, default=str))
    
    print("\n=== Recovery Metrics ===")
    print(json.dumps(get_recovery_metrics(3), indent=2, default=str))
    
    print("\n=== Body Battery ===")
    print(json.dumps(get_body_battery(3), indent=2, default=str))
    
    print("\n=== Daily Summary ===")
    print(json.dumps(get_daily_summary(3), indent=2, default=str))

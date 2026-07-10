#!/usr/bin/env python3
import json
from datetime import datetime
from garmin_api import (
    get_latest_sleep,
    get_latest_hrv,
    get_recovery_metrics,
    get_body_battery,
    get_daily_summary
)

# Generate daily report
report = {
    "generated_at": datetime.now().isoformat(),
    "sleep_last_3_nights": get_latest_sleep(3),
    "hrv_last_7_days": get_latest_hrv(7),
    "body_battery_last_7_days": get_body_battery(7),
    "daily_summary_last_7_days": get_daily_summary(7),
    "recovery_metrics_last_7_days": get_recovery_metrics(7)
}

# Save to file
with open("garmin_report.json", "w") as f:
    json.dump(report, f, indent=2, default=str)

print("✅ Report saved to garmin_report.json")

#!/usr/bin/env python3
import json
import sys
from garmin_api import (
    get_latest_sleep,
    get_latest_hrv,
    get_recovery_metrics,
    get_body_battery,
    get_daily_summary
)

def handle_tool_call(tool_name, args):
    days = args.get("days", 7)
    
    if tool_name == "get_sleep":
        return get_latest_sleep(days)
    elif tool_name == "get_hrv":
        return get_latest_hrv(days)
    elif tool_name == "get_recovery":
        return get_recovery_metrics(days)
    elif tool_name == "get_body_battery":
        return get_body_battery(days)
    elif tool_name == "get_daily_summary":
        return get_daily_summary(days)
    else:
        return {"error": f"Unknown tool: {tool_name}"}

if __name__ == "__main__":
    # Simple JSON-based interface for Claude
    for line in sys.stdin:
        try:
            request = json.loads(line.strip())
            tool_name = request.get("tool")
            args = request.get("args", {})
            result = handle_tool_call(tool_name, args)
            print(json.dumps({"result": result}))
        except Exception as e:
            print(json.dumps({"error": str(e)}))

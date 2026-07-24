import json
import os
from datetime import datetime

REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)


def save_report(module, action, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report = {
        "module": module,
        "action": action,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    }

    filename = f"{module.lower()}_{timestamp}.json"

    path = os.path.join(REPORT_DIR, filename)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return path

import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, config):
        self.file_path = config.get("report_path", "reports/trade_report.json")

    def generate(self, summary):
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": summary
        }
        with open(self.file_path, "w") as f:
            json.dump(report, f, indent=4)
        return report

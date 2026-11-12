#!/usr/bin/env python3
"""Lab-only regex preflight checker. Does NOT intercept actual USB/email/cloud transfers."""
import sys, re, json, uuid, subprocess
from pathlib import Path
from datetime import datetime, timezone
if len(sys.argv) != 3 or sys.argv[2] not in ("USB", "EMAIL", "CLOUD"):
    sys.exit("Usage: p2-dlp-check.py FILE USB|EMAIL|CLOUD")
file, channel = sys.argv[1:]
data = Path(file).read_text(errors="replace")
patterns = {
    "FIN": r"\bFIN\s*[:=]\s*[A-Z0-9]{7}\b",
    "TEST_FIN": r"\bFAKE-FIN-TEST-\d{3}\b",
    "CARD": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
}
matches = [name for name, pattern in patterns.items() if re.search(pattern, data, re.I)]
if matches:
    event = {
        "time": datetime.now(timezone.utc).isoformat(),
        "severity": "HIGH", "action": "BLOCK", "channel": channel,
        "matches": matches, "ticket_id": str(uuid.uuid4()),
    }
    logdir = Path("/var/log/p2-dlp")
    logdir.mkdir(mode=0o700, exist_ok=True)
    with (logdir / "alerts.jsonl").open("a") as f:
        f.write(json.dumps(event) + "\n")
    subprocess.run(["logger", "-p", "user.err", "-t", "P2-DLP", json.dumps(event)], check=False)
    print("BLOCKED | HIGH ALERT | Ticket:", event["ticket_id"])
    sys.exit(2)
print("ALLOW | No sensitive data detected")

from garminconnect import Garmin
from dotenv import load_dotenv
import os, json
from datetime import date, timedelta
import sys

# Load environment variables
load_dotenv()
email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

# Authenticate Garmin client
client = Garmin(email, password)
client.login()

# Generate last 7 dates including today
today = date.today()
dates = [today - timedelta(days=i) for i in range(6, -1, -1)]

# Fetch and format sleep data
sleep_summary = []
for d in dates:
    raw = client.get_sleep_data(d.isoformat())
    dto = raw.get("dailySleepDTO", {})
    if dto and dto.get("sleepTimeSeconds"):
        sleep_summary.append({
            "date": d.isoformat(),
            "hours": round(dto["sleepTimeSeconds"] / 3600, 1)
        })

# Write to file
with open("sleep.json", "w") as f:
    json.dump(sleep_summary, f, indent=2)

print("✅ Weekly sleep data written to sleep.json")


if not sleep or not isinstance(sleep, list) or len(sleep) == 0:
    print("❌ Sleep data is empty or malformed.")
    sys.exit(1)

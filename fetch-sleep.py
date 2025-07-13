from garminconnect import Garmin
from dotenv import load_dotenv
import os, json
from datetime import date

load_dotenv()

email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

client = Garmin(email, password)
client.login()

today = date.today().isoformat()
sleep = client.get_sleep_data(today)

with open("sleep.json", "w") as f:
    json.dump(sleep, f, indent=2)

print("✅ Sleep data written to sleep.json")

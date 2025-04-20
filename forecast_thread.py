import requests
import time
import yaml
from db import get_db
from datetime import datetime

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def fetch_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[ERROR] Failed to fetch forecast for {city}: {response.status_code}")
        return None

def run_forecast_thread():
    config = load_config()
    db = get_db()
    forecast_col = db.forecast_data

    while True:
        print("[INFO] Forecast thread running...")
        for city in config["cities"]:
            data = fetch_forecast(city, config["api_key"])
            if data:
                timestamp = datetime.utcnow().isoformat()
                forecast_col.insert_one({
                    "city": city,
                    "timestamp": timestamp,
                    "data": data
                })
                print(f"[INFO] Forecast saved for {city} at {timestamp}")
        time.sleep(config["refresh_interval"])


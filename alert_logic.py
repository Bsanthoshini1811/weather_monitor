from db import get_db
import time

def run_alert_checker():
    db = get_db()
    forecast_col = db.forecast_data

    while True:
        print("[INFO] Alert checker thread running...")
        forecasts = forecast_col.find().sort("timestamp", -1).limit(3)
        for forecast_doc in forecasts:
            city = forecast_doc["city"]
            for entry in forecast_doc["data"].get("list", []):
                temp_k = entry["main"]["temp_min"]
                temp_f = (temp_k - 273.15) * 9/5 + 32
                weather_conditions = [w["main"] for w in entry["weather"]]

                if "Rain" in weather_conditions or "Snow" in weather_conditions or temp_f < 32:
                    print(f"⚠️ Alert: {city} may have {' / '.join(weather_conditions)} at {entry['dt_txt']}")
        time.sleep(300)

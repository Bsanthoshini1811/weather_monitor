from db import get_db
import matplotlib.pyplot as plt

def plot_city_forecast(city_name):
    db = get_db()
    data = db.forecast_data.find({"city": city_name}).sort("timestamp", -1).limit(10)

    for doc in data:
        forecast = doc["data"]
        dates, temps = [], []
        for entry in forecast["list"]:
            dates.append(entry["dt_txt"])
            temp_k = entry["main"]["temp"]
            temp_f = (temp_k - 273.15) * 9/5 + 32
            temps.append(temp_f)

        plt.figure(figsize=(12,6))
        plt.plot(dates, temps, marker='o')
        plt.xticks(rotation=45)
        plt.title(f"Forecast Temperatures for {city_name}")
        plt.xlabel("Date/Time")
        plt.ylabel("Temp (°F)")
        plt.tight_layout()
        plt.grid()
        plt.show()

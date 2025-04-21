from nicegui import ui
from db import get_db
import matplotlib.pyplot as plt
import io
from PIL import Image
import base64

db = get_db()

def get_available_cities():
    return db.forecast_data.distinct("city")

def get_latest_forecast(city):
    doc = db.forecast_data.find({"city": city}).sort("timestamp", -1).limit(1)[0]
    return doc["data"]

def plot_forecast(city):
    forecast = get_latest_forecast(city)
    dates, temps = [], []
    for entry in forecast["list"]:
        dates.append(entry["dt_txt"])
        temp_k = entry["main"]["temp"]
        temp_f = (temp_k - 273.15) * 9/5 + 32
        temps.append(temp_f)

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(dates, temps, marker='o')
    ax.set_xticklabels(dates, rotation=45, fontsize=8)
    ax.set_title(f"Forecast for {city}")
    ax.set_ylabel("Temperature (°F)")
    ax.grid(True)

    buf = io.BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def display_alerts(city):
    doc = db.forecast_data.find({"city": city}).sort("timestamp", -1).limit(1)[0]
    alerts = []
    for entry in doc["data"]["list"]:
        temp_k = entry["main"]["temp_min"]
        temp_f = (temp_k - 273.15) * 9/5 + 32
        weather_main = [w["main"] for w in entry["weather"]]
        if temp_f < 32 or any(w in ["Rain", "Snow"] for w in weather_main):
            alerts.append(f"⚠️ {entry['dt_txt']} — {'/'.join(weather_main)} @ {temp_f:.1f}°F")
    return alerts

# --- UI Components ---
ui.label("🌦️ Real-Time Weather Dashboard").style('font-size: 30px; font-weight: bold;')

city = ui.select(get_available_cities(), label='Select City')

with ui.row():
    plot_button = ui.button("Show Forecast Plot")
    alert_button = ui.button("Show Alerts")

plot_output = ui.image()
alerts_output = ui.column()

def update_plot():
    img_data = plot_forecast(city.value)
    plot_output.source = f'data:image/png;base64,{img_data}'

def update_alerts():
    alerts_output.clear()
    for alert in display_alerts(city.value):
        alerts_output.append(ui.label(alert).style('color: red'))

# ✅ Use correct event binding
plot_button.on_click(update_plot)
alert_button.on_click(update_alerts)

ui.run()
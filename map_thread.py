import requests
import time
import yaml
from datetime import datetime
import os

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def download_map(layer, api_key):
    # Static tile example (centered on a rough location)
    url = f"https://tile.openweathermap.org/map/{layer}/5/10/10.png?appid={api_key}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        filename = f"data/{layer}_{timestamp}.png"
        os.makedirs("data", exist_ok=True)
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"[INFO] Map downloaded: {filename}")
    else:
        print(f"[ERROR] Failed to fetch map layer {layer}: {response.status_code}")

def run_map_thread():
    config = load_config()
    while True:
        print("[INFO] Map thread running...")
        for layer in config["map_layers"]:
            download_map(layer, config["api_key"])
        time.sleep(config["refresh_interval"])

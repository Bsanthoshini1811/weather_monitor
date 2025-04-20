import threading
from forecast_thread import run_forecast_thread
from map_thread import run_map_thread
from alert_logic import run_alert_checker

if __name__ == "__main__":
    print("[INFO] Starting weather monitoring system...")

    t1 = threading.Thread(target=run_forecast_thread)
    t2 = threading.Thread(target=run_map_thread)
    t3 = threading.Thread(target=run_alert_checker)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

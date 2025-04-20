# Weather Monitoring System (OpenWeatherMap API)

## Overview:
This repository contains a multithreaded weather monitoring system built using Python and MongoDB. The objective of the project is to track real-time weather conditions for selected cities using the OpenWeatherMap API, detect extreme weather events, and store historical weather data. The system also supports satellite map downloads and temperature trend visualizations. It is designed to be modular, scalable, and configuration-driven.

The project demonstrates how to integrate REST APIs with Python, use concurrency for efficient data fetching, store structured data in NoSQL databases, trigger real-time alerts, and visualize time-series data. It also includes best practices in project organization, security (API key handling), and configuration management.


## Project description:

This project is divided into four major modules:
1. Configuration and Setup
2. Forecast Fetching
3. Weather Map Downloading
4. Alerting and Visualization

**1. Configuration:**  
The system uses a `config.yaml` file to define the list of cities, API key, refresh interval, and map layers to be downloaded. This makes the system flexible and easy to adapt without changing the codebase.

**2. Forecast Fetching:**  
Using the OpenWeatherMap Forecast API, the system fetches 5-day weather forecasts at 3-hour intervals for each city. The response is stored in MongoDB (`forecast_data` collection) with UTC timestamps. Each forecast entry includes temperature, humidity, and weather conditions.

**3. Weather Map Downloading:**  
The system supports satellite map tile downloads such as `precipitation_new` and `clouds_new`. These maps are downloaded at regular intervals and saved as PNG files locally under the `data/` directory. The map downloader runs on a separate thread to avoid blocking the forecast thread.

**4. Alerting and Visualization:**  
The alert system monitors for rain, snow, and temperatures below 32°F (0°C) and prints warnings in real time. A plotting module allows users to generate a time-series graph of temperatures for any city, using `matplotlib`.


## Project Structure

The repository is organized as follows:

- **data/**: Contains weather map image files (ignored in `.gitignore`)
- **alert_logic.py**: Contains alert-checking logic for rain, snow, and freezing temps.
- **config.yaml**: Local configuration file with cities, API key, and refresh settings (excluded from repo).
- **config.example.yaml**: Template config file for safe sharing.
- **db.py**: MongoDB connection setup.
- **forecast_thread.py**: Thread logic for fetching forecast data.
- **map_thread.py**: Thread logic for downloading weather maps.
- **main.py**: Launches all threads (forecast, alert, and maps).
- **plot.py**: Provides temperature trend visualization for a city.
- **requirements.txt**: Lists required Python packages.


## Results

The system successfully:
- Stores timestamped forecast data for multiple cities.
- Downloads and maintains a directory of weather map images.
- Triggers alerts for snow, rain, and freezing weather.
- Visualizes forecast data using time-series plots.

All outputs (data and alerts) are available in real time through the terminal and visualizations via matplotlib.


## Contributing

Feel free to fork the repository, raise issues, or submit pull requests. Contributions that improve performance, add new alert types, or extend visualizations are welcome.



## Acknowledgments

This project uses data from the OpenWeatherMap API. Thanks to the open-source community for providing the tools and libraries that made this project possible.


## Contact

For any questions or feedback, please contact [bs441@usf.edu].

Happy Weather Hacking! ☀️❄️🌧️


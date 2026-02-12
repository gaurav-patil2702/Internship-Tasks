
"""
Internship Task 1 - API Integration and Data Visualization
Public API Used: OpenWeatherMap
"""

import requests
import matplotlib.pyplot as plt

API_KEY = "2ca399e158b8041d160926f8ee185847"
CITY = "Mumbai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = []
temperatures = []

for item in data["list"][:8]:  # next 24 hours (3-hour intervals)
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])

plt.figure()
plt.plot(dates, temperatures)
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title("24-Hour Temperature Forecast")
plt.tight_layout()
plt.show()

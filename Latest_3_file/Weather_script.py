import requests

# 1. API URL for Hyderabad (30 days history)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 17.3850,     # Hyderabad latitude
    "longitude": 78.4867,    # Hyderabad longitude
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto",
    "past_days": 30         # last 30 days
}

# 2. Get data from API
response = requests.get(url, params=params)
data = response.json()

# 3. Extract values
dates = data["daily"]["time"]
max_temps = data["daily"]["temperature_2m_max"]
min_temps = data["daily"]["temperature_2m_min"]

# 4. Print all 30 days
print("=== Day-wise Weather Report (Last 30 Days, Hyderabad) ===")
for i in range(len(dates)):
    print(f"{dates[i]}  -->  Min: {min_temps[i]}°C , Max: {max_temps[i]}°C")

# 5. Find highest and lowest temperatures
highest_temp = max(max_temps)
lowest_temp = min(min_temps)

# 6. Find the days for highest & lowest temps
highest_day = dates[max_temps.index(highest_temp)]
lowest_day = dates[min_temps.index(lowest_temp)]

print("\n=== Summary ===")
print(f"Highest temperature: {highest_temp}°C on {highest_day}")
print(f"Lowest temperature : {lowest_temp}°C on {lowest_day}")

# 7. Detect anomalies (drastic changes > 7°C in max temp)
print("\n=== Anomalies Detected ===")
for i in range(1, len(max_temps)):
    diff = max_temps[i] - max_temps[i-1]
    if abs(diff) > 3:  # sudden jump/drop
        print(f"On {dates[i]}: Max temp changed by {diff:+.1f}°C "
              f"(from {max_temps[i-1]}°C to {max_temps[i]}°C)")

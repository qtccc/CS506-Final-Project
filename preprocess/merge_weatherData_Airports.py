import pandas as pd

# File paths
airport_file = 'Filtered_Airports_with_Coordinates.csv'
hourly_weather_file = 'Hourly_Weather_Data.csv'
daily_weather_file = 'Daily_Weather_Data.csv'

# Load airport and weather data
airports = pd.read_csv(airport_file)
hourly_weather = pd.read_csv(hourly_weather_file)
daily_weather = pd.read_csv(daily_weather_file)

# Merge hourly weather data with airports based on 'date'
hourly_merged = pd.merge(
    airports,
    hourly_weather,
    how='cross'
)

# Merge daily weather data with airports based on 'date'
daily_merged = pd.merge(
    airports,
    daily_weather,
    how='cross'
)

# Save merged data
hourly_merged.to_csv('Airports_Hourly_Weather.csv', index=False)
daily_merged.to_csv('Airports_Daily_Weather.csv', index=False)

print("Merged airport data with hourly and daily weather data saved.")

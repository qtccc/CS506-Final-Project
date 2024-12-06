import pandas as pd

airport_file = 'Filtered_Airports_with_Coordinates.csv'
hourly_weather_file = 'Hourly_Weather_Data.csv'
daily_weather_file = 'Daily_Weather_Data.csv'

airports = pd.read_csv(airport_file)
hourly_weather = pd.read_csv(hourly_weather_file)
daily_weather = pd.read_csv(daily_weather_file)

hourly_merged = pd.merge(
    airports,
    hourly_weather,
    how='cross'
)

daily_merged = pd.merge(
    airports,
    daily_weather,
    how='cross'
)

hourly_merged.to_csv('Airports_Hourly_Weather.csv', index=False)
daily_merged.to_csv('Airports_Daily_Weather.csv', index=False)

print("Merged airport data with hourly and daily weather data saved.")

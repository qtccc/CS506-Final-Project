import pandas as pd

# Load the datasets
airports = pd.read_csv('Filtered_Airports_with_Coordinates.csv')
hourly_weather = pd.read_csv('Hourly_Weather_Data.csv')
daily_weather = pd.read_csv('Daily_Weather_Data.csv')

# Preview
print(airports.head())
print(hourly_weather.head())
print(daily_weather.head())


# Purpose: Preview and validate the datasets to ensure they have consistent formatting and fields before processing.
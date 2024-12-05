import requests
import pandas as pd
import time

# Input: Airports with latitude and longitude
airport_data_file = '/workspaces/CS506-Final-Project/Merged_Airport_Data.csv'
output_weather_file = '/workspaces/CS506-Final-Project/Weather_Data.csv'

# Load airport data
airport_data = pd.read_csv(airport_data_file)

# Base URL for the weather API
base_url = "https://api.open-meteo.com/v1/forecast"

# List to store weather data
weather_records = []

# Iterate over each airport to fetch weather data
for index, row in airport_data.iterrows():
    params = {
        "latitude": row['Latitude'],
        "longitude": row['Longitude'],
        "start_date": "2023-01-01",  # Change to your desired date range
        "end_date": "2023-12-31",
        "hourly": "temperature_2m,precipitation,wind_speed_10m,visibility"
    }
    print(f"Fetching weather data for: {row['AirportName']} ({row['Latitude']}, {row['Longitude']})")
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            for hourly_data in weather_data['hourly']:
                weather_records.append({
                    "AirportName": row['AirportName'],
                    "Latitude": row['Latitude'],
                    "Longitude": row['Longitude'],
                    "Timestamp": hourly_data['time'],
                    "Temperature": hourly_data['temperature_2m'],
                    "Precipitation": hourly_data['precipitation'],
                    "WindSpeed": hourly_data['wind_speed_10m'],
                    "Visibility": hourly_data['visibility']
                })
        else:
            print(f"Failed to fetch data for {row['AirportName']}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data for {row['AirportName']}: {e}")
    time.sleep(1)  # Pause to avoid rate limits

# Save weather data to a CSV file
weather_df = pd.DataFrame(weather_records)
weather_df.to_csv(output_weather_file, index=False)

print(f"Weather data saved to: {output_weather_file}")

import pandas as pd

# File paths
flight_file = 'data/Flight_Delay_Data.csv'
airport_weather_file = 'Airports_Hourly_Weather.csv'

# Load datasets
flights = pd.read_csv(flight_file)
airport_weather = pd.read_csv(airport_weather_file)

# Merge on OriginAirportSeqID and date
merged_data = pd.merge(
    flights,
    airport_weather,
    how='left',
    left_on=['OriginAirportSeqID', 'FlightDate'],
    right_on=['SeqID', 'date']
)

# Save the final dataset
merged_data.to_csv('processed_flight_weather_data.csv', index=False)
print("Processed flight and weather data saved.")

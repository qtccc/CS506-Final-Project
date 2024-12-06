import pandas as pd
import os

# Path to weather data
weather_file = "Airports_Daily_Weather.csv"
weather_df = pd.read_csv(weather_file)

# Convert the weather date to match FlightDate with time
weather_df['date'] = pd.to_datetime(weather_df['date']).dt.tz_localize(None)  # Remove timezone info

# Path to the flight data directory
data_dir = "../data"
output_dir = "../processed_data"  # Save output files to a new directory

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each month's CSV file
for month_file in os.listdir(data_dir):
    if month_file.endswith(".csv"):
        month_path = os.path.join(data_dir, month_file)
        
        # Load flight data
        flight_df = pd.read_csv(month_path)
        
        # Convert FlightDate to datetime and ensure it's timezone-naive
        flight_df['FlightDate'] = pd.to_datetime(flight_df['FlightDate'], format='%m/%d/%y', errors='coerce')
        
        # Perform the join on both `OriginAirportSeqID` and `date`
        merged_df = pd.merge(
            flight_df,
            weather_df,
            how="left",
            left_on=["OriginAirportSeqID", "FlightDate"],
            right_on=["SeqID", "date"]
        )
        
        # Save the merged data to a new file
        output_path = os.path.join(output_dir, month_file)
        merged_df.to_csv(output_path, index=False)
        print(f"Processed {month_file} -> {output_path}")

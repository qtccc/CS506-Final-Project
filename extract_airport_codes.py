import os
import pandas as pd
import json

# Path to the folder containing the processed CSV files
processed_data_path = './processed_data'

# Initialize a set to store unique airport codes
unique_airport_codes = set()

# Process each CSV file
for file_name in os.listdir(processed_data_path):
    if file_name.endswith('.csv'):  # Check for CSV files
        file_path = os.path.join(processed_data_path, file_name)
        print(f'Processing {file_path}...')

        # Load the CSV into a DataFrame
        df = pd.read_csv(file_path)

        # Check if the column 'OriginAirportSeqID' exists
        if 'OriginAirportSeqID' in df.columns:
            # Add unique airport codes to the set
            unique_airport_codes.update(df['OriginAirportSeqID'].unique())
        else:
            print(f"Warning: 'OriginAirportSeqID' column not found in {file_name}")

# Convert the set to a sorted list and cast all elements to int
sorted_airport_codes = sorted(map(int, unique_airport_codes))

# Ensure the 'static' directory exists
static_dir = './static'
os.makedirs(static_dir, exist_ok=True)

# Save the list to a JSON file
output_file = os.path.join(static_dir, 'airport_codes.json')
with open(output_file, 'w') as json_file:
    json.dump(sorted_airport_codes, json_file)

print(f'Successfully saved {len(sorted_airport_codes)} unique airport codes to {output_file}')
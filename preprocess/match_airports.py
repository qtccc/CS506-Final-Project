import pandas as pd
from fuzzywuzzy import process

# File paths
filtered_airports_file = '/workspaces/CS506-Final-Project/Filtered_Airport_Info.csv'
openflights_file = '/workspaces/CS506-Final-Project/preprocess/airports.dat.txt'
output_file = '/workspaces/CS506-Final-Project/Filtered_Airports_with_Coordinates.csv'

# Load Filtered_Airport_Info.csv
filtered_airports = pd.read_csv(filtered_airports_file)

# Load airports.dat.txt with appropriate column names
columns = [
    "AirportID", "AirportName", "City", "Country", "IATA", "ICAO",
    "Latitude", "Longitude", "Altitude", "Timezone", "DST", "TzDatabase", "Type", "Source"
]
openflights_data = pd.read_csv(openflights_file, header=None, names=columns)

# Normalize names for better matching (remove extra spaces, convert to lowercase)
filtered_airports['NormalizedDescription'] = (
    filtered_airports['Description'].str.split(':').str[-1].str.strip().str.lower()
)
openflights_data['NormalizedAirportName'] = openflights_data['AirportName'].str.strip().str.lower()

# Debug: Print some examples of normalized names
print("Filtered Airport Names:", filtered_airports['NormalizedDescription'].unique()[:10])
print("OpenFlights Airport Names:", openflights_data['NormalizedAirportName'].unique()[:10])

# Fuzzy matching to align names
def find_best_match(description, airport_names):
    match, score = process.extractOne(description, airport_names)
    return match if score > 80 else None  # Only consider matches with a score > 80

# Apply fuzzy matching
openflights_airport_names = openflights_data['NormalizedAirportName'].tolist()
filtered_airports['MatchedAirportName'] = filtered_airports['NormalizedDescription'].apply(
    lambda x: find_best_match(x, openflights_airport_names)
)

# Merge using fuzzy-matched names
merged_data = pd.merge(
    filtered_airports,
    openflights_data,
    how='left',
    left_on='MatchedAirportName',
    right_on='NormalizedAirportName'
)

# Find the unmatched row for "NY LaGuardia"
unmatched_rows = merged_data[merged_data['Latitude'].isna()]

# Manually update the coordinates for "NY LaGuardia"
merged_data.loc[merged_data['Description'].str.contains("LaGuardia", case=False, na=False), ['Latitude', 'Longitude']] = [40.77719879, -73.87259674]

# Keep only relevant columns for the final result
result = merged_data[["SeqID", "Description", "Latitude", "Longitude"]]

# Save the final dataset to a CSV file
result.to_csv(output_file, index=False)

print(f"Matched airport data with coordinates saved to: {output_file}")

# Save unmatched rows for inspection
unmatched = merged_data[merged_data['Latitude'].isna()]
unmatched.to_csv('/workspaces/CS506-Final-Project/Unmatched_Airports.csv', index=False)
print(f"Unmatched airports saved to: /workspaces/CS506-Final-Project/Unmatched_Airports.csv")

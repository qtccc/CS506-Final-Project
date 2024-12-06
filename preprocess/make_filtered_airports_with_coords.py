import pandas as pd
from fuzzywuzzy import process

filtered_airports_file = './Filtered_Airport_Info.csv'
openflights_file = './airports.dat.txt'
output_file = './Filtered_Airports_with_Coordinates.csv'

filtered_airports = pd.read_csv(filtered_airports_file)

columns = [
    "AirportID", "AirportName", "City", "Country", "IATA", "ICAO",
    "Latitude", "Longitude", "Altitude", "Timezone", "DST", "TzDatabase",
    "Type", "Source"
]
openflights_data = pd.read_csv(openflights_file, header=None, names=columns)
filtered_airports['NormalizedDescription'] = ( # normalize for better matching
    filtered_airports['Description'].str.split(':').str[-1]
    .str.strip().str.lower()
)
openflights_data['NormalizedAirportName'] = \
openflights_data['AirportName'].str.strip().str.lower()

# For debugging
print("Filtered Airport Names:",
      filtered_airports['NormalizedDescription'].unique()[:10])
print("OpenFlights Airport Names:",
      openflights_data['NormalizedAirportName'].unique()[:10])

# Fuzzy matching to align names
def find_best_match(description, airport_names):
    match, score = process.extractOne(description, airport_names)
    return match if score > 80 else None

openflights_airport_names = openflights_data['NormalizedAirportName'].tolist()
filtered_airports['MatchedAirportName'] = \
filtered_airports['NormalizedDescription'].apply(
    lambda x: find_best_match(x, openflights_airport_names)
)
merged_data = pd.merge(
    filtered_airports,
    openflights_data,
    how='left',
    left_on='MatchedAirportName',
    right_on='NormalizedAirportName'
)

########## Handle NY LaGuardia outlier ##########
# Find the unmatched row for "NY LaGuardia"
unmatched_rows = merged_data[merged_data['Latitude'].isna()]
# Manually update the coordinates for "NY LaGuardia"
merged_data.loc[merged_data['Description'].str.contains(
    "LaGuardia", case=False, na=False),
                ['Latitude', 'Longitude']] = [40.77719879, -73.87259674]
########## Handle NY LaGuardia outlier ##########

result = merged_data[["SeqID", "Description", "Latitude", "Longitude"]]
result.to_csv(output_file, index=False)

print(f"Matched airport data with coordinates saved to: {output_file}")

# Save unmatched rows for inspection
unmatched = merged_data[merged_data['Latitude'].isna()]
unmatched.to_csv('./Unmatched_Airports.csv', index=False)
print(f"Unmatched airports saved to: ./Unmatched_Airports.csv")

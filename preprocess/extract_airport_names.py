import pandas as pd

# Path to the file with airport info
airport_info_file = '/workspaces/CS506-Final-Project/preprocess/L_AIRPORT_SEQ_ID.csv'

# List of OriginAirportSeqIDs to extract names for
origin_airport_ids = [
    1471105, 1013506, 1402501, 1226505, 1239703, 1393305, 1025702, 1079206, 1057705, 1153706, 1432105,
    1225003, 1430706, 1058102, 1507003, 1247805, 1239103, 1329605, 1457607, 1295304, 1157706, 1161802,
    1043405, 1289806, 1410005, 1255905, 1509602, 1078502, 1072102, 1412202, 1052907, 1425902, 1015406,
    1535602, 1219702, 1354102, 1323002, 1015804
]

# Load the airport information file
airport_info_df = pd.read_csv(airport_info_file)

# Rename columns for convenience (adjust based on actual column names)
airport_info_df.columns = ['SeqID', 'Description']

# Filter the rows for the given OriginAirportSeqIDs
filtered_airports = airport_info_df[airport_info_df['SeqID'].isin(origin_airport_ids)]

# Save the filtered results to a new CSV file
output_path = "/workspaces/CS506-Final-Project/Filtered_Airport_Info.csv"
filtered_airports.to_csv(output_path, index=False)

print(f"Filtered airport information saved at: {output_path}")

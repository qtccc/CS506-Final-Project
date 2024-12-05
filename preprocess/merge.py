import pandas as pd

# Paths to files
filtered_airports_file = '/workspaces/CS506-Final-Project/Filtered_Airport_Info.csv'
original_dataset_file = '/workspaces/CS506-Final-Project/data/January.csv'  # Example
output_file = '/workspaces/CS506-Final-Project/Merged_Airport_Data.csv'

# Load the filtered airport data
filtered_airports = pd.read_csv(filtered_airports_file)

# Load the original dataset
original_data = pd.read_csv(original_dataset_file)

# Merge the datasets on OriginAirportSeqID
merged_data = pd.merge(original_data, filtered_airports, how='left', left_on='OriginAirportSeqID', right_on='SeqID')

# Save the merged dataset to a new file
merged_data.to_csv(output_file, index=False)

print(f"Merged data saved to: {output_file}")

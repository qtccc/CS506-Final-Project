all: processed_data

Merged_Airport_Data.csv:
	python3 merge.py

Daily_Weather_Data.csv:
	python3 weatherdata.py
Hourly_Weather_Data.csv: Daily_Weather_Data.csv
Filtered_Airport_Info.csv:
	python3 extract_airport_names.py
Filtered_Airports_with_Coordinates.csv: airports.dat.txt Filtered_Airport_Info.csv
	python3 make_filtered_airports_with_coords.py
Airports_Daily_Weather.csv: Filtered_Airports_with_Coordinates.csv Hourly_Weather_Data.csv
	python3 merge_weatherData_Airports.py
Airports_Hourly_Weather.csv: Airports_Daily_Weather.csv
processed_data:
	python3 final_join.py					# join on day weather (don't have hour)

.PHONY: processed_data clean
clean:
	rm *.csv

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": [40.652099609375, 41.25310135, 39.45759963989258,
                     42.74829864501953, 41.3385009766, 41.9388999939,
                     42.20869827, 44.80739974975586, 42.36429977,
                     44.4719009399, 42.94049835, 42.1599006652832,
                     42.0831270134, 40.692501068115234, 41.06700134277344,
                     -33.9648017883, 43.1072998046875, 39.17710113525391,
                     43.1735992432, 40.63980103, 40.31610107421875, 40.27590179,
                     40.77719879, 40.1935005188, 42.932598, 41.3931007385,
                     42.26729965209961, 44.6509017944336, 39.87189865112305,
                     40.49150085, 43.0778999329, 45.4706001282, 43.64619827,
                     -3.58383011818, 40.8493003845, 45.3224983215332,
                     43.11119842529297, 40.27669906616211],
	"longitude": [-75.44080352783203, -70.06020355, -74.57720184326172,
                      -73.80169677734375, -75.72339630130001, -72.68319702149999,
                      -75.97979736, -68.8281021118164, -71.00520325,
                      -73.15329742429999, -78.73220062, -76.8916015625,
                      -80.1738667488, -74.168701171875, -73.70760345458984,
                      18.6016998291, -78.94619750976562, 23.503700256347656,
                      -79.93499755859999, -73.77890015, -78.83390045166016,
                      -79.40480042, -73.87259674, -76.7633972168, -71.435699,
                      -70.6143035889, -71.87570190429688, -73.46810150146484,
                      -75.24109649658203, -80.23290253, -70.8233032227,
                      -73.7407989502, -70.30930328, 143.669006348,
                      -77.84870147710001, -75.66919708251953,
                      -76.1063003540039, -74.8134994506836],
	"start_date": "2023-01-01",
	"end_date": "2023-12-31",
	"hourly": ["temperature_2m", "relative_humidity_2m",
                   "precipitation", "pressure_msl", "cloud_cover",
                   "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
	"daily": ["weather_code", "temperature_2m_max", "wind_speed_10m_max",
                  "wind_direction_10m_dominant"]
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()
hourly_pressure_msl = hourly.Variables(3).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(4).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(5).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(6).ValuesAsNumpy()
hourly_wind_gusts_10m = hourly.Variables(7).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["precipitation"] = hourly_precipitation
hourly_data["pressure_msl"] = hourly_pressure_msl
hourly_data["cloud_cover"] = hourly_cloud_cover
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(2).ValuesAsNumpy()
daily_wind_direction_10m_dominant = daily.Variables(3).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["weather_code"] = daily_weather_code
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)
hourly_wdata = "Hourly_Weather_Data.csv"
daily_wdata = "Daily_Weather_Data.csv"
hourly_dataframe.to_csv(hourly_wdata, index=False)
daily_dataframe.to_csv(daily_wdata, index=False)

print(f"Hourly and daily weather data saved to {hourly_wdata} and {daily_wdata}.")

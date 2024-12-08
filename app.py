import pandas as pd
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Path to processed data folder
processed_data_path = './processed_data'

# Create a unique mapping of airport codes to names
airport_mapping = {}
for file_name in os.listdir(processed_data_path):
    if file_name.endswith('.csv'):  # Process only CSV files
        file_path = os.path.join(processed_data_path, file_name)
        df = pd.read_csv(file_path)

        # Extract airport codes and names
        if 'OriginAirportSeqID' in df.columns and 'Description' in df.columns:
            for code, name in zip(df['OriginAirportSeqID'], df['Description']):
                if code not in airport_mapping:  # Avoid overwriting duplicates
                    airport_mapping[code] = name


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/get_airports', methods=['GET'])
def get_airports():
    """Serve the list of airports with their codes and names."""
    airports = [{"code": int(code), "name": name} for code, name in airport_mapping.items()]
    return jsonify(airports)


@app.route('/get_delays', methods=['POST'])
def get_delays():
    """Calculate and return delay likelihood for selected airport and month."""
    data = request.json
    airport = int(data.get('airport'))
    month = data.get('month')

    # Find the corresponding CSV file
    file_name = os.path.join(processed_data_path, f'{month}.csv')

    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
        airport_data = df[df['OriginAirportSeqID'] == airport]

        # Handle empty DataFrame
        if airport_data.empty:
            return jsonify({
                'delay_likelihood': 0,
                'weather_delay_likelihood': 0,
                'message': 'No data available for the selected airport and month.'
            })

        # Calculate delay likelihoods
        delay_likelihood = airport_data['DepDelayMinutes'].mean()
        weather_delay_likelihood = airport_data['WeatherDelay'].fillna(0).mean()  # Replace NaN with 0

        return jsonify({
            'delay_likelihood': delay_likelihood if not pd.isna(delay_likelihood) else 0,
            'weather_delay_likelihood': weather_delay_likelihood if not pd.isna(weather_delay_likelihood) else 0
        })
    else:
        return jsonify({'error': f'Month {month} data not found.'}), 404


if __name__ == '__main__':
    app.run(debug=True)

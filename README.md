# Flight Delay Prediction Using Weather Data


**MIDTERM VIDEO**:
    <div class="assignment-card">
      <h2>Midterm Video</h2>
      <p> </p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/2EWXgbAuChQ?si=IrGQamRudoZOl1ic" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Objective**:  
This project aims to develop a predictive model that forecasts flight delays using weather data. Accurately predicting delays can help airlines, passengers, and airports better manage time and resources.

## Goals:
We aim to predict flight delay likelihood based on weather conditions, such as precipitation and wind speed.

## Data Source
https://open-meteo.com/ for weather data by (lat,long)
https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr for flights and delay information, coordinates of departing airport


## Data Collection:
We will gather:
- **Historical Flight Data**: Including details on departure, arrival airports, and delay durations. U.S. 2023, 12 months.
- **Weather Data**: Temperature, precipitation, wind speed, and visibility data, linked to corresponding flight information.

## Modeling Approach:
We plan to use **tree models or XGBoost** to predict delays based on weather conditions. Though clustering like **KMeans** is typically used for unsupervised tasks, we initially planned to explore it for grouping weather patterns that correlate with delays. However, since our data is labeled, we will focus more on supervised learning techniques.

## Visualization:
We will develop interactive visualizations such as scatter plots to show the relationship between delays and weather conditions, and time graphs to visualize delay trends over time.

## Test Plan:
We will split the dataset into 80% training and 20% testing data, training the model on one time period and testing on another to evaluate performance over time.

## Distribution of work
  * Ross: model
  * Ashkat: model training
  * Lauren: data collection
  * Tiffany: data 
  * Aurora: preprocessing data (e.g. join weather data w/ flight data on (lat,long) coordinate).

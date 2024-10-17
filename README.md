# Flight Delay Prediction Using Weather Data

**Objective**:  
This project aims to develop a predictive model that forecasts flight delays using weather data. Accurately predicting delays can help airlines, passengers, and airports better manage time and resources.

## Goals:
We aim to predict flight delay likelihood based on weather conditions, such as precipitation and wind speed.

## Data Source
https://www.flightaware.com/

## Data Collection:
We will gather:
- **Historical Flight Data**: Including details on departure, arrival airports, and delay durations.
- **Weather Data**: Temperature, precipitation, wind speed, and visibility data, linked to corresponding flight information.

## Modeling Approach:
We plan to use **tree models or XGBoost** to predict delays based on weather conditions. Though clustering like **KMeans** is typically used for unsupervised tasks, we initially planned to explore it for grouping weather patterns that correlate with delays. However, since our data is labeled, we will focus more on supervised learning techniques.

## Visualization:
We will develop interactive visualizations such as scatter plots to show the relationship between delays and weather conditions, and time graphs to visualize delay trends over time.

## Test Plan:
We will split the dataset into 80% training and 20% testing data, training the model on one time period and testing on another to evaluate performance over time.

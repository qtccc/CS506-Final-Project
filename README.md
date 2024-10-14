# CS506-Final-Project

Description of the project : The objective of this project is to develop a predictive model that forecasts flight delays using weather data. Flight delays are a common issue, and accurate predictions can help airlines, passengers, and airports manage time and resources more efficiently.

Data Source Link: https://www.flightaware.com/

Goals : Our goal is to predict the likelihood of delays for upcoming flights due to weather conditions.

Data needed :
- Collect historical flight data on departure/arrival airports, duration of delay, etc.
- Collect past weather data on temperature, precipitation, wind speed, visibility, and other relevant weather variables.


Data Collection Modeling :
we can utilize tree modles or XGBoost to improve the accuracy of the predictions. We would take into account weather factors such as precipitation and wind speed.


Visualizing the data :
We plan to utilize interactive visualizations such as scatter plots in order to see the connection between flight delay and weather 
factors. We can use a time graph to see the trend of delayed flights over time. This can also allow us to see the comparison between the 
predicted delay and the actual delay. 

Test Plan : We will withold 20% of the historical data for testing and train on the remaining 80% of the data. We plan to train on data
from one period and test on a different period.

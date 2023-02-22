# Bike Sharing Project
In this project, I will be investigating into the bike share rental data from “Capital Bikeshare” servicing Washington D.C. and surrounding areas beginning 2011. Capital Bikeshare was the largest bike sharing service in the United States when they started, until Citi Bike for New York City started operations in 2013. Capital Bikeshare started from 10 stations with 120 bicycles in Washington D.C. and expanded into a bike share system that owns more than 429 stations and 2500 bicycles.

## Problem Definition
My objective of the analysis is to find out the determining factor that drives the demand on bike share rentals, construct statistical models and then try to make prediction on rentals based on the information and models I have. My exploration and the analysis of the data will be performed in python.

## Dataset Information
The data I will be working on can be found on [Kaggle](https://www.kaggle.com/c/bike-sharing-demand/data?select=train.csv). This bike share rental data of Capital Bikeshare only contains entries sampled from Washington D.C. spaning two years dating from January 1st, 2011 to December 19th, 2012. The dataset is also joined by the weather statistics for the corresponding date and time.

## Data Features
`datetime` - Containing hourly date in timestamp format\ 
`season` -  Containing integers 1 to 4 representing following:

* 1 = spring
* 2 = summer
* 3 = fall
* 4 = winter

`holiday` - Whether the day is considered a holiday\
`workingday` - Whether the day is neither a weekend nor holiday\
`weather` - Containing integers 1 to 4 representing four different lists of weather conditions:

* 1: Clear, Few clouds, Partly cloudy, Partly cloudy
* 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
* 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
* 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

`temp` - Temperature in Celsius\
`atemp` - "Feel's Like" temperature in Celsius\
`humidity` - Relative humidity\
`windspeed` - Wind speed\
`casual` - Number of non-registered user rentals initiated\
`registered` - Number of registered user rentals initiated\
`count` - Number of total rentals

## Model Evaluation Criteria
The model(s) will be evaluated based on following.

* Root Mean Squared Log Error
* Mean Squared Log Error
* Mean Squared Error
* Mean Absolute Error
* r2 Score

## Model Selection
1. Support Vector Machine
2. Random Forest Regressor
3. Linear Regression

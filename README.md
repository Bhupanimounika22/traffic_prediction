# Traffic Prediction

## Overview
Traffic prediction involves analyzing vehicle movement patterns to estimate traffic conditions (low, normal, heavy) based on various factors. This project aims to develop a predictive model that classifies traffic levels using machine learning techniques.

## Features
- Predicts traffic levels: **Low, Normal, Heavy**
- Uses vehicle count, speed, road type, and weather conditions as input
- Implements deep learning models for accurate predictions

## Data Collection
The dataset includes:
- **Vehicle Count**: Number of vehicles passing through a point in a given time frame
- **Vehicle Types**: Cars, trucks, buses, motorcycles
- **Speed Data**: Average vehicle speed in km/h
- **Road Type**: Highway, city roads, rural roads
- **Time of Day**: Morning, afternoon, evening, night
- **Weather Conditions**: Clear, rainy, foggy, snowy

## Model Implementation
- **Data Preprocessing**: Cleaning, normalization, and feature extraction
- **Machine Learning Models**: Decision Trees, Random Forest, Neural Networks
- **Deep Learning Models**: LSTMs, CNNs for spatiotemporal analysis

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Bhupanimounika22/traffic_prediction.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```sh
   export FLASK_APP=app.py
   flask run
   ```

## Usage
- Upload real-time traffic data
- Get predictions on traffic status
- Analyze trends with visualizations

## Future Enhancements
- Integrate real-time traffic API
- Improve model accuracy with more data
- Develop a mobile-friendly UI

## Contributors
- **Bhupani Mounika**  
  [GitHub](https://github.com/Bhupanimounika22)

## License
MIT License


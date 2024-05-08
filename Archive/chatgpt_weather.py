import requests
import json

def get_weather_forecast(latitude, longitude):
    # Construct the URL for the weather forecast endpoint
    weather_api = f"https://api.weather.gov/points/{latitude},{longitude}"
    
    # Make a GET request to the weather API
    response = requests.get(weather_api)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_dict = response.json()
        
        # Extract the forecast URL from the properties
        forecast_url = response_dict['properties']['forecast']
        
        # Make a second GET request to the forecast URL
        forecast_response = requests.get(forecast_url)
        
        # Check if the request was successful (status code 200)
        if forecast_response.status_code == 200:
            # Parse the JSON response for the forecast
            forecast_dict = forecast_response.json()
            
            # Print the detailed forecast from the first period
            first_period = forecast_dict['properties']['periods'][0]
            print(first_period['detailedForecast'])
        else:
            # Print an error message if the forecast request failed
            print("Failed to fetch forecast data.")
    else:
        # Print an error message if the initial request failed
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    # Read coordinates from the file
    with open('coordinates.txt', 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split(',')
            location = parts[0].strip()
            latitude = parts[1].strip()
            longitude = parts[2].strip()
            
            # Call the get_weather_forecast function with the provided coordinates
            print(f"Weather forecast for {location}:")
            get_weather_forecast(latitude, longitude)
            print()

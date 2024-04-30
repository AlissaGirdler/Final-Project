import requests
import json
from pprint import pprint


weather_api = "https://api.weather.gov/points/35.7687,-75.5241"
response = requests.get(weather_api)
response_dict = json.loads(response.text)
pprint(response_dict)

forecast = 'https://api.weather.gov/gridpoints/MHX/95,79/forecast'
forecast_response = requests.get(forecast)
forecast_dict = json.loads(forecast_response.text)
pprint(forecast_dict)



#OBX Lat / Long 35.768719 -75.524109
#Tokyo Lat / Long 35.689487 35.689487

#How to insert variable for the lat / lon in the weather api url? 
#How to circular reference forecast url in second GET request?
#How to associate good / bad with sunny / rainy? 
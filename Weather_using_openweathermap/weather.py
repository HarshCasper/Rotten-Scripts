#!/usr/bin/env python3

#converting the program into a script

import requests, json 
from sys import argv

#imports and dependencies

api_key = "26efcdb88222e7ef85b472051b4e49d0"

#api key got from openweathermap

base_url = "http://api.openweathermap.org/data/2.5/weather?" 

#url to access to the API

city_name = argv[1] 

#name of the city received as a command line argument

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

#URL based on the API key generated

response = requests.get(complete_url) 
weather_data = response.json() 

#obtaining data in JSON form

if weather_data["cod"] != "404": #If the URL is not accessible it will show a 404 page not found error, else continue
    weather = weather_data["main"] 
    current_temperature = weather["temp"] 
    current_pressure = weather["pressure"] #Data is parsed from the JSON file
    current_humidity = weather["humidity"] 
    details = weather_data["weather"] 
    weather_description = details[0]["description"]
    print("The weather in " + argv[1] + " is :")
    print(" Temperature (in degrees celsius) : " +
                    str(int(current_temperature-273)) + 
                    "\n Humidity : (in percentage) = " +
                    str(current_humidity) + "%"
                    "\n Description : " +
                    str(weather_description)) 
  
else: 
    print("City Not Found") 

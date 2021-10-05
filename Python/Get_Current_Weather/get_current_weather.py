import sys
import requests
import json
import datetime

# each key can respond to a maximum of 60 calls per minute
# and 1,000,000 calls per month
# use your own api key which you can get from openweathermap
api_key = "c4129d312f42336xxxxxe5b8c65e3647"

# the first argument is the script name
# the second argument is the city name
# the third argument is the units format (standard, imperial and metric)
# the following arguments can be sun, main, weather, wind or clouds
argumentList = sys.argv
if len(argumentList) < 3:
    print("Please enter the city name and units format")
    sys.exit()

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# take input(city name) from user
city_name = argumentList[1]

# in which units the user wants the data in
option = argumentList[2]

# set default units format to metrics
units = "&units=metrics"

if option == "1":
    units = ""
elif option == "2":
    units = "&units=imperial"
elif option == "3":
    units = "&units=metric"
else:
    print("All the units are in Metrics.")

# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + units

# get method returns the response object
response = requests.get(complete_url)

# convert json format into python format data
x = response.json()

# if any of the additional arguments is sun
# it should give the time of sunrise and sunset


def getSunData():
    sun = x["sys"]
    sunrise = datetime.datetime.fromtimestamp(sun["sunrise"])
    sunset = datetime.datetime.fromtimestamp(sun["sunset"])
    print("\nSunrise (UTC): " + sunrise.strftime("%Y-%m-%d %H:%M:%S"))
    print("Sunset (UTC): " + sunset.strftime("%Y-%m-%d %H:%M:%S"))


# if any of the additional arguments is main
# it should give the temperature details


def getMainData():
    main = x["main"]
    print("\nActual Temperature: " + str(main["temp"]))
    print("Feels like: " + str(main["feels_like"]))
    print("Temperature (min): " + str(main["temp_min"]))
    print("Temperature (max): " + str(main["temp_max"]))


# if any of the additional arguments is weather
# it should give the pressure, humidity and weather description


def getWeatherData():
    main = x["main"]
    weather = x["weather"]
    print("\nPressure: " + str(main["pressure"]))
    print("Humidity: " + str(main["humidity"]))
    print("Weather: " + weather[0]["description"])


# if any of the additional arguments is wind
# it should give the speed and direction of wind


def getWindData():
    wind = x["wind"]
    print("\nWind Speed: " + str(wind["speed"]))
    print("Wind Direction: " + str(wind["deg"]))


# if any of the additional arguments is clouds
# it should give the percentage of cloudinesss


def getCloudsData():
    clouds = x["clouds"]
    print("\nCloudiness (Percentage): " + str(clouds["all"]))


# now x contains list of nested dictionaries
# check if the value of "cod" key is equal to "404"
# which means the city is not found
if x["cod"] != "404":

    for i in range(3, len(argumentList)):
        if argumentList[i] == "sun":
            getSunData()
        elif argumentList[i] == "main":
            getMainData()
        elif argumentList[i] == "weather":
            getWeatherData()
        elif argumentList[i] == "wind":
            getWindData()
        elif argumentList[i] == "clouds":
            getCloudsData()

    # if no additional arguments are given, then output all the data
    if len(argumentList) == 3:
        getSunData()
        getMainData()
        getWeatherData()
        getWindData()
        getCloudsData()

else:
    print("City Not Found")
    print("Please check the spelling and enter the full city name")
    print(
        "Also make sure you follow the order in which the arguments need to be given in"
    )

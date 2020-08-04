#This script is used to obtain details of COVID in all the countries, using the open source API provided John Hopkins University
#________________________________________________________________________________________________#

#Imports

import requests
import json
import difflib
from similar import similar_locations

#A country is passed as a parameter and corresponding response is obtained

def all_countries(country):
    countries = dict()
    count = 0

    #GET request is made to the API
    response = requests.get("https://api.covid19api.com/summary")
    response = json.loads(response.text)
    
    #All the countries are assigned a serial number, so the same can be used for accessing the details
    for entry in response["Countries"]:
        countries[entry["Country"]] = count
        count += 1
    info = ""
    
    #The country name is converted to Title Case, as that is how it is represented
    country = country[0].upper() + country[1:].lower()
    
    #Data fields are extracted and stored
    if country in countries:
        serial = countries[country] 
        target_country = response["Countries"][serial]
        covid_stats = dict(list(target_country.items())[: -3])
        for data in covid_stats:
            if data not in ["Slug", "CountryCode"]:
                info += data + " : " + str(covid_stats[data]) + "\n"
        return(info)
    else:
        similar = similar_locations(countries, country)
        if len(similar) <= 2:
            return("Country does not exist, Try Again")
        return("Country does not exist, maybe you are looking for \n" + similar)

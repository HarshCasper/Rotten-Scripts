#The data about COVID cases in India is obtained using the open source API

#Imports and dependencies
import requests
import json
from sys import argv
import difflib
from similar import similar_locations

#Data is collected regarding all states and districts in India and stored in dictionaries.
def states_and_districts_in_India():

    #API for data regarding COVID cases in India
    response = requests.get("https://api.covidindiatracker.com/state_data.json")
    response = json.loads(response.text)
    
    #Dictionaries for all states and Districts
    all_states = dict()
    all_districts = dict()
    for state in response:
        all_states[state["state"].lower()] = "State : " + state["state"] + "\nActive : " + str(state["active"])  + "\nRecovered : "  + str(state["recovered"]) + "\nConfirmed : " + str(state["confirmed"]) + "\nDeaths : "  + str(state["deaths"])
        district_data = state["districtData"]
        for district in district_data:
            all_districts[district["name"].lower()] = "District : " + district["name"]  + "\nConfirmed : " + str(district["confirmed"]) + "\n"  + "Recovered : " + str(district["recovered"]) + "\n" + "deaths : " + str(district["deaths"]) + "\n" + "Zone : " + district["zone"] 
    return(all_states, all_districts)

#Based on the input, a suitable response is returned

def in_district(district):
    all_states, all_districts = states_and_districts_in_India()
    if district in all_districts:
        return(all_districts[district])
    else:
        similar = similar_locations(all_districts, district)
        #If there are no similar states, then the following is returned
        if len(similar) <= 2:
            return("District does not exist, Try Again")
        return("District is non-existent, You might be looking for \n" + similar) #If there are similar locations, this is returned.

def in_state(state):
    all_states, all_districts = states_and_districts_in_India()
    if state in all_states:
        return(all_states[state])
    else:
        similar = similar_locations(all_states, state)
        if len(similar) <= 2:
            return("State does not exist, Try Again")
        return("State is non-existent, You might be looking for \n" + similar)


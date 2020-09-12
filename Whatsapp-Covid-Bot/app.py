#!/usr/bin/env python3

#Imports and dependencies
import requests
import json
import os
from countries import all_countries
from indiaa import in_district, in_state
import difflib
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

'''Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, 
and perform other communication functions using its web service APIs'''
#Here the Twilio API's are used in order to interact with whatsapp

#setting up the flask server
app = Flask(__name__)

@app.route("/")
def hello():
    return "Covid cases"

#The call-back URL used here, is running on the URL hosted on heroku routed to /sms
@app.route("/sms", methods=['POST'])

def incoming_sms():

    #The incoming request from the user is collected here
    body = request.values.get('Body')
    resp = MessagingResponse()
    body = body.split(",")
    geography, loc = body[0] , body[1].strip().lower()
    
    #The user enters either of the notations followed by a comma. The name of the country/state/district follows this.
    #Example : c, India
    #Example: District, Thane
    #Example: state, kerala

    if geography in ["Country", "country" , "COUNTRY", "C", "c"]:
            cases = all_countries(loc)
    elif geography in ["District", "district" , "DISTRICT", "D" , "d"]:
        cases = in_district(loc)
    elif geography in ["state" , "State" , "STATE", "S", "s"]:
        cases = in_state(loc)
    resp.message(cases)
    return str(resp)

#running the flask server
if __name__ == "__main__":
    app.run(debug=True)


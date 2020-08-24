#Imports and dependencies

import requests
import time
from bs4 import BeautifulSoup
from mail_in_python import send_confirmation
import datetime  
    
#This variable is to test the feasibility of the product
feasible = False

#This function is to indicate to the user the currency the product is mentioned in, so the same currency is used for budget.

def currency_used(URL):

    #These headers are user specific, look for "my user agent" in the google search bar and replace your user agent here"
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'} 

    #Response got from the request sent to the desired product URL
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    currency_symbols = {'€' : "Euro", '£' : "Pound", '$' : "Dollars", "¥" : "Renminbi", "HK$" : "Hong Kong Dollars", "₹" : "Rupeees"} 
    
    #Using web-scraping the price of the product is found
    price = soup.find(id="priceblock_ourprice").get_text()
    currency = ""
    
    for symbol in currency_symbols:
        if symbol in price:
            currency = currency_symbols[symbol]
            price = price.replace(symbol, "")

    #The currency of the product is stored here"
    return(currency)


def price_check(URL, budget):
    
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'} 
    feasible = False
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    currency_symbols = {'€' : "Euro", '£' : "Pound", '$' : "Dollars", "¥" : "Renminbi", "HK$" : "Hong Kong Dollars", "₹" : "Rupeees"} 
    price = soup.find(id="priceblock_ourprice").get_text()
    currency = ""
    
    for symbol in currency_symbols:
        if symbol in price:
            currency = currency_symbols[symbol]
            price = price.replace(symbol, "")
    
    #string is converted to a number and extra characters are removed
    
    if "," in price:
        price = price.replace(",", "")
    
    #The price for some products is expressed as a range, thus the following is performed
    price = price = price.split("-")
    price_now = []
    if len(price) == 2:
            lower, upper = float(price[0].strip('\xa0')) , float(price[1].strip('\xa0'))
            price_now.append(lower)
            price_now.append(upper)
            price_range = [*(range(int(lower), int(upper+1)))]
            if budget in price_range:
                feasible = True
    else:
        price = float(price[0].strip("\xa0"))
        if budget >= int(price):
            feasible = True
        price_now.append(price)
    return(feasible, price_now)

#Enter the URL of the amazon product
URL = input("Enter the URL of the Amazon product : ")

print("The price of the product is expressed in " + (currency_used(URL)))

#Enter your budget in the same currency as mentioned above
budget = int(input("Enter your budget for the product in same unit of currency as mentioned above: "))

print("Please enter your email details as asked, when the price of the product is below or equal to your budget, you will receive an email conformation")

#Since a mail is sent from this script, security mode has to be disabled
print("Also ensure that security mode is switched off in your email settings")

sender_email = input("Enter the sender's Email-ID : ")
receiver_email = input("Enter the receiver's Email-ID : ")
password = input("Enter the sender's password : ")

feasible, price_range = price_check(URL, budget)

#The price_check function will execute every 12 hours to check, the prices will also be logged so that a comparison can be made
while not feasible:
    feasible, price_range = price_check(URL, budget)
    
    if len(price_range) == 1: 
        cost = "The cost of the product is  " + str(price_range[0])
    else:
        cost = "The cost of the product is within the range " + str(price_range[0]) + " and " + str(price_range[1])
    
    current_time = datetime.datetime.now()  
    
    #Logging records into the text file.
    with open("price_logger.txt" , "w") as file:
        file.write(cost + " at " + str(current_time))
        file.write("\n")
    
    if feasible:
        break
    else:
        #Sleeps for 12 hours and then checks for the same
        time.sleep(43200)

#The user will be notified through an email
send_confirmation(sender_email, receiver_email, password, price_range)


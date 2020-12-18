##we willl be using coinbase API as it is public

## More info below
##https://developers.coinbase.com/api/v2?python#get-exchange-rates

import requests

#This function gets exhange rates.
#The coinbase API returns the JSON for an input cryptocurrency with
#data or exhangerate of one coin to all known "normal" currencies
#like BTC(input) to INR,USD,etc.


def exchange_rates(cryptocurrency):
    #capitalising the cryptocurrency values as the API accepts and returns
    cryptocurrency=cryptocurrency.upper()
    
    #"BTC" is for Bitcoin,"ETH" is for Ethirium and so on
    #These are the crypti currency available currently by the API.
    available_cryptocurrencies=['BTC','ETH','ETC','BCH','LTC','ZEC','ZRX']

    if cryptocurrency not in available_cryptocurrencies:
        return None
    
    #sending a request to the api and storing the response object in r variable
    r=requests.get('https://api.coinbase.com/v2/exchange-rates?currency='+cryptocurrency)

    #print(r.text)
    try:
        exchange_dict=r.json()["data"]["rates"]
    except KeyError:
        return None
    return exchange_dict

#This function converts currency amount to cryptocurrency amount
def convert_currency_to_crypto(amount,currency,cryptocurrency):
    #Just checking the input
    try:
        amount=float(amount)
    except:
        return "wrong input!"
    
    #get current_price for cryptocurrency using exhange_rates function
    current_price=exchange_rates(cryptocurrency)[currency]

    if current_price is None:
        return "No info available"

    return amount/float(current_price)

#This function converts currency amount to cryptocurrency amount
def convert_crypto_to_currency(amount,cryptocurrency,currency):
    #Just checking the input
    try:
        amount=float(amount)
    except:
        return "wrong input!"

    #get current_price for cryptocurrency using exhange_rates function
    current_price=exchange_rates(cryptocurrency)[currency]

    if current_price is None:
        return "No info available"

    return float(current_price)*amount


#Just a test
#Should print 1.0

print(convert_currency_to_crypto(convert_crypto_to_currency(1,'BTC','USD'),'USD','BTC'))


"""we will be using coinbase API as it is public
More info below
https://developers.coinbase.com/api/v2?python#get-exchange-rates"""

import requests


def exchange_rates(cryptocurrency):
    """
    This function gets exhange rates.
    The coinbase API returns the JSON for an input cryptocurrency with
    data or exhangerate of one coin to all known "normal" fiat currencies
    like BTC(input) to INR,USD,etc.
    """

    # capitalising the cryptocurrency values as the API accepts and returns
    cryptocurrency = cryptocurrency.upper()

    # These are the cryptocurrency available currently by the API.
    # "BTC" is for Bitcoin,"ETH" is for Ethereum and so on
    available_cryptocurrencies = [
        'BTC', 'ETH', 'ETC', 'BCH', 'LTC', 'ZEC', 'ZRX']

    if cryptocurrency not in available_cryptocurrencies:
        return None

    # sending a request to the api and storing the response object in r variable
    response_obj = requests.get(
        'https://api.coinbase.com/v2/exchange-rates?currency='+cryptocurrency)

    try:
        exchange_dict = response_obj.json()["data"]["rates"]
    except KeyError:
        return None
    return exchange_dict

# This function converts currency amount to cryptocurrency amount


def convert_currency_to_crypto(amount, currency, cryptocurrency):
    """This function converts currency amount to cryptocurrency amount"""

    # checking that the input is correct
    try:
        amount = float(amount)
    except ValueError:
        return "wrong input!"

    # get current_price for cryptocurrency using exhange_rates function
    current_price = exchange_rates(cryptocurrency)[currency]

    if current_price is None:
        return "No info available"

    return amount/float(current_price)


def convert_crypto_to_currency(amount, cryptocurrency, currency):
    """This function converts currency amount to cryptocurrency amount"""

    # Just checking the input
    try:
        amount = float(amount)
    except ValueError:
        return "wrong input!"

    # get current_price for cryptocurrency using exhange_rates function
    current_price = exchange_rates(cryptocurrency)[currency]

    if current_price is None:
        return "No info available"

    return float(current_price)*amount


if __name__ == "__main__":
    STRING = """
    ################################################################

    examples of fiat currencies :INR,USD,etc.
    examples of Cryptocurrencies :BTC,ETH,etc.
    
    ################################################################

    Choose one of the below options:

    Convert Cryptocurrency to fiat currency (Enter 1)  
    Convert fiat currency to Cryptocurrency (Enter 2) 
    Quit (Enter Q)
    """

    while True:
        print(STRING)
        user_inp = input()
        currency = input("Enter fiat currency type:").upper()
        cryptocurrency = input("Enter Cryptocurrency type:").upper()
        amount = int(input("Enter Cryptocurrency amount:"))
        print("\n")
        if user_inp == "1":
            result = convert_crypto_to_currency(
                amount, cryptocurrency, currency)
            print(f"{amount} {cryptocurrency} in {currency} is {result}")
        elif user_inp == "2":
            result = convert_crypto_to_currency(
                amount, cryptocurrency, currency)
            print(f"{amount} {currency} in {cryptocurrency} is {result}")
        elif user_inp == "Q":
            break
        else:
            print("Wrong Input! try again")

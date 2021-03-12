"""we will be using coinbase API as it is public
https://developers.coinbase.com/api/v2?python#get-exchange-rates"""

import requests
import sys


def exchange_rates(typee):
    """This function gets exhange rates. The coinbase API returns the JSON for an input cryptocurrency with data or exhangerate of one coin to all known "normal" fiat currencies like BTC(input) to INR,USD,etc."""
    typee = typee.upper()
    response_obj = requests.get('https://api.coinbase.com/v2/exchange-rates?currency='+typee)

    try: exchange_dict = response_obj.json()["data"]["rates"]
    except: return None
    return exchange_dict

def convert_fiat_to_crypto(fvalue, ftype, ctype):
    """This function converts fiat money to cryptocurrency amount."""
    available_cryptocurrencies = ['BTC', 'ETH', 'ETC', 'BCH', 'LTC', 'ZEC', 'ZRX']
    if ctype not in available_cryptocurrencies:
        print(f"\n{ctype} is not a Cryptocurrency. Try again!")
        sys.exit(0)
    # get current_price for cryptocurrency using exhange_rates function
    try: current_price = exchange_rates(ftype)[ctype]
    except:
        print("nNo Information Available. We're Sorry!")
        sys.exit(0)
    if current_price is None:
        print("\nNo Information Available. We're Sorry!")
        sys.exit(0)

    return float(current_price)*fvalue


def convert_crypto_to_fiat(cvalue, ctype, ftype):
    """This function converts cryptocurrency amount to fiat money."""
    available_cryptocurrencies = ['BTC', 'ETH', 'ETC', 'BCH', 'LTC', 'ZEC', 'ZRX']
    if ftype in available_cryptocurrencies:
        print(f"\n{ftype} is not a Fiat Money. Try Again!")
        sys.exit(0)
    # get current_price for cryptocurrency using exhange_rates function
    try: current_price = exchange_rates(ctype)[ftype]
    except:
        print("\nNo Information Available. We're Sorry!")
        sys.exit(0)
    if current_price is None:
        print("\nNo Information Available. We're Sorry!")
        sys.exit(0)

    return float(current_price)*cvalue


if __name__ == "__main__":
    info_msg = """
We convert currency -> Cryptocurrency to Fiat Money and vice-versa.
\nPress (1)  :  To convert Cryptocurrency to Fiat Money.
Press (2)  :  To convert Fiat Money to Cryptocurrency.
Press (Q/q)  :  If you're wanting to Quit.
    """
    print(info_msg)

    while True:
        user_inp = input("\nEnter Your Choice Here : ")
        if user_inp == "1":
            crypto_type = input("\nEnter the Cryptocurrency Type  :  ")
            fiat_type = input("Enter the Fiat Money Type  :  ")
            try: crypto_value = float(input("\nEnter the Cryptocurrency Value  :  "))
            except:
                print("Bad Input!\nPlease Enter \"y\" if you wish to continue, else \"n\".")
                choice = input()
                if choice == "y": continue
                elif choice == "n": sys.exit(0)
                else:
                    print("Bad Input Again!")
                    sys.exit(0)
            result = convert_crypto_to_fiat(crypto_value, crypto_type.upper(), fiat_type.upper())
            print(f"{crypto_value} {crypto_type.upper()} in {fiat_type.upper()} is  -->  {result}")
        elif user_inp == "2":
            fiat_type = input("\nEnter the Fiat Money Type  :  ")
            crypto_type = input("Enter the Cryptocurrency Type  :  ")
            try: fiat_value = float(input("\nEnter the Fiat Money Value  :  "))
            except:
                print("You did not enter a number!\nPlease Enter \"y\" if you wish to continue, else \"n\".")
                choice = input()
                if choice == "y": continue
                elif choice == "n": sys.exit(0)
                else:
                    print("Bad Input Again!")
                    sys.exit(0)
            result = convert_fiat_to_crypto(fiat_value, fiat_type.upper(), crypto_type.upper())
            print(f"{fiat_value} {fiat_type.upper()} in {crypto_type.upper()} is  -->  {result}")
        elif user_inp == "Q" or user_inp == "q": sys.exit(0)
        else:
            print("Your Input was NOT in the choices.")
            sys.exit(0)

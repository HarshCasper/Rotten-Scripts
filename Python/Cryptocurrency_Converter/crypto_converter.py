"""We will be using coinbase API as it is public.
https://developers.coinbase.com/api/v2?python#get-exchange-rates"""

import requests


def exchange_rates(exchange_type):
    """This function gets exhange rates. The coinbase API returns the JSON for an input cryptocurrency
    with data or exhangerate of one coin to all known "normal" fiat currencies like BTC(input) to INR, USD etc."""
    exchange_type = exchange_type.upper()
    response_obj = requests.get(
        f"https://api.coinbase.com/v2/exchange-rates?currency={exchange_type}"
    )

    try:
        exchange_dict = response_obj.json()["data"]["rates"]
    except:
        return None
    return exchange_dict


def convert_fiat_to_crypto(fvalue, ftype, ctype):
    """This function converts Fiat Money to Cryptocurrency amount.
    Returns 1 if the input is found not valid, converted currency value if the input is found valid, else returns "None".
    "fvalue" corresponds to Fiat Money value, "ftype" to Fiat Money type and "ctype" to Cryptocurrency type --> all given by the user."""
    flag, statement = validity_of_currencytype(ctype, ftype)
    if flag == 1:
        print(statement)
        return 1

    # get current_price for cryptocurrency using exhange_rates function
    try:
        current_price = exchange_rates(ftype)[ctype]
    except:
        print("nNo Information Available. We're Sorry!")
        return
    if current_price is None:
        print("\nNo Information Available. We're Sorry!")
        return
    return float(current_price) * fvalue


def convert_crypto_to_fiat(cvalue, ctype, ftype):
    """This function converts Cryptocurrency amount to Fiat Money.
    Returns 1 if the input is found not valid, converted currency value if the input is found valid, else returns "None".
    "cvalue" corresponds to Cryptocurrency value, "ctype" to Cryptocurrency type and "ftype" to Fiat Money type --> all given by the user."""
    flag, statement = validity_of_currencytype(ctype, ftype)
    if flag == 1:
        print(statement)
        return 1

    # get current_price for cryptocurrency using exhange_rates function
    try:
        current_price = exchange_rates(ctype)[ftype]
    except:
        print("\nNo Information Available. We're Sorry!")
        return
    if current_price is None:
        print("\nNo Information Available. We're Sorry!")
        return
    return float(current_price) * cvalue


def validity_of_currencytype(ctype, ftype):
    """This function checks if the user input of Cryptocurrency type or Fiat Money type are truly the latter.
    Returns 1 if found an error in the input, else returns 0."""
    available_cryptocurrencies = ["BTC", "ETH", "ETC", "BCH", "LTC", "ZEC", "ZRX"]
    if ctype not in available_cryptocurrencies:
        return 1, f"\n{ctype} is not a Cryptocurrency. Try Again!\n"
    if ftype in available_cryptocurrencies:
        return 1, f"\n{ftype} is not a Fiat Money. Try Again!\n"
    return 0, "\nAll Good!"


def main():
    """This function loops through the input given by the user, until given a bad input or "Q/q"."""
    while True:
        user_inp = input("\n\tEnter Your Choice Here : ")

        if user_inp == "1":
            crypto_type = input("\nEnter the Cryptocurrency Type  :  ")
            fiat_type = input("Enter the Fiat Money Type  :  ")
            try:
                crypto_value = float(input("\nEnter the Cryptocurrency Value  :  "))
            except:
                print('Bad Input!\nPlease Enter "y" if you wish to continue, else "n".')
                choice = input()
                if choice == "y":
                    continue
                if choice == "n":
                    return
                print("Bad Input Again!")
                return
            result = convert_crypto_to_fiat(
                crypto_value, crypto_type.upper(), fiat_type.upper()
            )
            if result is None:
                return
            if result == 1:
                continue
            print(
                f"{crypto_value} {crypto_type.upper()} in {fiat_type.upper()} is  -->  {result}"
            )

        elif user_inp == "2":
            fiat_type = input("\nEnter the Fiat Money Type  :  ")
            crypto_type = input("Enter the Cryptocurrency Type  :  ")
            try:
                fiat_value = float(input("\nEnter the Fiat Money Value  :  "))
            except:
                print(
                    'You did not enter a number!\nPlease Enter "y" if you wish to continue, else "n".'
                )
                choice = input()
                if choice == "y":
                    continue
                if choice == "n":
                    return
                print("Bad Input Again!")
                return
            result = convert_fiat_to_crypto(
                fiat_value, fiat_type.upper(), crypto_type.upper()
            )
            if result is None:
                return
            if result == 1:
                continue
            print(
                f"{fiat_value} {fiat_type.upper()} in {crypto_type.upper()} is  -->  {result}"
            )

        elif user_inp == "Q" or user_inp == "q":
            return

        else:
            print("\nYour Input was NOT in the choices. Try again later.\n")
            return


if __name__ == "__main__":
    """The driver code."""
    info_msg = """
We convert currency -> Cryptocurrency to Fiat Money and vice-versa.\n\n
Possible Cryptocurrencies available for conversion are : 
\t BTC  :  Bitcoin
\t ETH  :  Ethereum.
\t ETC  :  Ethereum Classic
\t BCH  :  Bitcoin Cash
\t LTC  :  Litecoin
\t ZEC  :  Zcash
\t ZRX  :  Ox\n\n
Press (1)  :  To convert Cryptocurrency to Fiat Money.
Press (2)  :  To convert Fiat Money to Cryptocurrency.
Press (Q/q)  :  If you're wanting to Quit
"""
    print(info_msg)
    stat = main()
    if stat is not None:
        print(stat)

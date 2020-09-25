import requests
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--amount', action='store', type=int, required=True, help="Enter the amount")
my_parser.add_argument('--f', action='store', type=str, required=True, help="Convert from")
my_parser.add_argument('--t', action='store', type=str, required=True, help="Convert to")

args = my_parser.parse_args()
amount = args.amount
fromCountry = args.f
toCountry = args.t
  
class Currency_convertor: 
    # empty dict to store the conversion rates 
    rates = {}  
    def __init__(self, url): 
        data = requests.get(url).json() 
  
        # Extracting only the rates from the json data 
        self.rates = data["rates"]  
  
    # function to do a simple cross multiplication between  
    # the amount and the conversion rates 
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 
  
        # limiting the precision to 2 decimal places 
        amount = round(amount * self.rates[to_currency], 2) 
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)) 
  
# Driver code 
if __name__ == "__main__": 
  
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io' 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    c = Currency_convertor(url)
  
    c.convert(fromCountry, toCountry, amount) 
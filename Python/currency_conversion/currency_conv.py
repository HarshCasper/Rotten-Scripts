import requests

# Where INR is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/c724ae55d19e2fbee9d643bf/latest/INR'


# Making our request
response = requests.get(url)
data = response.json()

val = int(input("Enter Amount in USD : "))
# Your JSON object
#print(data['conversion_rates']['USD'])
conv_rate=data['conversion_rates']['USD']
amount_in_rs=val/conv_rate
print("Amount in RS",amount_in_rs)		

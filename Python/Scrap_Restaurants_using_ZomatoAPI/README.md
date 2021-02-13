# Scrap Resturants using the Zomato API

## Description

This Python Script Scraps Resturants using API Key of Zomato

## Get a Zomato API Key

* Log in or create a free account on [Zomato](https://www.zomato.com/)
* Navigate to their [developers page](https://developers.zomato.com/api), click on the "Generate API Key" button.
  * The API requires that you enter your phone number, Company Website/Blog
  
## Execution

* Run `pip install - r requirements.txt`
* Create a `.env` file like as `.env.example`, and add follwoing line with your API Key which you get from above Steps.
```
projectKey = {put your key here without brackets}

cityName = {add City Name Here}
```

- Run `python main.py`

Run Programs In Order: 
![Terminal](https://i.pinimg.com/originals/98/11/39/981139102df3bfa5b776a626bec42501.png?epik=dj0yJnU9S0stamItZ0kwY3hnN3RUTGI1dC1qSEtnTDh4OXpsWDAmcD0wJm49RmtIQUVpYzl2eUNYRGtpb3RVbHRBdyZ0PUFBQUFBR0FWQVc0)

You Will Get Output Like This: 

![Output](https://i.pinimg.com/originals/ef/6d/c1/ef6dc17845920a580eaffd21e09433fb.png?epik=dj0yJnU9b1EyenIyQnpfUzJLa2w4MllTR2dFQjBDMkh3RU1NdWImcD0wJm49ZWFfeHRxUGphTWdWMWZwU0VnQ09XUSZ0PUFBQUFBR0FWQVZB)

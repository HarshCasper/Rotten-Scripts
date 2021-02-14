# CryptoCurrencies Price Using Coinbase API

## About Coinbase

Coinbase is a digital currency exchange headquartered in San Francisco, California. They broker exchanges of Bitcoin, Bitcoin Cash, Ethereum, Ethereum Classic, Litecoin, Tezos, and many others, with fiat currencies in approximately 32 countries, and bitcoin transactions and storage in 190 countries worldwide

## Explanation of code

- We are using fetch api to call the coinbase API url
- The cryptocurrencies array is defined already and the price of only these included in array will be shown, you can add more if you wish
- The API sends response with value of cryptocurrencies for 1 unit of the basecurrency mentioned for example, exchange price of BTC for 1 INR
- You can change the basecurency to USD or any other currency
- We have divided exchange price of cryptocurrency by 1 as it gives the value of cryptocurrency in baseCurrency

## To run the code

- Clone the folder
- Inside the folder open command line and run
- npm install
- node cryptoprice.js

## Output

You will see the cryptocurrency name and live price as output
![image](https://i.imgur.com/koTZWbA.png)
code by [Mohit Bhat](https://www.mbcse.co)

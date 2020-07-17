# Nodejs Script to Download all user repositories

## About 
Github being the top choice for open source and storing our Projects code, it becomes very difficult for us to clone each and every Repository. This is time consuming when we want to have a copy of our github repositories in our PC. SO keeping this in mind I have developed a script to download all github public repositories in once!

## Explanation of code
- We are using fetch api to call the coinbase API url
- The cryptocurrencies array is defined already and the price of only these included in array will be shown, you can add more if you wish
- The API sends response with value of cryptocurrencies for 1 unit of the basecurrency mentioned for example, exchange price of BTC for 1 INR
- You can change the basecurency to USD or any other currency 
- We have divided exchange price of cryptocurrency by 1 as it gives the value of cryptocurrecny in baseCurrency 

## To run the code
- Clone the folder
- Inside the folder open command line and run
- npm install
- node cryptoprice.js

## Output 
You will see the cryptocurrency name and live price as output 
![image](https://github.com/mbcse/Rotten-Scripts/blob/crypto_price/All_Crypto_Price/cryptoprice.png)
code by Mohit Bhat(https://www.mbcse.co)
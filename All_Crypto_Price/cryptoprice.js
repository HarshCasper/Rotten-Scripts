const fetch = require('node-fetch');

//cryptocurrencies array, prices of these cryptocurrencies will be shown
//Add more names whose price you to fetch 
var cryptocurrencies=[
"ALGO",
"ATOM",
"COMP",
"DASH",	
"LINK",	
"LOOM",
"MANA",
"USDC",
"BAT",
"BTC",
"BCH",
"BSV",
"CVC",
"DAI",	
"DNT",
"EOS",	
"ETH",
"ETC",
"GNT",
"KNC",
"LTC",
"MKR",
"OMG",
"OXT",
"REP",
"XTZ",
"XLM",
"ZEC",
"ZRX"
]

var baseCurrency="INR";//Its the currency in which you want price of crypto, if you want in usd change to "USD", similarly for others
var url="https://api.coinbase.com/v2/exchange-rates?currency="+baseCurrency;

//Api get call to coinBase api using fetch in javascript
fetch(url).then(res => res.json())
    .then((json) => {

        var cryptoPrice=json.data.rates;//storing cryptocurrencies rate as key value json data in cryptoPrice object

        for(var key in cryptoPrice ){
        
            cryptoPrice[key]=1/cryptoPrice[key];//as the value of crytoPrice is for 1 rs we need price of cryptocurrency in terms of inr we are doing 1/(crypto price for 1INR)
        }   

        console.log("Crypto   "+"     Price");

        //printing name of cryptocurrency and its price 
        for(var key in cryptoPrice){

            if(cryptocurrencies.indexOf(key)!==-1){
                console.log(key+"   "+"     "+cryptoPrice[key]);
            }
            
        }
 
    }).catch(err=>console.log(err));
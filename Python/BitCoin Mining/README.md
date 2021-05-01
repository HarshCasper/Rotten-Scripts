# What Is Bitcoin Mining?
Bitcoin mining is performed by high-powered computers that solve complex computational math problems; these problems are so complex that they cannot be solved by hand and are complicated enough to tax even compelling computers.

## Terminology :
1. Transaction: An transaction is a transfer of Bitcoin value and is collected in Blocks 

2. SHA256: a function that can generate an almost-unique 256-bit (32-byte) signature(Hexa-Decimal) for a text.

3. Block: Blocks are files where data about the Bitcoin network are permanently recorded

4. Nonce: Miners have to guess this number which will reward them BTC. A nonce is an abbreviation for "number only used once," which is a number added to a hashed—or encrypted—block in a blockchain that, when rehashed, meets the difficulty level restrictions. 

5. Difficulty Level: Number of prefix Contagious Zeroes 


## Theory :
BTC will be rewarded if Nonce gives us a string with Zeroes' prefix the difficulty number of times. Sounds confusing?
So, Let's take an example :
1. Let's assume we have a difficulty level = 20 
2. Now, Let's again assume that we have the previous hash as: 'a5x208fecf9a66be9a2bc7...'
3. Now we create text as  : text = str(block_number) + transactions + previous_hash + str(nonce)
4. Now, we pass text to SHA256 Function to generate hash
5. Finally, that hash prefix must be equal to the number of zeroes as difficulty level.
6. And Boom!! You have mined successfully.

## To Run the script :
1. Run Command ```BitCoin_Mining.py```.
2. Now Enter Required Values.
3. You have Mined succesfully!!.

## Sample Test Case :
INPUT : Transactions = '''Neeraj->Zara->50,Nandu->Allu->5''', difficulty=2,
        Previous_hash = a7sdxa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7.
OUTPUT : Successfully mined bitcoins with nonce value:336 end mining. Mining took: 12.207852363586426 seconds
006f74cef9d071afa15c58b38198be14f9b4aabb4cd6f7a44afffd9f6968efcd.

## Draw Backs:
The script has no drawbacks, but due to the increase in miners, the difficulty level increases, and hence we'd require the best hardware as the fastest wins. 

# Refrences 
[Investopedia](https://www.investopedia.com/terms/b/bitcoin.asp)

[Computerphile Video](https://www.youtube.com/watch?v=wTC31ZI6QM4)

[Codebasics Video](https://www.youtube.com/watch?v=ZhnJ1bkIWWk&t=143s)

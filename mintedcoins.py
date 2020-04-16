#!/usr/bin/env python3
import json
from urllib.request import urlopen

url_blockheight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
result_blockheight = json.loads(url_blockheight)
blockheight = int(result_blockheight['height'])

url_price = urlopen('https://www.bitstamp.net/api/ticker/').read()
result_url_price = json.loads(url_price)
dollar_per_btc = float(result_url_price['ask'])

block_halving  = 210000
first_halving  = 210000
second_halving = 420000
third_halving  = 630000
fourth_halving = 840000

bitcoin_hardcap = 21000000

total_coins = 0;

if blockheight > first_halving:
	total_coins = block_halving * 50

if blockheight > second_halving:
	total_coins = total_coins + block_halving * 25

if blockheight > third_halving:
	total_coins = total_coins + block_halving * 12.5

elif blockheight < third_halving:
	temp = blockheight - second_halving
	total_coins = total_coins + (temp * 12.5)

if blockheight > fourth_halving:
	total_coins = total_coins + block_halving * 6.25

elif blockheight < fourth_halving and blockheight > third_halving:
	temp = blockheight - third_halving
	total_coins = total_coins + (temp * 6.25)

percentage_mined = total_coins / bitcoin_hardcap * 100

print (f"Bitcoins in circulation : {int(total_coins):,d}",", {0:.2f}%".format(round(percentage_mined,2)))
print (f"Bitcoins left to mine  : {int(bitcoin_hardcap - total_coins):,d}")
print (f"Market capitalization : {int(total_coins * dollar_per_btc):,d}$")

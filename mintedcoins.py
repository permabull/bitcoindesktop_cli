#!/usr/bin/env python3
import json
from urllib.request import urlopen

urlBlockHeight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
resultBlockHeight = json.loads(urlBlockHeight)
blockheight = int(resultBlockHeight['height'])

urlPrice = urlopen('https://www.bitstamp.net/api/ticker/').read()
resultUrlPrice = json.loads(urlPrice)
dollarPerBtc = float(resultUrlPrice['ask'])

blockHalving  = 210000
firstHalving  = 210000
secondHalving = 420000
thirdHalving  = 630000
fourthHalving = 840000

hardCap = 21000000

totalCoins = 0;

if blockheight > firstHalving:
	totalCoins = blockHalving * 50

if blockheight > secondHalving:
	totalCoins = totalCoins + blockHalving * 25

if blockheight > thirdHalving:
	totalCoins = totalCoins + blockHalving * 12.5

elif blockheight < thirdHalving:
	temp = blockheight - secondHalving
	totalCoins = totalCoins + (temp * 12.5)

if blockheight > fourthHalving:
	totalCoins = totalCoins + blockHalving * 6.25

elif blockheight < fourthHalving and blockheight > thirdHalving:
	temp = blockheight - thirdHalving
	totalCoins = totalCoins + (temp * 6.25)

percentageMined = totalCoins / hardCap * 100

print ("Bitcoins in circulation :",f"{int(totalCoins):,d}",", {0:.2f}%".format(round(percentageMined,2)))
print ("Bitcoins left to mine  :",f"{int(hardCap - totalCoins):,d}")
print ("Market capitalization :",f"{int(totalCoins * dollarPerBtc):,d}$")

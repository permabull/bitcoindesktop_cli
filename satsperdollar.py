#!/usr/bin/env python3
import json
from urllib.request import urlopen

urlPrice = urlopen('https://www.bitstamp.net/api/ticker/').read()
resultUrlPrice = json.loads(urlPrice)
dollarPerBtc = float(resultUrlPrice['ask'])

satPerDollar = 100000000 / dollarPerBtc

print("Sats/Dollar : {:.0f}".format(satPerDollar))

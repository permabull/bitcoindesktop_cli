#!/usr/bin/env python3
import json
from urllib.request import urlopen

urlPrice = urlopen('https://www.bitstamp.net/api/ticker/').read()
resultUrlPrice = json.loads(urlPrice)
dollarPerBtc = float(resultUrlPrice['ask'])

print("Price : {:.0f}$".format(dollarPerBtc))

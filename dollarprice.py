#!/usr/bin/env python3
import json
from urllib.request import urlopen

url_price = urlopen('https://www.bitstamp.net/api/ticker/').read()
result_url_price = json.loads(url_price)
dollarPerBtc = float(result_url_price['ask'])

print(f"Price : {int(dollarPerBtc):.0f}$")

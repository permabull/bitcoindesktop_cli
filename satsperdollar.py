#!/usr/bin/env python3
import json
from urllib.request import urlopen

url_price = urlopen('https://www.bitstamp.net/api/ticker/').read()
result_url_price = json.loads(url_price)
dollar_per_btc = float(result_url_price['ask'])

sat_per_dollar = 100000000 / dollar_per_btc

print("Sats/Dollar : {:.0f}".format(sat_per_dollar))

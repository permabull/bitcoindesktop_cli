#!/usr/bin/env python3
import json
from urllib.request import urlopen

url_fear_index = urlopen('https://api.alternative.me/fng/').read()
fear = json.loads(url_fear_index)
fear_index = (fear['data'])

fear = (([li["value"] for li in fear_index]))
market_sentiment = (([li["value_classification"] for li in fear_index]))

fear = fear[0]
sentiment = market_sentiment[0]

print(f"Fear index : {fear}")
print(f"Market sentiment : {sentiment}")

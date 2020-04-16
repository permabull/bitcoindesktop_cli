#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
import json
from urllib.request import urlopen

url_blockheight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
result_blockHeight = json.loads(url_blockheight)
blockheight = int(result_blockHeight['height'])

blocks_left = 630000 - blockheight

minutes_left_until_halving = blocks_left * 10

hours_left_until_halving = minutes_left_until_halving / 60

days_left_until_halving = hours_left_until_halving / 24

estTime = datetime.now() + timedelta(days=days_left_until_halving)

print (f"Blocks left until halving {blocks_left}")
print (f"Halving is in :", int(days_left_until_halving), "Days,", "Est date :", estTime.strftime("%Y-%m-%d: %H:%M:%S"))

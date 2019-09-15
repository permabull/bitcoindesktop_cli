#!/usr/bin/env python3

import json
from urllib.request import urlopen

urlBlockHeight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
resultBlockHeight = json.loads(urlBlockHeight)
blockheight = int(resultBlockHeight['height'])

print("Blockheight : ", blockheight)

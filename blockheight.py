#!/usr/bin/env python3

import json
from urllib.request import urlopen

url_blockheight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
result_blockheight = json.loads(url_blockheight)
blockheight = int(result_blockheight['height'])

print(f"Blockheight : {blockheight}")


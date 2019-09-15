#!/usr/bin/env python3

import json
from urllib.request import urlopen

urlFees = urlopen('https://mempool.space:8999/api/v1/fees/recommended').read()
resultFees = json.loads(urlFees)
fastestFee = int(resultFees['fastestFee'])
halfHourFee = int(resultFees['halfHourFee'])
hourFee = int(resultFees['hourFee'])

print("FastestFee : ",  fastestFee, " sat/byte")
print("HalfhourFee : ", halfHourFee, " sat/byte")
print("HourFee : ",     hourFee, " sat/byte")

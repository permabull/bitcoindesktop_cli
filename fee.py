#!/usr/bin/python3

import json
from urllib.request import urlopen

url_fees = urlopen('https://mempool.space/api/v1/fees/recommended').read()
result_fees = json.loads(url_fees)
fastest_fee = int(result_fees['fastestFee'])
half_hour_fee = int(result_fees['halfHourFee'])
hour_fee = int(result_fees['hourFee'])

print(f"FastestFee : {fastest_fee} sat/byte")
print(f"HalfhourFee : {half_hour_fee} sat/byte")
print(f"HourFee : {hour_fee} sat/byte")

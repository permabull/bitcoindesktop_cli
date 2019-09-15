#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
import json
from urllib.request import urlopen

urlBlockHeight = urlopen('https://api.blockcypher.com/v1/btc/main').read()
resultBlockHeight = json.loads(urlBlockHeight)
blockheight = int(resultBlockHeight['height'])

blocksLeft = 630000 - blockheight

minutesLeftUntilHalvening = blocksLeft * 10

hoursLefUntilHalvening = minutesLeftUntilHalvening / 60

daysLeftUntilHalvening = hoursLefUntilHalvening / 24

estTime = datetime.now() + timedelta(days=daysLeftUntilHalvening)

print ("Blocks left until halving : ", blocksLeft)
print ("Halving is in :", int(daysLeftUntilHalvening), "Days,", "Est date :", estTime.strftime("%Y-%m-%d: %H:%M:%S"))

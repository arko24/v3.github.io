import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&limit=24'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')

#tampil
for i in range(len(bd)):
    print(f"{bd[i]['longAccount']}"+' | '+f"{bd[i]['shortAccount']}")

timestamp

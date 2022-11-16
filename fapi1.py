import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&limit=10'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

def xharga2(coin):
#  url = 'https://fapi.binance.com/futures/data/topLongShortAccountRatio?symbol=BTCUSDT&period=5m&limit=10'
  url = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=ETHUSDT&period=5m&limit=10'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
bd2 = xharga2('')

#tampil
for i in range(len(bd)):
    h1 = (f"{bd[i]['longAccount']}"+' | '+f"{bd[i]['shortAccount']}")

print('=====')

for i in range(len(bd2)):
    h2 = (f"{bd2[i]['longAccount']}"+' | '+f"{bd2[i]['shortAccount']}")

print(h1+'   '+h2)

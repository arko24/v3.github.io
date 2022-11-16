import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&limit=5'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

def xharga2(coin):
  url = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=ETHUSDT&period=5m&limit=5'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
bd2 = xharga2('')

#tampil
print('BTCUSDT')
for i in range(len(bd)):
    print = (f"{bd[i]['longAccount']}"+' | '+f"{bd[i]['shortAccount']}")

print('')
print('ETHUSDT')
for i in range(len(bd2)):
    print = (f"{bd2[i]['longAccount']}"+' | '+f"{bd2[i]['shortAccount']}")

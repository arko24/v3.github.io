import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://fapi.binance.com/fapi/v1/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

def xharga2(coin):
  url = 'https://fapi.binance.com/futures/data/topLongShortPositionRatio?symbol='
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
bd2 = xharga2('')
crn = ('USDT')
param = ('&period=5m&limit=1')

#tampil
for i in range(len(bd)):
    c1 =(f"{bd[i]['symbol']}")
    print(f"{bd2&(c1)&(param)})


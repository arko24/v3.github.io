import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://api.binance.com/api/v3/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
crn = ('USDT')
persen = ('-0.20')
price1 = ('0.0001')
#tampil
for i in range(len(bd)):
  if (bd[i]['symbol'][-4:]) == (crn) and (bd[i]['priceChangePercent']) < (persen) and (bd[i]['lastPrice']) > (price1)  :
    print(f"{bd[i]['symbol']}" +'  |  '+ f"{bd[i]['lastPrice']}")


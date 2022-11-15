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
persen = ('-0.10')

#tampil
for i in range(len(bd)):
  if (bd[i]['symbol'][-4:]) == (crn) and (bd[i]['priceChange']) < (persen):
    print(f"{i}. {bd[i]['symbol']}" + f"{i}. {bd[i][' lastPrice']}")


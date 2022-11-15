import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("clear", shell=True)

#class
def xharga(coin):
  url = 'https://api.binance.com/fapi/v1/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js


#parameter
bd = xharga('')
crn = ('USDT')
persen = ('-0.10')

#tampil
for i in range(len(bd)):
    print(f"{bd[i]['symbol']}" + f"{bd[i]['lastPrice']}")


import subprocess
import json
import requests as rq
import time, sys, datetime, os, click


#script 
subprocess.call("cls", shell=True)

#class
def xharga(coin):
  url = 'https://api.binance.com/api/v3/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter
bd = xharga('')
crn = ('BUSD')

#tampil
print(bd['symbol'])

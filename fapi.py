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

def xharga3(coin):
#  url = 'https://api.binance.com/api/v3/ticker/24hr'
  url = 'https://fapi.binance.com/fapi/v1/ticker/24hr'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

def xharga4(coin):
  url = 'https://fapi.binance.com/futures/data/takerlongshortRatio?symbol=BTCUSDT&period=5m&limit=5'
  r = rq.get(url)
  js = json.loads(r.text)
  return js


def xharga5(coin):
  url = 'https://fapi.binance.com/futures/data/takerlongshortRatio?symbol=ETHUSDT&period=5m&limit=5'
  r = rq.get(url)
  js = json.loads(r.text)
  return js



#parameter
bd = xharga('')
bd2 = xharga2('')
bd3 = xharga3('')
bd4 = xharga4('')
bd5 = xharga5('')
crn = ('BUSD')
btc = ('BTCUSDT')
eth = ('ETHUSDT')
per = ('0.90')
per2 = ('1.10')

#tampil


print('BTCUSDT|'+'buy vol   |'+'sell vol  ')
for i in range(len(bd4)):
    print(f"{bd4[i]['buySellRatio']}"+' | '+f"{bd4[i]['buyVol']}"+' | '+f"{bd4[i]['sellVol']}")

print('')
for i in range(len(bd3)):
    if (bd3[i]['symbol']) == (btc):
      print(f"{bd3[i]['symbol']}" +' : '+f"{bd3[i]['lastPrice']}")
for i in range(len(bd)):
    print(f"{bd[i]['longAccount']}"+' | '+f"{bd[i]['shortAccount']}")
    
print('')
print('ETHUSDT|'+'buy vol   |'+'sell vol  ')
for i in range(len(bd5)):
    print(f"{bd5[i]['buySellRatio']}"+' | '+f"{bd5[i]['buyVol']}"+' | '+f"{bd5[i]['sellVol']}")
    
print('')
for i in range(len(bd3)):
    if (bd3[i]['symbol']) == (eth):
      print(f"{bd3[i]['symbol']}"+' : '+f"{bd3[i]['lastPrice']}")
for i in range(len(bd2)):
    print(f"{bd2[i]['longAccount']}"+' | '+f"{bd2[i]['shortAccount']}")

print('')
print('')    
print ('harga bawah')
for i in range(len(bd3)):
    if (bd3[i]['symbol'][-4:]) == (crn) and float(bd3[i]['lastPrice']) < float(bd3[i]['openPrice']) * float(per) :
      print(f"{bd3[i]['symbol']}" +'  price : '+ f"{bd3[i]['lastPrice']}"+'  open : '+f"{bd3[i]['openPrice']}"+'  high : '+f"{bd3[i]['highPrice']}"+'  low : '+f"{bd3[i]['lowPrice']}"+'  avg : '+f"{bd3[i]['weightedAvgPrice']}"+'  percent : '+f"{bd3[i]['priceChangePercent']}")

print('')    
print ('harga atas')
for i in range(len(bd3)):
    if (bd3[i]['symbol'][-4:]) == (crn) and float(bd3[i]['lastPrice']) > float(bd3[i]['openPrice']) * float(per2) :
      print(f"{bd3[i]['symbol']}" +'  price : '+ f"{bd3[i]['lastPrice']}"+'  open : '+f"{bd3[i]['openPrice']}"+'  high : '+f"{bd3[i]['highPrice']}"+'  low : '+f"{bd3[i]['lowPrice']}"+'  avg : '+f"{bd3[i]['weightedAvgPrice']}"+'  percent : '+f"{bd3[i]['priceChangePercent']}")


import subprocess
import json
import requests as rq
import time, sys, datetime, os, click
from datetime import datetime


#script 
subprocess.call("cls", shell=True)

#class
def xharga(coin):
  url = 'https://indodax.com/api/summaries'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

def xharga2(coin):
  url = 'https://testnet.binance.vision/api/v3/ticker/price'
  r = rq.get(url)
  js = json.loads(r.text)
  return js

#parameter banding
bd = xharga('')
bd2 = xharga2('')

#parameter harga all
a1 = ('btc_idr')
a2 = ('usdt_idr')
a3 = ('bear_usdt')
a4 = ('btc_usdt')
a5 = ('bull_usdt')
a6 = ('eth_idr')
a7 = ('ethbull_usdt')
a8 = ('bnbbull_usdt')

#parameter harga all2
b1 = ('btcidr')
b2 = ('usdtidr')
b3 = ('bearusdt')
b4 = ('btcusdt')
b5 = ('bullusdt')
b6 = ('ethidr')
b7 = ('ethbull_usdt')
b8 = ('bnbbull_usdt')

#masukan Aset
#k0 = (float('0.56709822')*float(bd['tickers'][a2]['last']))
k0 = (float('1.5')*float(bd['tickers'][a2]['last']))
k2 = (float('807910.48519736')*float(bd['tickers'][a2]['last']))
k3 = (float('9.0521571')*float(bd['tickers'][a2]['last']))
k4 = (float('4.10860236')*float(bd['tickers'][a2]['last']))

#support / resistant harian
RS3 = float('20999.5')
RS2 = float('20264.4')
RS1 = float('19810.2')
SS1 = float('18339.8')
SS2 = float('17885.6')
SS3 = float('17150.5')

#binance
bi1 = (float(bd2[7]['price']))
bi12 = (float(bd2[8]['price']))

#tampilkan harga BTC
print('==========================================')
ax1 = (float(bd['tickers'][a5]['last'])*float(k0))
ax2 = (float(bd['tickers'][a3]['last'])*float(k2))
print('ESTIMASI BULL     :''{:16,.2f}'.format(float(bd['tickers'][a5]['last'])*float(k0)))
#print('ESTIMASI ETH BULL :''{:16,.2f}'.format(float(bd['tickers'][a7]['last'])*float(k3)))
print('ESTIMASI BEAR     :''{:16,.2f}'.format(float(bd['tickers'][a3]['last'])*float(k2)))
#print('ESTIMASI BNB BULL :''{:16,.2f}'.format(float(bd['tickers'][a8]['last'])*float(k4)))
#print('ESTIMASI ASET    :''{:16,.2f}'.format((ax1)+(ax2)))

print('==========================================')
print ('USDT     :'+'{:10,.2f}'.format(float((bd ['tickers'][a2]['last'])))+'  LOW   :'+'{:10,.2f}'.format(float((bd ['tickers'][a2]['low']))))
print ('BULL     :'+'{:10,.2f}'.format(float((bd ['tickers'][a5]['last'])))+'  LOW   :'+'{:10,.2f}'.format(float((bd ['tickers'][a5]['low']))))
print ('BEAR     :'+'{:10,.6f}'.format(float((bd ['tickers'][a3]['last'])))+'  HIGH  :'+'{:10,.6f}'.format(float((bd ['tickers'][a3]['high']))))
print ('ETHBULL  :'+'{:10,.2f}'.format(float((bd ['tickers'][a7]['last'])))+'  LOW   :'+'{:10,.2f}'.format(float((bd ['tickers'][a7]['low']))))
print ('BNBBULL  :'+'{:10,.2f}'.format(float((bd ['tickers'][a8]['last'])))+'  LOW   :'+'{:10,.2f}'.format(float((bd ['tickers'][a8]['low']))))
 
print('==========================================')
print ('VOL BTC  :'+'{:10,.2f}'.format(float((bd ['tickers'][a1]['vol_btc'])))+'  ==>    31.87')
print ('VOL ETH  :'+'{:10,.2f}'.format(float((bd ['tickers'][a6]['vol_eth'])))+'  ==>   393.96')



R3 = (float(RS3)*float(bd['tickers'][a2]['last']))
R2 = (float(RS2)*float(bd['tickers'][a2]['last']))
R1 = (float(RS1)*float(bd['tickers'][a2]['last']))
S1 = (float(SS1)*float(bd['tickers'][a2]['last']))
S2 = (float(SS2)*float(bd['tickers'][a2]['last']))
S3 = (float(SS3)*float(bd['tickers'][a2]['last']))

print('==========================================')
print('BTC BINANCE : '+'{:10,.2f}'.format((bi1))+' | HIGH :'+'{:10,.2f}'.format(float(bd['tickers'][a1]['high'])/float(bd['tickers'][a2]['last'])))
print('BTC INDODAX : ''{:10,.2f}'.format(float(bd['tickers'][a1]['last'])/float(bd['tickers'][a2]['last']))+' | LOW  :'+'{:10,.2f}'.format(float(bd['tickers'][a1]['low'])/float(bd['tickers'][a2]['last'])))
print('ETH BINANCE : '+'{:10,.2f}'.format((bi12))+' | HIGH :'+'{:10,.2f}'.format(float(bd['tickers'][a6]['high'])/float(bd['tickers'][a2]['last'])))
print('ETH INDODAX : ''{:10,.2f}'.format(float(bd['tickers'][a6]['last'])/float(bd['tickers'][a2]['last']))+' | LOW  :'+'{:10,.2f}'.format(float(bd['tickers'][a6]['low'])/float(bd['tickers'][a2]['last'])))
print('==========================================')
print('FIBONACCI WEEKLY')
if (bi1) > (RS3):
  print ('RESIST 3 :'+ '{:16,.2f}'.format(R3)+' | '+ '{:6,.2f}'.format(float(RS3))+ ' <==')
  X1 = float('0')
else:
  print ('RESIST 3 :'+ '{:16,.2f}'.format(R3)+' | '+ '{:6,.2f}'.format(float(RS3)))
  X1 = float('1')
if (bi1) > (RS2):
  print ('RESIST 2 :'+ '{:16,.2f}'.format(R2)+' | '+ '{:6,.2f}'.format(float(RS2))+  ' <==')
  X2 = float('0')
else:
  print ('RESIST 2 :'+ '{:16,.2f}'.format(R2)+' | '+ '{:6,.2f}'.format(float(RS2)))
  X2 = float('1')
if (bi1) > (RS1):
  print ('RESIST 1 :'+ '{:16,.2f}'.format(R1)+' | '+ '{:6,.2f}'.format(float(RS1))+  ' <==')
  X3 = float('0')
else:
  print ('RESIST 1 :'+ '{:16,.2f}'.format(R1)+' | '+ '{:6,.2f}'.format(float(RS1)))
  X3 = float('1')
if (bi1) > (SS1):
  print ('SUPORT 1 :'+ '{:16,.2f}'.format(S1)+' | '+ '{:6,.2f}'.format(float(SS1))+  ' <==')
  X4 = float('-1')
else:
  print ('SUPORT 1 :'+ '{:16,.2f}'.format(S1)+' | '+ '{:6,.2f}'.format(float(SS1)))
  X4 = float('0')
if (bi1) > (SS2):
  print ('SUPORT 2 :'+ '{:16,.2f}'.format(S2)+' | '+ '{:6,.2f}'.format(float(SS2))+  ' <==')
  X5 = float('-1')
else:
  print ('SUPORT 2 :'+ '{:16,.2f}'.format(S2)+' | '+ '{:6,.2f}'.format(float(SS2)))
  X5 = float('0')
if (bi1) > (SS3):
  print ('SUPORT 3 :'+ '{:16,.2f}'.format(S3)+' | '+ '{:6,.2f}'.format(float(SS3))+  ' <==')
  X6 = float('-1')
else:
  print ('SUPORT 3 :'+ '{:16,.2f}'.format(S3)+' | '+ '{:6,.2f}'.format(float(SS3)))
  X6 = float('0')

print('==========================================')
#print analisa
XX = (X1+X2+X3+X4+X5+X6)
print('HASIL ANALISA')
if (XX) == float('-3'):
  print ('RESISTEN 3 BREAK (SUPER BULLISH):  '+ '{:6,.2f}'.format(float(bi1)-(RS3)))

if (XX) == float('-2'):
  print ('RESISTEN 2 BREAK (MOST BULLISH) :  '+ '{:6,.2f}'.format(float(bi1)-(RS2)))

if (XX) == float('-1'):
  print ('RESISTEN 1 BREAK (BULLISH)      :  '+ '{:6,.2f}'.format(float(bi1)-(RS1)))

if (XX) == float('0'):
  print ('PIVOT (BEARISH/BULLISH) : '+ '{:6,.2f}'.format(float(bi1)-(SS1)) + ' | '+ '{:6,.2f}'.format(float(bi1)-(RS1)))

if (XX) == float('1'):
  print ('SUPPORT 1 BREAK (BEARISH)       :  '+ '{:6,.2f}'.format(float(bi1)-(SS1)))

if (XX) == float('2'):
  print ('SUPPORT 2 BREAK (MOST BEARISH)  :  '+ '{:6,.2f}'.format(float(bi1)-(SS2)))

if (XX) == float('3'):
  print ('SUPPORT 3 BREAK (SUPER BEARISH) :  '+ '{:6,.2f}'.format(float(bi1)-(SS3)))


#https://localbitcoins.com/bitcoincharts/PEN/trades.json?since=15335474
import sys
import urllib.request, json
import pandas as pd
import datetime
import time


justnow=time.time()-3600
print (justnow)
print (datetime.datetime.fromtimestamp(justnow))
ttime=0
ctid=10000
while ttime < justnow:
    with urllib.request.urlopen("https://localbitcoins.com/bitcoincharts/PEN/trades.json?since="+str(ctid)) as url:
        data = json.loads(url.read().decode())
    a = len(data)
    ctid =data[a-1]['tid']
    df = pd.DataFrame(data)
    df.to_csv("out.csv",mode='a', header=False)
    ttime = data[a-1]['date']
    print(datetime.datetime.fromtimestamp(ttime))
    print(ctid)
    print(ttime)
print (time.time())



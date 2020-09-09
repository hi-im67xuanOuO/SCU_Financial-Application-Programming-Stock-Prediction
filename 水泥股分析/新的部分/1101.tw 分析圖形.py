import requests
from io import StringIO
import pandas as pd
import numpy as np

def crawl_price(date):
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL')
    ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                        for i in r.text.split('\n') 
                                        if len(i.split('",')) == 17 and i[0] != '='])), header=0)
    ret = ret.set_index('證券代號')
    ret['成交金額'] = ret['成交金額'].str.replace(',','')
    ret['成交股數'] = ret['成交股數'].str.replace(',','')
    return ret


import datetime
import time
import matplotlib.pyplot as plt

data = {}
n_days = 90
date = datetime.datetime.now()
fail_count = 0
allow_continuous_fail_count = 50
while len(data) < n_days:
    try:
        # 抓資料
        data[date.date()] = crawl_price(date)
        fail_count = 0
    except:
        fail_count += 1
        if fail_count == allow_continuous_fail_count:
            raise
            break
    # 減一天
    date -= datetime.timedelta(days=1)
    time.sleep(10)
    
close = pd.DataFrame({k:d['收盤價'] for k,d in data.items()}).transpose()
close.index = pd.to_datetime(close.index)

open = pd.DataFrame({k:d['開盤價'] for k,d in data.items()}).transpose()
open.index = pd.to_datetime(open.index)

high = pd.DataFrame({k:d['最高價'] for k,d in data.items()}).transpose()
high.index = pd.to_datetime(high.index)

low = pd.DataFrame({k:d['最低價'] for k,d in data.items()}).transpose()
low.index = pd.to_datetime(low.index)

volume = pd.DataFrame({k:d['成交股數'] for k,d in data.items()}).transpose()
volume.index = pd.to_datetime(volume.index)

#print( close )

taini = {
    'close':close['1101']['2020'].dropna().astype(float),
    'open':open['1101']['2020'].dropna().astype(float),
    'high':high['1101']['2020'].dropna().astype(float),
    'low':low['1101']['2020'].dropna().astype(float),
    'volume': volume['1101']['2020'].dropna().astype(float),
}

taini['volume'].plot()
#taini['close'].plot()

import talib
from talib import abstract

def talib2df(talib_output):
    if type(talib_output) == list:
        ret = pd.DataFrame(talib_output).transpose()
    else :
        ret = pd.Series(talib_output)
    ret.index = taini['close'].index
    ret.fillna(0)
    return ret

#ax.set_xlim(, right)
#KD
talib2df(talib.abstract.STOCH(taini)).plot()
taini['close'].plot(secondary_y=True)
plt.savefig("kd.png")
plt.show()
plt.cla()

#RSI
talib2df(talib.abstract.RSI(taini)).plot()
taini['close'].plot(secondary_y=True)
plt.savefig("rsi.png")
plt.cla()
#MACD
talib2df(abstract.STOCH(taini, fastk_period=9)).plot()
taini['close'].plot(secondary_y=True)
plt.savefig("macd.png")
plt.show()
plt.cla()
#OBV
talib2df(abstract.OBV(taini)).plot()
taini['close'].plot(secondary_y=True)
plt.savefig("obv.png")
plt.cla()
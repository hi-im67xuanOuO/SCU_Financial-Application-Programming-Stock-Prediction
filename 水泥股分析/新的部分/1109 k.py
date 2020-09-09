import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib
import matplotlib.pyplot as plt
import mpl_finance as mpf

import seaborn as sns
import datetime as datetime

#talib

start = datetime.datetime(2020,1,1)
df_1109 = pdr.DataReader('1109.TW', 'yahoo', start=start)

df_1109.index = df_1109.index.format(formatter=lambda x: x.strftime('%Y-%m-%d')) 

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(range(0, len(df_1109.index), 10))
ax.set_xticklabels(df_1109.index[::10])
mpf.candlestick2_ochl(ax, df_1109['Open'], df_1109['Close'], df_1109['High'],
                      df_1109['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75);
import talib
sma_10 = talib.SMA(np.array(df_1109['Close']), 10)
sma_30 = talib.SMA(np.array(df_1109['Close']), 30)

fig = plt.figure(figsize=(10,4))
ax = fig.add_axes([0,0.2,1,0.5])
ax2 = fig.add_axes([0,0,1,0.2])

ax.set_xticks(range(0, len(df_1109.index), 10))
ax.set_xticklabels(df_1109.index[::10])
mpf.candlestick2_ochl(ax, df_1109['Open'], df_1109['Close'], df_1109['High'],
                      df_1109['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75)
plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 
ax.plot(sma_10, label='10日均線')
ax.plot(sma_30, label='30日均線')

mpf.volume_overlay(ax2, df_1109['Open'], df_1109['Close'], df_1109['Volume'], colorup='r', colordown='g', width=0.5, alpha=0.8)
ax2.set_xticks(range(0, len(df_1109.index), 10))
ax2.set_xticklabels(df_1109.index[::10])

ax.legend();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:13:34 2020

@author: liuqingxuan
"""

import pandas as pd
import requests
dfs=pd.read_html("https://www.cnyes.com/twstock/ps_historyprice/2330.htm")
print(dfs)

import pandas_datareader.data as web
import datetime
import pandas as pd
start = datetime.datetime(2000,1,20)
end = datetime.datetime(2000,3,23)
df_2330 = web.DataReader('2330.TW','yahoo',start,end)
print(df_2330.head(5))
print(df_2330.tail(5))

df_stock = web.DataReader(['2330.TW','0050.TW','2412.TW'],'yahoo',start,end)
print(df_stock.tail(5))

writer = pd.ExcelWriter('stock2330.xlsx')
df_stock.to_excel(writer,'Sheet1')
writer.save()


import pandas as pd
import pandas_datareader.data as pdr
import datetime as datetime
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt

#國泰金控(2882)為範例
stock_number = '2882.TW'
start = datetime.datetime(2018,1,1)
end   = datetime.datetime(2018,6,1)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)

print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')

AX.legend();
AX2.legend();
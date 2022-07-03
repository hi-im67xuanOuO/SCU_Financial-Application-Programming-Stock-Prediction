import pandas as pd
import pandas_datareader as pdr
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

fig = plt.figure(figsize=(5,5))
AX3 = fig.add_axes([0.1,0.5,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')

AX.legend();
AX2.legend();

AX3.plot(DataFrame['Open'],label='Open',color='B')
AX3.plot(DataFrame['High'],label='High',color='G')
#AX3.plot(DataFrame['Low'],label='High',color='G')

#c=DataFrame['Close']
#近60日收盤
c60=DataFrame['Close'].rolling(60,min_periods=1).mean()

#畫圖
AX3.plot(c60,label='60MA',color='R')

AX.legend();
AX2.legend();
AX3.legend();
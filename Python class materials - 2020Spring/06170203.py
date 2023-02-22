#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:15:06 2020

@author: liuqingxuan
"""

#df_stock=web.DataReader(['1101.TW','1101B.TW','1102.TW','1103.TW','1104.TW','1104.TW','1108.TW','1109.TW','1110.TW'],'yahoo',start,end)

import pandas as pd
import pandas_datareader.data as pdr
import datetime as datetime
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt

#台泥(1101)為範例
stock_number = '1101.TW'
tart = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,24)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)
num = len(DataFrame)

#計算每日報酬率
DataFrame['TurnOver']=0.00000
for i in range(num):
    DataFrame['TurnOver'][i] = (DataFrame['Close'][i]-DataFrame['Open'][i])/DataFrame['Open'][i]

#print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])
fig2 = plt.figure(figsize=(5, 5))
AX3 = fig2.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)
AX3.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')
#TurnOver
AX3.plot(DataFrame['TurnOver'], label='TurnOver', color='B')

AX.legend();
AX2.legend();
AX3.legend();


#正向操作
#True/False
DataFrame['TF']=0
for i in range(num):
    if DataFrame['TurnOver'][i] > 0.002:
        DataFrame['TF'][i] = 1 #漲幅大於0.002時 TF為1
    else:
        DataFrame['TF'][i] = 0 #小於則為0

#print(DataFrame)


#買賣動作欄位
DataFrame['PL']=0.000000
#購買價格
long=0.000000

n=2 #因為看到第二筆，才有資料可以判斷，如果是weekly要設7，以此類推
while(n<num): #當n小於所有筆數時，繼續執行以下程式
  if(DataFrame['TF'][n-1]==0 and DataFrame['TF'][n]==1): #當大漲的事實觸發時
    long= float(DataFrame['Close'][n])#趕快尾盤跳下去買
    while (DataFrame['TF'][n]==1 and n<num):#當大漲情況維持，則持續hold
      n = n+1 #筆數往後看
    DataFrame['PL'][n]=(DataFrame['Close'][n])-(long)-(DataFrame['Close'][n])*0.00585 
    #當大漲情況消失時執行(while不成立時執行)，也就是賣掉股票，此值為獲利
  n=n+1
  
print(DataFrame)








stock_number = '1102.TW'
tart = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,24)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)
num = len(DataFrame)

#計算每日報酬率
DataFrame['TurnOver']=0.00000
for i in range(num):
    DataFrame['TurnOver'][i] = (DataFrame['Close'][i]-DataFrame['Open'][i])/DataFrame['Open'][i]

#print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])
fig2 = plt.figure(figsize=(5, 5))
AX3 = fig2.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)
AX3.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')
#TurnOver
AX3.plot(DataFrame['TurnOver'], label='TurnOver', color='B')

AX.legend();
AX2.legend();
AX3.legend();


#正向操作
#True/False
DataFrame['TF']=0
for i in range(num):
    if DataFrame['TurnOver'][i] > 0.002:
        DataFrame['TF'][i] = 1 #漲幅大於0.002時 TF為1
    else:
        DataFrame['TF'][i] = 0 #小於則為0

#print(DataFrame)


#買賣動作欄位
DataFrame['PL']=0.000000
#購買價格
long=0.000000

n=2 #因為看到第二筆，才有資料可以判斷，如果是weekly要設7，以此類推
while(n<num): #當n小於所有筆數時，繼續執行以下程式
  if(DataFrame['TF'][n-1]==0 and DataFrame['TF'][n]==1): #當大漲的事實觸發時
    long= float(DataFrame['Close'][n])#趕快尾盤跳下去買
    while (DataFrame['TF'][n]==1 and n<num):#當大漲情況維持，則持續hold
      n = n+1 #筆數往後看
    DataFrame['PL'][n]=(DataFrame['Close'][n])-(long)-(DataFrame['Close'][n])*0.00585 #當大漲情況消失時執行(while不成立時執行)，也就是賣掉股票，此值為獲利
  n=n+1
  
print(DataFrame)







stock_number = '1108.TW'
tart = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,24)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)
num = len(DataFrame)

#計算每日報酬率
DataFrame['TurnOver']=0.00000
for i in range(num):
    DataFrame['TurnOver'][i] = (DataFrame['Close'][i]-DataFrame['Open'][i])/DataFrame['Open'][i]

#print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])
fig2 = plt.figure(figsize=(5, 5))
AX3 = fig2.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)
AX3.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')
#TurnOver
AX3.plot(DataFrame['TurnOver'], label='TurnOver', color='B')

AX.legend();
AX2.legend();
AX3.legend();


#正向操作
#True/False
DataFrame['TF']=0
for i in range(num):
    if DataFrame['TurnOver'][i] > 0.035:
        DataFrame['TF'][i] = 1 #漲幅大於0.002時 TF為1
    else:
        DataFrame['TF'][i] = 0 #小於則為0

#print(DataFrame)


#買賣動作欄位
DataFrame['PL']=0.000000
#購買價格
long=0.000000

n=2 #因為看到第二筆，才有資料可以判斷，如果是weekly要設7，以此類推
while(n<num): #當n小於所有筆數時，繼續執行以下程式
  if(DataFrame['TF'][n-1]==0 and DataFrame['TF'][n]==1): #當大漲的事實觸發時
    long= float(DataFrame['Close'][n])#趕快尾盤跳下去買
    while (DataFrame['TF'][n]==1 and n<num):#當大漲情況維持，則持續hold
      n = n+1 #筆數往後看
    DataFrame['PL'][n]=(DataFrame['Close'][n])-(long)-(DataFrame['Close'][n])*0.00585 #當大漲情況消失時執行(while不成立時執行)，也就是賣掉股票，此值為獲利
  n=n+1
  
print(DataFrame)







stock_number = '1109.TW'
tart = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,24)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)
num = len(DataFrame)

#計算每日報酬率
DataFrame['TurnOver']=0.00000
for i in range(num):
    DataFrame['TurnOver'][i] = (DataFrame['Close'][i]-DataFrame['Open'][i])/DataFrame['Open'][i]

#print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])
fig2 = plt.figure(figsize=(5, 5))
AX3 = fig2.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)
AX3.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')
#TurnOver
AX3.plot(DataFrame['TurnOver'], label='TurnOver', color='B')

AX.legend();
AX2.legend();
AX3.legend();


#正向操作
#True/False
DataFrame['TF']=0
for i in range(num):
    if DataFrame['TurnOver'][i] > 0.008:
        DataFrame['TF'][i] = 1 #漲幅大於0.002時 TF為1
    else:
        DataFrame['TF'][i] = 0 #小於則為0

#print(DataFrame)


#買賣動作欄位
DataFrame['PL']=0.000000
#購買價格
long=0.000000

n=2 #因為看到第二筆，才有資料可以判斷，如果是weekly要設7，以此類推
while(n<num): #當n小於所有筆數時，繼續執行以下程式
  if(DataFrame['TF'][n-1]==0 and DataFrame['TF'][n]==1): #當大漲的事實觸發時
    long= float(DataFrame['Close'][n])#趕快尾盤跳下去買
    while (DataFrame['TF'][n]==1 and n<num):#當大漲情況維持，則持續hold
      n = n+1 #筆數往後看
    DataFrame['PL'][n]=(DataFrame['Close'][n])-(long)-(DataFrame['Close'][n])*0.00585 #當大漲情況消失時執行(while不成立時執行)，也就是賣掉股票，此值為獲利
  n=n+1
  
print(DataFrame)







stock_number = '1110.TW'
tart = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,3,24)
DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)
num = len(DataFrame)

#計算每日報酬率
DataFrame['TurnOver']=0.00000
for i in range(num):
    DataFrame['TurnOver'][i] = (DataFrame['Close'][i]-DataFrame['Open'][i])/DataFrame['Open'][i]

#print(DataFrame)

#畫圖
fig = plt.figure(figsize=(5, 5))
AX  = fig.add_axes([0.1,0.5,1,0.2])
AX2 = fig.add_axes([0.1,0.1,1,0.2])
fig2 = plt.figure(figsize=(5, 5))
AX3 = fig2.add_axes([0.1,0.1,1,0.2])

#表格標題
AX.set_title(stock_number)
AX2.set_title(stock_number)
AX3.set_title(stock_number)

#收盤價
AX.plot(DataFrame['Close'], label='Close', color='B')
#成交量
AX2.bar(DataFrame.index, DataFrame['Volume'], label='Volume', color='R')
#TurnOver
AX3.plot(DataFrame['TurnOver'], label='TurnOver', color='B')

AX.legend();
AX2.legend();
AX3.legend();


#正向操作
#True/False
DataFrame['TF']=0
for i in range(num):
    if DataFrame['TurnOver'][i] > 0.006:
        DataFrame['TF'][i] = 1 #漲幅大於0.002時 TF為1
    else:
        DataFrame['TF'][i] = 0 #小於則為0

#print(DataFrame)


#買賣動作欄位
DataFrame['PL']=0.000000
#購買價格
long=0.000000

n=2 #因為看到第二筆，才有資料可以判斷，如果是weekly要設7，以此類推
while(n<num): #當n小於所有筆數時，繼續執行以下程式
  if(DataFrame['TF'][n-1]==0 and DataFrame['TF'][n]==1): #當大漲的事實觸發時
    long= float(DataFrame['Close'][n])#趕快尾盤跳下去買
    while (DataFrame['TF'][n]==1 and n<num):#當大漲情況維持，則持續hold
      n = n+1 #筆數往後看
    DataFrame['PL'][n]=(DataFrame['Close'][n])-(long)-(DataFrame['Close'][n])*0.00585 #當大漲情況消失時執行(while不成立時執行)，也就是賣掉股票，此值為獲利
  n=n+1
  
print(DataFrame)
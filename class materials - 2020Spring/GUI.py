#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:53:21 2020

@author: liuqingxuan
"""
import tkinter as tk
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import pandas as pd


window=tk.Tk()
window.title('輸入股票代號')
window.geometry('300x350+200+50')
window.configure(bg='lightgray')
label=tk.Label(window,
               text='輸入股票代號',
               bg='#6dcff2',#背景顏色
               font=('Arial',20),#字型及大小
               width=15,height=2)#文字標示尺寸

    
# 抓到今天的時間
now = datetime.datetime.now()

# 先與網站請求抓到價格
def getstock(stocknumber):
    
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20180814&stockNo=' + stocknumber + '&_=' + str(time.mktime(now.timetuple()))
    
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    
    # 判斷請求是否成功
    if getjson['stat'] != '很抱歉，沒有符合條件的資料!': 
        return [getjson['data']]
    else:
        return [] # 請求失敗回傳空值

def ratio(stocknumber):    
    # 第一步 載入所需套件 
    import requests
    import pandas as pd
    import numpy as np
    from io import StringIO
    
    # 第二步 爬取股票資訊（含本益比）
    stocklist = getstock(stocknumber)
    date = str(now.date())
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')

    # 第三步 篩選出個股盤後資訊
    str_list = []
    for i in r.text.split('\n'):
        if len(i.split('",')) == 17 and i[0] != '=':       
            i = i.strip(",\r\n")
            str_list.append(i)      

    # 第四步 印出選股資訊
    df = pd.read_csv(StringIO("\n".join(str_list)))  
    pd.set_option('display.max_rows', None)
    
    n = len(df['證券代號'])
    for i in range(n):
        if df['證券代號'][i]==str(stocknumber):
            print("該支股票今日本益比為：",df['本益比'][i],"\n")
            ratio = df['本益比'][i]
    
    # 判斷是否為空值
    if len(stocklist) == 0:
        print('請求失敗，請檢查您的股票代號')
    return ratio


def testing():
    
    stocknumber = str(entry.get())
    final = ratio(stocknumber)
    close = tkinter.messagebox.showinfo('Results',str(stocknumber) +' 本益比： ' +str(final)+'\n')


def other(stocknumber):
    # 第一步 載入所需套件 
    import requests
    import pandas as pd
    import numpy as np
    from io import StringIO
    
    # 第二步 爬取股票資訊（含本益比）
    stocklist = getstock(stocknumber)
    date = str(now.date())
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')

    # 第三步 篩選出個股盤後資訊
    str_list = []
    for i in r.text.split('\n'):
        if len(i.split('",')) == 17 and i[0] != '=':       
            i = i.strip(",\r\n")
            str_list.append(i)      

    # 第四步 印出選股資訊
    df = pd.read_csv(StringIO("\n".join(str_list)))  
    pd.set_option('display.max_rows', None)
    
    # 判斷是否為空值
    if len(stocklist) != 0:
        stockdf = pd.DataFrame(stocklist[0],columns=["日期","成交股數","成交金額","開盤價","最高價","最低價",
                                                     "收盤價","漲跌價差","成交筆數"])
        # 顯示結果
        close = stockdf['收盤價'][-1:].values[0]
        #middle= str(stockAverage)
        #STD = str(stockSTD)
    else:
        print('請求失敗，請檢查您的股票代號')
    return close


def testing2():
    
    stocknumber = str(entry.get())
    final2 = other(stocknumber)
    close2 = tkinter.messagebox.showinfo('Results',str(stocknumber) +' 當日收盤價： ' +str(final2)+'\n')


def createNewWindow():
    
    import pandas as pd
    import pandas_datareader as pdr
    import datetime as datetime
    from pandas.plotting import register_matplotlib_converters
    import matplotlib.pyplot as plt
#國泰金控(2882)為範例
    stocknumber= str(entry.get())
    stock_number = str(stocknumber+'.TW')
    start = datetime.datetime(2020,1,1)
    end   = datetime.datetime.now()
    DataFrame = pdr.DataReader(stock_number, 'yahoo', start, end)

    fig = plt.figure(figsize=(6, 4))
    AX  = fig.add_axes([0.1,0.5,0.8,0.5])
    AX.set_title(stock_number)
    AX.plot(DataFrame['Close'], label='Close', color='B')
    AX.legend();
    fig.savefig('plot.png')
    
    
def new_i():
    createNewWindow()

    root =tk.Toplevel()
    root.title('收盤價折線圖')        #窗口標題
    root.resizable(False, False)
    windowWidth = 500               #寬
    windowHeight = 300              #高
    screenWidth,screenHeight = root.maxsize()
    geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
    root.geometry(geometryParam) 
#label文本
 
#label圖片
    img_gif = tk.PhotoImage(file = 'plot.png')
    label_img = tk.Label(root, image = img_gif)
    label_img.pack()


    
    root.mainloop()



#製作 menu bar & 提示視窗
    
from tkinter import messagebox as mBox
from tkinter import Menu

# 離開程式的指令
def _quit():
    win.quit()
    win.destroy()
    exit()
    
# Creating a Menu Bar
menuBar = Menu(window)
window.config(menu=menuBar)
 
# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="退出", command=_quit)
menuBar.add_cascade(label="執行選項", menu=fileMenu)
 
# Display a Message Box
def _msgBox1():
    mBox.showinfo('Python Message Info Box', '使用須知：\n請輸入想查詢之股票代號，\n即可查詢該股票之本益比、當日收盤價與近期收盤價折線圖')
def _msgBox2():
    mBox.showwarning('Python Message Warning Box', '提示：\n請於網路狀態佳時使用，並稍後程式執行。')
def _msgBox4():
    answer = mBox.askyesno("Python Message Dual Choice Box", "您喜歡這個程式嗎？\n您的選擇是：") 
    if answer == True:
        mBox.showinfo('顯示選擇結果', '您選擇了“是”，謝謝參與！')
    else:
        mBox.showinfo('顯示選擇結果', '您選擇了“否”，謝謝參與！')
 
# Add another Menu to the Menu Bar and an item
msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label="使用須知 Box", command=_msgBox1)
msgMenu.add_command(label="提示 Box", command=_msgBox2)
msgMenu.add_separator()
msgMenu.add_command(label="使用者回饋", command=_msgBox4)
menuBar.add_cascade(label="使用須知與警示", menu=msgMenu)



#標示文字
label=tk.Label(window,
               text='輸入股票代號',
               bg='#6dcff2',#背景顏色
               font=('Arial',20),#字型及大小
               width=15,height=3)#文字標示尺寸
label.pack()

#輸入欄位
entry=tk.Entry(window,width=20)
entry.pack()

#按鈕
button1=tk.Button(window,text='顯示本益比',bg='#ACD6FF',font=('Arial',16),command=testing,width=10,height=2)

button2=tk.Button(window,text='折線圖收盤',bg='#ACD6FF',font=('Arial',16),command=new_i,width=10,height=2)

button3=tk.Button(window,text='當日收盤價',bg='#ACD6FF',font=('Arial',16),command=testing2,width=10,height=2)

button1.pack(side=tk.BOTTOM)#convert按鈕
button2.pack(side=tk.BOTTOM)#convert按鈕
button3.pack(side=tk.BOTTOM)#convert按鈕
window.mainloop()


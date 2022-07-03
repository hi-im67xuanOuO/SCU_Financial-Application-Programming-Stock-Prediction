#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:34:25 2020

@author: liuqingxuan
"""

import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title('title')
window.geometry("300x100+250+150")

def onOK():
    msg = "Hello, {}.".format(entry.get())
    tkinter.messagebox.showinfo(title ='Hello', #視窗標題
                                message = msg) #訊息內容

#標示文字
label = tk.Label(window, text = '姓名')
label.pack()

#輸入欄位
entry = tk.Entry(window, width = 20)
entry.pack()

#按鈕
button = tk.Button(window, text="OK", command=onOK)
button.pack()

window.mainloop()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:22:50 2020

@author: liuqingxuan
"""
#引入訊息視窗模組
import tkinter as tk 
#設定主視窗frame
window=tk.Tk() 
#設定視窗標題
window.title('title') 
#設定視窗大小為300x100,視窗（左上角）在螢幕上的座標位置為（250,150）
window.geometry("300x100+250+150")
#標示文字
label=tk.Label(window,#文字顯示所在視窗
               text='Label',#顯示文字
               bg='#00eec6',#背景顏色
               font=('Arial',12),#字型與大小
               width=15,height=2)#文字標示尺寸

#已預設方式排版標示文字
label.pack()
#最後呼叫mainloop的函數運行視窗程式
window.mainloop()
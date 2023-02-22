#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:17:53 2020

@author: liuqingxuan
"""

from turtle import *
color('blue', 'yellow') #畫筆顏色先、填滿顏色後
begin_fill() #開始填充
while True:
    forward(200) #往畫筆指向向前移動
    left(170) #角度逆時針170度，right為順時針
    if abs(pos()) < 1: #回傳畫筆座標，x軸與y軸座標絕對值小於1（意思其實就是回到起始點）
        break
end_fill() #結束填滿
done() #結束繪製
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:42:07 2020

@author: liuqingxuan
"""

import xlrd
import xlwt
from datetime import date,datetime

li1=[]
date=[]
data=xlrd.open_workbook('excelin2.xls')
table =data.sheets()[0]
num = table.nrows #共有幾列資料
for i in range(1,table.nrows):
    li1.append(table.cell(i,2).value-table.cell(i,3).value)

li1.sort(reverse=True) #差價
target = li1[4] #第五大

for i in range(1,table.nrows):
    a = table.cell(i,2).value-table.cell(i,3).value
    if a >= target:
        data_value=xlrd.xldate_as_tuple(table.cell(i,0).value,data.datemode)
        print('%d/%d/%d'%(data_value[0],data_value[1],data_value[2]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:21:49 2020

@author: liuqingxuan
"""

import csv
with open('csvin.csv','r') as fin:
    with open('csvout.csv','w') as fout:
        csvreader = csv.reader(fin, delimiter=',')
        csvwriter = csv.writer(fout, delimiter=',')
        header = next(csvreader)
        print(header)
        csvwriter.writerow(header)
        for row in csvreader:
            row[0] = row[0].replace('/','-')
            print(','.join(row))
            csvwriter.writerow(row)
            


import xlrd
import xlwt

li1=[]
data=xlrd.open_workbook('excelin.xls')
table =data.sheets()[0]
print('表格內共有%d列'%(table.nrows))
print('表格內共有%d行'%(table.ncols))
print('原始資料內容 = ')
for i in range(0,table.nrows):
    print(table.cell(i,0).value)
    li1.append(table.cell(i,0).value)
#write excel file
wb = xlwt.Workbook()
ws = wb.add_sheet('ClosePrice')
print('修改後的資料內容 = ')
for i in range(0,table.nrows):
    print(li1[i]+10000)
    ws.write(i,0,li1[i]+10000)
wb.save('excelout.xls')



import xlrd
import xlwt

li1=[]
data=xlrd.open_workbook('excelin2.xls')
table =data.sheets()[0]
x=xlrd.xldate_as_tuple(table.cell(1,0).value,0)
print(x)
print(x[1])
print('表格內共有%d列'%(table.nrows))
print('表格內共有%d行'%(table.ncols))
print('原始資料內容 = ')
for i in range(0,table.nrows):
    print(table.cell(i,2).value)
    li1.append(table.cell(i,2).value)
#write excel file
wb = xlwt.Workbook()
ws = wb.add_sheet('highestPrice')
print('修改後的資料內容 = ')
for i in range(0,table.nrows):
    print(li1[i])
    ws.write(i,0,li1[i])
wb.save('excelout2.xls')
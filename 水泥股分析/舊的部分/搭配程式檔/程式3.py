import pandas_datareader.data as web
import datetime
import pandas as pd
import xlrd#配對檔案excelin2.xls
import xlwt

import pandas_datareader.data as pdr
import datetime as datetime
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
start=datetime.datetime(2020,1,1)
end=datetime.datetime(2020,4,1)
df_2330=web.DataReader('1101.TW','yahoo',start,end)
#print(df_2330.head(5))#head(5)印五列
#print(df_2330.tail(5))
df_stock=web.DataReader(['1101.TW','1102.TW','1103.TW','1104.TW','1108.TW','1109.TW','1110.TW'],'yahoo',start,end)
writer=pd.ExcelWriter('stock.xls')#寫入excel
df_stock.to_excel(writer,'Sheet1')
writer.save()
data=xlrd.open_workbook('stock.xls')
table=data.sheets()[0]

df=pd.read_excel('stock.xls')
data=xlrd.open_workbook('stock.xls')   #開啟excel檔案
table = data.sheets()[0]              #開啟第一張表格
nrows = table.nrows
#1101
sum=0.0
b=0.0
c3=0.0
c2=0.0#月份
c4=0.0
#二月
for i in range(3,18):    
    sum=sum+float(table.cell(i,1).value)    
b=sum/15
#print(b)#平均股價
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,1).value)<b:
    
    print('二月初買1101')
else:
    c2+=1
    print('二月初不買1101')
#三月
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,1).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,1).value)<b:
    print('三月初買1101')
else:
    c3+=1
    print('三月初不買1101')
#四月  
for i in range(37,58):#1101     
    sum=sum+float(table.cell(i,1).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,1).value)<b:
    print('四月初買1101')
else:
    c4+=1
    print('四月初不買1101')
    

#1102
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,2).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,2).value)<b:
    print('二月初買1102')
else:
    c2+=1
    print('二月初不買1102')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,2).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,2).value)<b:
    print('三月初買1102')
else:
    c3+=1
    print('三月初不買1102')
#四月  
for i in range(37,58):#1101     
    sum=sum+float(table.cell(i,2).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,2).value)<b:
    print('四月初買1102')
else:
    c4+=1
    print('四月初不買1102')   
    
#1103
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,3).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,3).value)<b:
    print('二月初買1103')
else:
    c2+=1
    print('二月初不買1103')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,3).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,3).value)<b:
    print('三月初買1103')
else:
    c3+=1
    print('三月初不買1103')
#四月  
for i in range(37,58):#1101     
    sum=sum+float(table.cell(i,3).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,3).value)<b:
    print('四月初買1103')
else:
    c4+=1
    print('四月初不買1103')

#1104
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,4).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,4).value)<b:
    print('二月初買1104')
else:
    c2+=1
    print('二月初不買1104')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,4).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,4).value)<b:
    print('三月初買1104')
else:
    c3+=1
    print('三月初不買1104')
#四月  
for i in range(37,58):   
    sum=sum+float(table.cell(i,4).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,4).value)<b:
    print('四月初買1104')
else:
    c4+=1
    print('四月初不買1104')
cc2=0.0
cc3=0.0
cc4=0.0    
#1108
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,5).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,5).value)<b:
    print('二月初買1108')
else:
    cc2+=1
    print('二月初不買1108')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,5).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,5).value)<b:
    print('三月初買1108')
else:
    cc3+=1
    print('三月初不買1108')
#四月  
for i in range(37,58):   
    sum=sum+float(table.cell(i,5).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,5).value)<b:
    print('四月初買1108')
else:
    cc4+=1
    print('四月初不買1108')
    
#1109
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,6).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,6).value)<b:
    print('二月初買1109')
else:
    cc2+=1
    print('二月初不買1109')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,6).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,1).value)<b:
    print('三月初買1109')
else:
    cc3+=1
    print('三月初不買1109')
#四月  
for i in range(37,58):#1101     
    sum=sum+float(table.cell(i,6).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,6).value)<b:
    print('四月初買1109')
else:
    cc4+=1
    print('四月初不買1109') 
ccc2=0.0
ccc3=0.0
ccc4=0.0    
#1110
sum=0.0
for i in range(3,18):    
    sum=sum+float(table.cell(i,1).value)
    
a=sum
b=a/15
#print(table.cell(18,1).value) 19列     
if float(table.cell(18,7).value)<b:
    print('二月初買1110')
else:
    ccc2+=1
    print('二月初不買1110')
for i in range(18,37):#1101     
    sum=sum+float(table.cell(i,7).value)
    #print(sum)
a=sum
b=a/19 
if float(table.cell(37,7).value)<b:
    print('三月初買1110')
else:
    ccc3+=1
    print('三月初不買1110')
#四月  
for i in range(37,58):#1101     
    sum=sum+float(table.cell(i,7).value)
    #print(sum)
a=sum
b=a/21
if float(table.cell(58,7).value)<b:
    print('四月初買1110')
else:
    ccc4+=1
    print('四月初不買1110')

print(c2,c3,c4,cc2,cc3,cc4,ccc2,ccc3,ccc4)#==這四支二月都買

p=0.0
q=0.0
r2=0.0
r=0.0
    
for n in range(1,5):
    q=float(table.cell(17,n).value)
    p=float(table.cell(36,n).value)
    r=float(table.cell(58,n).value)
    
    print('110',n,'1月投資報酬率',(table.cell(17,n).value-table.cell(3,n).value)/table.cell(3,n).value)  
    
    print('110',n,'2月投資報酬率',(table.cell(36,n).value-table.cell(18,n).value)/table.cell(18,n).value)

    print('110',n,'3月投資報酬率',(table.cell(58,n).value-table.cell(37,n).value)/table.cell(37,n).value)
    print('110',n,'Q1投資報酬率',(r2+r+r-(q+p+r2))/(q+p+r2))#假設每個月買進1:1:1的股數，用現值扣每個月成本，再除以成本

    if cc2>=1 or cc3>=1 or cc4>=1:
        if c2>=1:
            print('不買的話','110',n,'Q1投資報酬率',(r2+r-(p+r2))/(p+r2))
        elif c3>=1:
            print('不買的話','110',n,'Q1投資報酬率',(r2+r-(q+r2))/(q+r2))
        elif c4>=1:
            print('不買的話','110',n,'Q1投資報酬率',(r+r-(q+p))/(q+p))
for n in range(5,7):
    q=float(table.cell(17,n).value)
   
    p=float(table.cell(36,n).value)
    r=float(table.cell(58,n).value)
    print('110',n+3,'1月投資報酬率',(table.cell(17,n).value-table.cell(3,n).value)/table.cell(3,n).value)  
    
    print('110',n+3,'2月投資報酬率',(table.cell(36,n).value-table.cell(18,n).value)/table.cell(18,n).value)

    print('110',n+3,'3月投資報酬率',(table.cell(58,n).value-table.cell(37,n).value)/table.cell(37,n).value)
    print('110',n+3,'Q1投資報酬率',(r2+r+r-(q+p+r2))/(q+p+r2))#假設每個月買進1:1:1的股數，用現值扣每個月成本，再除以成本
    
    if cc2>=1 or cc3>=1 or cc4>=1:
        if cc2>=1:
            print('不買的話','110',n+3,'Q1投資報酬率',(r2+r-(p+r2))/(p+r2))
        elif cc3>=1:
            print('不買的話','110',n+3,'Q1投資報酬率',(r2+r-(q+r2))/(q+r2))
        elif cc4>=1:
            print('不買的話','110',n+3,'Q1投資報酬率',(r+r-(q+p))/(q+p))
        
for n in range(7,8):
    q=float(table.cell(17,n).value)
    p=float(table.cell(36,n).value)
    r=float(table.cell(58,n).value)
    print('1110','1月投資報酬率',(table.cell(17,n).value-table.cell(3,n).value)/table.cell(3,n).value)  
    
    print('1110','2月投資報酬率',(table.cell(36,n).value-table.cell(18,n).value)/table.cell(18,n).value)

    print('1110','3月投資報酬率',(table.cell(58,n).value-table.cell(37,n).value)/table.cell(37,n).value)
    print('1110','Q1投資報酬率',(r2+r+r-(q+p+r2))/(q+p+r2))#假設每個月買進1:1:1的股數，用現值扣每個月成本，再除以成本
    if ccc2>=1 or ccc3>=1 or ccc4>=1:
        if cc2>=1:
            print('不買的話','1110',n+3,'Q1投資報酬率',(r2+r-(p+r2))/(p+r2))
        elif cc3>=1:
            print('不買的話','1110',n+3,'Q1投資報酬率',(r2+r-(q+r2))/(q+r2))
        elif cc4>=1:
            print('不買的話','1110',n+3,'Q1投資報酬率',(r+r-(q+p))/(q+p))

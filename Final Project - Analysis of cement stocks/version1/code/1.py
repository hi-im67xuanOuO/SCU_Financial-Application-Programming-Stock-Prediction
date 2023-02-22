import pandas_datareader.data as web
import pandas as pd 
import datetime 
import xlrd
import xlwt
list=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
start = datetime.datetime(2020,1,1)
end   = datetime.date.today()
df_stock=web.DataReader(['1101.TW','1102.TW','1103.TW','1104.TW',
                         '1108.TW','1109.TW','1110.TW'],'yahoo',start,end)
writer=pd.ExcelWriter('stock.xls')
df_stock.to_excel(writer,'Sheet1')
writer.save()
data=xlrd.open_workbook('stock.xls')
table=data.sheets()[0]
#1101

for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
        list1.append(table.cell(j,15).value-table.cell(i,22).value)#j是高
list1.sort(reverse=True)
for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list1[0]==(table.cell(j,15).value-table.cell(i,22).value):
           x1=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y1=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print('TW1101台泥',x1[0],'/',x1[1],'/',x1[2],'買',y1[0],'/',y1[1],'/',y1[2],'賣')
           print('每股獲利:','%f' %list1[0],'報酬率:','%f' %(list1[0]/table.cell(i,22).value))
           list.append(list1[0]/table.cell(i,22).value)
           a1=table.cell(i,22).value

#1102           
for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       list2.append(table.cell(j,16).value-table.cell(i,23).value)
list2.sort(reverse=True)
for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list2[0]==(table.cell(j,16).value-table.cell(i,23).value):
           x2=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y2=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1102亞泥",x2[0],'/',x2[1],'/',x2[2],'買',y2[0],'/',y2[1],'/',y2[2],'賣')
           print('每股獲利:','%f' %list2[0],'報酬率:','%f' %(list2[0]/table.cell(i,23).value))
           list.append(list2[0]/table.cell(i,23).value)
           a2=list2[0]/table.cell(i,23).value
#1103
for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       list3.append(table.cell(j,17).value-table.cell(i,24).value)
list3.sort(reverse=True)

for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list3[0]==(table.cell(j,17).value-table.cell(i,24).value):
           x3=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y3=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1103嘉泥",x3[0],'/',x3[1],'/',x3[2],'買',y3[0],'/',y3[1],'/',y3[2],'賣')
           print('每股獲利:','%f' %list3[0],'報酬率:','%f' %(list3[0]/table.cell(i,24).value))
           list.append(list3[0]/table.cell(i,24).value)
           a3=list3[0]/table.cell(i,24).value
           
for i in range(3,table.nrows-1):#1106
    for j in range(i+1,table.nrows):
       list4.append(table.cell(j,18).value-table.cell(i,25).value)
list4.sort(reverse=True)

for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list4[0]==(table.cell(j,18).value-table.cell(i,25).value):
           x4=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y4=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1104環泥",x4[0],'/',x4[1],'/',x4[2],'買',y4[0],'/',y4[1],'/',y4[2],'賣') 
           print('每股獲利:','%f' %list4[0],'報酬率:','%f' %(list4[0]/table.cell(i,25).value))
           list.append(list4[0]/table.cell(i,25).value)
           a4=list4[0]/table.cell(i,25).value
           
for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       list5.append(table.cell(j,19).value-table.cell(i,26).value)
list5.sort(reverse=True)

for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list5[0]==(table.cell(j,19).value-table.cell(i,26).value):
           x5=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y5=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1108幸福",x5[0],'/',x5[1],'/',x5[2],'買',y5[0],'/',y5[1],'/',y5[2],'賣')  
           print('每股獲利:','%f' %list5[0],'報酬率:','%f' %(list5[0]/table.cell(i,26).value))
           list.append(list5[0]/table.cell(i,26).value)
           a5=list5[0]/table.cell(i,26).value

for i in range(3,table.nrows-1):#1109.TW
    for j in range(i+1,table.nrows):#高t
       list6.append(table.cell(j,20).value-table.cell(i,27).value)
list6.sort(reverse=True)

for i in range(3,table.nrows-1):
    for j in range(i+1,table.nrows):
       if list6[0]==(table.cell(j,20).value-table.cell(i,27).value):
           x6=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y6=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1109信大",x6[0],'/',x6[1],'/',x6[2],'買',y6[0],'/',y6[1],'/',y6[2],'賣')  
           print('每股獲利:','%f' %list6[0],'報酬率:','%f' %(list6[0]/table.cell(i,27).value))
           list.append(list6[0]/table.cell(i,27).value)
           a6=list6[0]/table.cell(i,27).value

for i in range(3,table.nrows-1):#1110
    for j in range(i+1,table.nrows):
        list7.append(table.cell(j,21).value-table.cell(i,28).value)
list7.sort(reverse=True)

for i in range(3,table.nrows):
    for j in range(i+1,table.nrows-1):
       if list7[0]==(table.cell(j,21).value-table.cell(i,28).value):
           x7=xlrd.xldate_as_tuple(table.cell(i,0).value,0)
           y7=xlrd.xldate_as_tuple(table.cell(j,0).value,0)
           print("TW1110東泥",x7[0],'/',x7[1],'/',x7[2],'買',y7[0],'/',y7[1],'/',y7[2],'賣')  
           print('每股獲利:','%f' %list7[0],'報酬率:','%f' %(list7[0]/table.cell(i,28).value))                        
           list.append(list7[0]/table.cell(i,28).value)
           a7=list7[0]/table.cell(i,28).value
           
list.sort(reverse=True)
if a1==list[0]:
   print('在',x1[0],'/',x1[1],'/',x1[2],'買TW1101台泥',y1[0],'/',y1[1],'/',y1[2],'賣有最佳報酬率')
if a2==list[0]:
   print('在',x2[0],'/',x2[1],'/',x2[2],'買TW1102亞泥',y2[0],'/',y2[1],'/',y2[2],'賣有最佳報酬率')
if a3==list[0]:
    print("在",x3[0],'/',x3[1],'/',x3[2],'買TW1103嘉泥',y3[0],'/',y3[1],'/',y3[2],'賣有最佳報酬率')
if a4==list[0]:
    print("在",x4[0],'/',x4[1],'/',x4[2],'買TW1104環泥',y4[0],'/',y4[1],'/',y4[2],'賣有最佳報酬率')
if a5==list[0]:    
    print("在",x5[0],'/',x5[1],'/',x5[2],'買TW1108幸福',y5[0],'/',y5[1],'/',y5[2],'賣有最佳報酬率') 
if a6==list[0]:    
    print("在",x6[0],'/',x6[1],'/',x6[2],'買TW1109信大',y6[0],'/',y6[1],'/',y6[2],'賣有最佳報酬率')
if a7==list[0]:
    print("在",x7[0],'/',x7[1],'/',x7[2],'買TW1110東泥',y7[0],'/',y7[1],'/',y7[2],'賣有最佳報酬率')
print('報酬率為','%f' %list[0])



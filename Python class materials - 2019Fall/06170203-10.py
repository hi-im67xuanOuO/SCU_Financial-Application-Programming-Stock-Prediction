import datetime
import time

m = int(input('month:'))
d = int(input('day:'))
wd = int(input('weekday:'))

#第三個整數1為星期一、整數2為星期二、整數3為星期三、整數4為星期四、整數5為星期五、整數6為星期六或整數7為星期日
#從今年1月1日起至輸入的月份日期(皆含當天)，第三個整數的週數共有多少週。

d1 = datetime.date(2019,1,1) #今年1月1日
d2 = datetime.date(2019,m,d) #今年指定月日
delta = d2-d1
days = delta.days #兩者相距天數
print(days) 

d1_weekday=d1.isoweekday()
d2_weekday=d2.isoweekday()
#print(d1_weekday) #2 #星期二是2
#print(d2_weekday) #2 #星期二是2

count=0
count=days/7

if d2_weekday>=wd:
    count+=1
elif d2_weekday<=wd:
    if d1_weekday==wd:
        count+=1
print (int(count))


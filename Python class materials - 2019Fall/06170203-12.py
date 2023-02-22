import datetime
import time
a1 = input('輸入起始年月日：(yyyy-mm-dd)')
t1 = time.strptime(a1,"%Y-%m-%d")
y1,m1,d1 = t1[0:3]
a2 = input('輸入終止年月日：(yyyy-mm-dd)')
t2 = time.strptime(a2,"%Y-%m-%d")
y2,m2,d2 = t2[0:3]
wd = int(input('weekday:'))
#第三個整數1為星期一、整數2為星期二、整數3為星期三、整數4為星期四、整數5為星期五、整數6為星期六或整數7為星期日
#從今年1月1日起至輸入的月份日期(皆含當天)，第三個整數的週數共有多少週。
d1 = datetime.date(y1,m1,d1) #起始日
d2 = datetime.date(y2,m2,d2) #終止日
delta = d2-d1
#print(delta) #16 days, 0:00:00
days = delta.days+1 #兩者相距天數
d1_weekday=d1.isoweekday()
d2_weekday=d2.isoweekday()
#print(d1_weekday) #2 #星期二是2
more = 0
if d1_weekday<=7:
    more += 7-d1_weekday+1
if d2_weekday<7:
    more += d2_weekday
#print(more) #8
other = days-more
#print(other) #7
count=0
count=other/7
if d1_weekday<=wd:
    count+=1
if d2_weekday>=wd:
    count+=1
print (int(count))
#2019/1/1 2019/12/31 53

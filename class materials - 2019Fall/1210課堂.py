import datetime
import time
now = datetime.datetime.now()
now_str = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
print(datetime.date.today()) #2019-12-10
print(now.weekday()) #1 #星期二是1
print(now_str) #15:46:36

print(datetime.date(2019,2,15)) #2019-02-15

d1 = datetime.date(1869,1,2) 
d2 = datetime.date(1869,10,2)
print(d1.isoweekday()) #6
delta = d2-d1
print(delta) #273 days, 0:00:00

d3 = datetime.date(2019,12,10)
d4 = datetime.date(2019,12,11)
delta2 = d4-d3
print(delta2) #1 day, 0:00:00
print(d3.isoweekday()) #2 #星期二是2
print(delta2.days)

import calendar
c = calendar.TextCalendar(calendar.SUNDAY) #指定從星期幾開始印
str = c.formatmonth(2025,1) #要印幾年幾月
print(str)

#公告成績的期中考全班平均成績
import csv
total1 = 0
total2 = 0
average = 0
with open("1.csv") as f:
    reader = csv.reader(f)
    next(reader)#skip header
    data = []
    for row in reader:
        data.append(row)

count = len(data)
for i in range(len(data)):
    total1=total1+int(data[i][0])
    total2=total2+int(data[i][1])
average = ((total1*0.5)+(total2*0.5))/count
print(average)

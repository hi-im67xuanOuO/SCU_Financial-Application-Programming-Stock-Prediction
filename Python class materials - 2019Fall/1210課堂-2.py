import csv
total1 = 0
total2 = 0
with open("stock2.csv") as f:
    reader = csv.reader(f)
    next(reader)#skip header
    data = []
    for row in reader:
        data.append(row)
print(data)
print("\n",data[0][1],data[0][2])
print(len(data))
for i in range(len(data)):
    total1=total1+int(data[i][1])
    total2=total2+int(data[i][2])
print(total1)
print(total2)

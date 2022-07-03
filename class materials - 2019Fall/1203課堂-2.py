import csv
f = open('stock2.csv','r')
for row in csv.DictReader(f):
    print(row['成交金額'])
f.seek(0,0)
for row in csv.DictReader(f):
    print(row['漲跌點數'])
f.close()

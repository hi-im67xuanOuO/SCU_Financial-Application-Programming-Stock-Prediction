import csv
with open('2.csv','r') as csvfile:
    r = csv.reader(csvfile)
    for t in r:
        print(t[3])
    csvfile.seek(0,0) #讓程式碼回到檔案的一開始，不然for迴圈跑過去不會再從頭跑一次
    with open('3.csv','w') as outfile:
        w = csv.writer(outfile)
        for t in r:
            t[3]=t[3].replace('/','-')
            print(t[3])
            w.writerow(t)

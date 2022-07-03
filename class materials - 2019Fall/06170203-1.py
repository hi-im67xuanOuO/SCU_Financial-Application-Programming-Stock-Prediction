n = int(input('an integer')) #輸入一個小於10000的數
count = 0
for i in range(2,n,1):
    if i==n-1: #是質數
        n+=1       
while count<10:
    for i in range(2,n,1):
        if (n%i) == 0: #非質數
            n+=1
            break
        if i==n-1: #是質數
            print(n)
            n+=1
            count+=1

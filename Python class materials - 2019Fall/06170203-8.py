n = int(input('an integer(奇數)：')) #輸入一個小於10000的奇數
count = 0
ans=[]
big = n
small = n-2

while count<10:
     
    for i in range(2,big,1): #2到自己
        
        if (big%i) == 0: #只要有一次整除，非質數
            break
        if i==big-1: #直到除數等於自己，質數
            ans.append(big)
            count+=1
            break
    big+=1

    if small==2:
        ans.append(small)
        count+=1      
        
    for i in range(2,small,1): #2到自己
        
        if (small%i) == 0: #只要有一次整除，非質數
            break
        if i==small-1: #直到除數等於自己，質數
            ans.append(small)
            count+=1
            break
    small-=1

ans.sort()
print(ans)

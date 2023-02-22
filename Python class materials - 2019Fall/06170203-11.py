n = int(input('an integer(1000~10000)：')) #輸入一個1000~10000的奇數
count = 0
ans=[]
big = n
small = n-1
big_range = big+200
small_range = small-200
while big<=big_range:
    for i in range(2,big,1): #2到自己
        if (big%i) == 0: #只要有一次整除，非質數
            break
        if i==big-1: #直到除數等於自己，質數
            ans.append(big)
            break
    big+=1
while small>=small_range:
    if small==2:
        ans.append(small)
        count+=1      
    for i in range(2,small,1): #2到自己
        if (small%i) == 0: #只要有一次整除，非質數
            break
        if i==small-1: #直到除數等於自己，質數
            ans.append(small)
            break
    small-=1
ans.sort()
print(ans)

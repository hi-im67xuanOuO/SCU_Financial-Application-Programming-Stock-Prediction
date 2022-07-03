num1 = int(input('Enter your month:'))
num2 = int(input('輸入該月份最後一天為星期幾:'))
print('日\t一\t二\t三\t四\t五\t六')

day = 0 #每月天數
weekday = 0 #從星期幾開始
if (num1==1)or(num1==3)or(num1==5)or(num1==7)or(num1==8)or(num1==10)or(num1==12):
    weekday = num2-2
    day = 31
if (num1==4)or(num1==6)or(num1==9)or(num1==11):
    weekday = num2-1
    day = 30
if num1 == 2:
    weekday = num2
    day = 28

count = 0
k = 1
while k<weekday:
    print('\t',end='')
    k+=1
    count+=1
    if count%7 == 0:
        print("\n")
n = 1
while n<=day:
    print(n,'\t',end='')
    n+=1
    count+=1
    if count%7 == 0:
        print("\n")
    

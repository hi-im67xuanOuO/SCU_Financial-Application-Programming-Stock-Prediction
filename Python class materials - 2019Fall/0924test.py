#輸入年月日
print("Enter the year:")
year = int(input())
print("Enter the month:")
month = int(input())
print("Enter the day:")
day = int(input())
answer = 0

#判斷是否閏年
if year%100==0:
    if year%400==0:
        leap_year=True
    else:
        lear_year=False
else:
    if year%4==0:
        leap_year=True
    else:
        leap_year=False


#天數計算
if month==1:
    answer = day-1
elif month == 2:
    answer = 31+day-1
else:
    if leap_year:
        day2 = 29
        if month == 3:
            answer = 31+day2+day-1
        elif month == 4:
            ansewr = 31+day2+31+day-1
        elif month == 5:
            ansewr = 31+day2+31+30+day-1
        elif month == 6:
            ansewr = 31+day2+31+30+31+day-1
        elif month == 7:
            ansewr = 31+day2+31+30+31+30+day-1
        elif month == 8:
            ansewr = 31+day2+31+30+31+30+31+day-1
        elif month == 9:
            ansewr = 31+day2+31+30+31+30+31+31+day-1
        elif month ==10:
            ansewr = 31+day2+31+30+31+30+31+31+30+day-1
        elif month ==11:
            ansewr = 31+day2+31+30+31+30+31+31+30+31+day-1
        elif month ==12:
            ansewr = 31+day2+31+30+31+30+31+31+30+31+30+day-1
        
    else:
        day2 = 28
        if month == 3:
            answer = 31+day2+day-1
        elif month == 4:
            ansewr = 31+day2+31+day-1
        elif month == 5:
            ansewr = 31+day2+31+30+day-1
        elif month == 6:
            ansewr = 31+day2+31+30+31+day-1
        elif month == 7:
            ansewr = 31+day2+31+30+31+30+day-1
        elif month == 8:
            ansewr = 31+day2+31+30+31+30+31+day-1
        elif month == 9:
            ansewr = 31+day2+31+30+31+30+31+31+day-1
        elif month ==10:
            ansewr = 31+day2+31+30+31+30+31+31+30+day-1
        elif month ==11:
            ansewr = 31+day2+31+30+31+30+31+31+30+31+day-1
        elif month ==12:
            ansewr = 31+day2+31+30+31+30+31+31+30+31+30+day-1
print(answer)
        
    
    













    

print("Enter the year:")
year = int(input())
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
if leap_year:
    print("That is a leap year.February has 29 days.")
else:
    print("That is not a leap year.February has 28 days.")

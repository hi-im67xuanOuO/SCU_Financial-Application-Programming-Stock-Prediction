list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
num = int(input('Enter your number(<10000):'))
for i in list:
    if num%i == 0:
        print(i)
        

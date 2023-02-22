def add(x,y):
    """相加"""
    return x+y

def substract(x,y):
    """相減"""
    return x-y

def multiply(x,y):
    """相乘"""
    return x*y

def divide(x,y):
    """相除"""
    return x/y

#輸入
print("選擇運算:")
print("1、相加")
print("2、相減")
print("3、相乘")
print("4、相除")

choice = int(input("輸入選擇1/2/3/4:"))

num1 = int(input("輸入第一個數字："))
num2 = int(input("輸入第二個數字："))

if choice == 1:
    print(num1,"+",num2,"=",add(num1,num2))

if choice == 2:
    print(num1,"-",num2,"=",substract(num1,num2))
    
if choice == 3:
    print(num1,"*",num2,"=",multiply(num1,num2))
    
if choice == 4:
    print(num1,"/",num2,"=",divide(num1,num2))

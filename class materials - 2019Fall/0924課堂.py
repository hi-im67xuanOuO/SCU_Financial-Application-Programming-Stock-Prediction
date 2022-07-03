print(123.456,'.2f')
format(123.456,'.2f')
format(123.456,'.0f')

a = int(input("1st integer:"))
b = int(input("2nd integer:"))
if a>b:
    print("htr large one is",a)
    a = a+10
else:
    print("the large one is",b)
    b = b+10
print(a,b)



f = open('number.txt','r')
a = f.read()
print(a)
print(len(a))
f.close()

L1 = a.split() #分離後字串列
print('L1:',L1)
print('\n')

f = open('number.txt','r')
a = f.readlines()
print(a)
print(len(a))
f.close

print(a[0].split())
print(a[1].split())

L2=a[0].split()
print('L2:',L2)
print('\n')

L3 = a[0].split()
L3.extend(a[1].split())
print('L3:',L3)
print('\n')

L4 = a[0].split()+a[1].split()
print('L4:',L4)



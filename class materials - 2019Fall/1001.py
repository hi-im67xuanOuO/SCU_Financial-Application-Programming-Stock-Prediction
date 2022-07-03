for i in range(1,10,1):#從1到9 每次遞增1
    for j in range(1,10,1):
        print(format(i,'2d'),'*',format(j,'2d'),'=',format((i*j),'2d'))
    print()

sum = 0
for i in range(1,10,1):
    x = int(input('第%d個數：'%(i)))
    sum = sum+x
print('總和=%d'%(sum))

end=100
for val in range(2,end+1):
    for n in range(2,val):
        if (val%n)==0:
            break
        if n==val-1:
            print(val)


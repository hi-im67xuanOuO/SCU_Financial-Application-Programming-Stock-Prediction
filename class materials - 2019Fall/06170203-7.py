f = open('number.txt','r')
a = f.read()
f.close()
L=a.split()
for i in range(len(L)):
    L[i]=int(L[i])

L.sort()
answer = L[1]*L[-2]
print(answer)

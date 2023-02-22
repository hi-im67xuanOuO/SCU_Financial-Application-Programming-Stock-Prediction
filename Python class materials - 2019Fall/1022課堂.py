fin = open('philosophers.txt','r')
content = fin.read()
print(content)

print()

fin = open('philosophers.txt','r')
for line in fin:
    print(line,end='')
fin.close()

print('\n')

with open('philosophers.txt','r') as fin:
    for line in fin:
        print(line,end='')



p=int(input('an integer'))

for i in range(2,p,1):
    if (p % i) == 0:
        print(p,'not prime')
        break
    if i==p-1:
        print(p,'is prime')




for letter in 'abcdefgh':
    if letter=='e':
        break
    print('letter:',letter)

number = 10
while number>0:
    number = number-1
    if number ==5:
        break
    print('number:',number)
print("the end")





for letter in 'abcdefgh':
    if letter == 'e':
        continue
    print('letter:',letter)

number = 10
while number>0:
    number = number-1
    if number ==5:
        continue
    print('number:',number)
print("the end")

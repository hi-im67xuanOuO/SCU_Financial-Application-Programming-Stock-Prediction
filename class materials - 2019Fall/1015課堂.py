def compare(x,y):
    return x if x>y else y

m = int(input('1st integer'))
n = int(input('2nd integer'))
print('the largest number: %d'%compare(m,n))


n = int(input('an integer'))
sum = 1
for i in range(1,n+1):
    sum = sum*i
print(sum)

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)
    #return m if n==0 else gcd(n,m%n)

def lcm(m,n):
    return m*n//gcd(m,n)
m = int(input("輸入m:"))
n = int(input("輸入n:"))
print("Gcd:",gcd(m,n))
print("Lcm:",lcm(m,n))

import random
number = random.randint(1,100)
print('the number is:',number)


# This program displays a random number
# in the range of 1 through 10.
import random

def main():
    # Get a random number.
    number = random.randint(1, 100)
    # Display the number.
    print('The number is', number)

# Call the main function.
main()

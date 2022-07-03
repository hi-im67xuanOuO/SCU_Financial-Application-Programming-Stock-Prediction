up = 0
low = 0
Digits = 0
Spaces = 0
with open('text.txt','r') as fin:
    for line in fin.read():
        if line.isupper():
            up+=1
        if line.islower():
            low+=1
        if line.isdigit():
            Digits+=1
        if line.isspace():
            Spaces+=1
print("Uppercase letters:",up)
print("Lowercase letters:",low)
print("Digits:",Digits)
print("Spaces:",Spaces)

import random
answer = random.randint(1,100)
print("the answer is:",answer)

number = int(input("輸入您的答案："))
while answer != number:
    if answer>number:
        print("Too low, try again.")
        number = int(input("輸入您的答案："))

    if answer<number:
        print("Too high, try again.")
        number = int(input("輸入您的答案："))

print("The answer is right!.")

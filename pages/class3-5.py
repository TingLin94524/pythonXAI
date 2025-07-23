import random

target = random.randint(1, 100)

while True:
    guess = int(input("請輸入你的數字: "))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜中了!")
        break

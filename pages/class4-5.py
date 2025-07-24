import random


def roll_dice(num):
    list_value = []
    for i in range(num):
        x = random.randint(1, 6)
        list_value.append(x)
    return list_value


n = int(input())
outcome = roll_dice(n)
print(outcome)


n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

for num in outcome:
    if num == 1:
        n1 += 1
    elif num == 2:
        n2 += 1
    elif num == 3:
        n3 += 1
    elif num == 4:
        n4 += 1
    elif num == 5:
        n5 += 1
    elif num == 6:
        n6 += 1


print("1出現", n1, "次")
print("2出現", n2, "次")
print("3出現", n3, "次")
print("4出現", n4, "次")
print("5出現", n5, "次")
print("6出現", n6, "次")

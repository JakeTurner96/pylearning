import random


def randNum(i):
    ints = []
    count = 0
    while count < i:
        num = random.randint(100, 999)
        if num % 5 == 0:
            ints.append(num)
            count = count + 1
    return ints


print(randNum(3))
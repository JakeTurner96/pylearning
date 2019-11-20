import random


def randomIntArray(length):
    numbers = []
    i = 0
    while i < length:
        numbers.append(random.randint(1, 100))
        i = i + 1
    return numbers


list = randomIntArray(10)

print(list)
print("Max: " + str(max(list)))
print("Min: " + str(min(list)))

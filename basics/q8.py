import random


def randomIntArray(length):
    numbers = []
    i = 0
    while i < length:
        numbers.append(random.randint(1, 100))
        i += 1
    return numbers


listA = randomIntArray(5)
listB = randomIntArray(5)

print(listA)
print(listB)

i = 0
while i < len(listA):
    print("\n(" + str(listA[i]) + ", " + str(listB[i]) + ")")
    i += 1

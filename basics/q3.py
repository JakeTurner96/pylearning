import random


def randomIntArray(length):
    array = []
    i = 0
    while i < length:
        array.append(random.randint(1, 100))
        i += 1
    return array


list = randomIntArray(10)
divisors = []

print("\nYour randomly generated list is: " + str(list))

for i in list:
    if i % 5 == 0:
        divisors.append(i)

print("The divisors of 5 are: " + str(divisors))

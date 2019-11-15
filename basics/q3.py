import random

def randomIntArray(length):
    numbers = []
    i = 0
    while i < length:
        numbers.append(random.randint(1, 100))
        i = i + 1
    return numbers

list = randomIntArray(10)
divisors = []

print("\nYour randomly generated list is: " + str(list))

for i in list:
    if i%5 ==0:
        divisors.append(i)

print("The divisors of 5 are: " + str(divisors))

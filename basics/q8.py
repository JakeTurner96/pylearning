import random


# A function for generating an array of random ints in the rang 1 - 100
# The length of the list is n which is passed as a parameter
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
    print(f"\n({str(listA[i])}, {str(listB[i])})")
    i += 1

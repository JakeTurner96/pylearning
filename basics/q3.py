import random
# Given a list of integers, print only those that are divisible by 5


# A function for generating an array of random ints in the rang 1 - 100
# The length of the list is n which is passed as a parameter
def randomIntArray(length):
    arr = []
    i = 0
    while i < length:
        arr.append(random.randint(1, 100))
        i += 1
    return arr


array = randomIntArray(10)
divisors = []

print(f"\nYour randomly generated list is: {str(array)}")

for i in array:
    if i % 5 == 0:
        divisors.append(i)

print(f"The divisors of 5 are: {str(divisors)}")

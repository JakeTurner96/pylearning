import random
# Given a list of integers, print the maximum and minimum numbers from the list


# A function for generating an array of random ints in the rang 1 - 100
# The length of the list is n which is passed as a parameter
def randomIntArray(length):
    numbers = []
    i = 0
    while i < length:
        numbers.append(random.randint(1, 100))
        i = i + 1
    return numbers


list = randomIntArray(10)

print(list)
print(f"Max: {str(max(list))}")
print(f"Min: {str(min(list))}")


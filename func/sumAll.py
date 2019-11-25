# Function which given a list of integers, returns the sum of all numbers
def sumAll(list):
    total = 0

    for i in list:
        total = total + i
    return total


print(sumAll([1, 2, 3, 4, 5, 6]))

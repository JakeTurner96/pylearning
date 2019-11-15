userInput = input("Please input a string\n\n")

dict = {}

for i in userInput:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i, j in dict.items():
    print(i + " = " + str(j))

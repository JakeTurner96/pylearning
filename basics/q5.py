# Given an input string, count the occurrences of all characters and print the result

userInput = input("Please input a string\n\n")
lettersDict = {}

for i in userInput:
    if i not in lettersDict:
        lettersDict[i] = 1
    else:
        lettersDict[i] += 1

for i, j in lettersDict.items():
    print(f"{i} = {str(j)}")

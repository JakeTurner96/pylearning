import re


def getCharCount(string):
    splitString = re.split(":", string)
    return int(splitString[1])


def getMinString(array):
    j = 0
    minString = ""
    while j < len(array):
        if j == 0:
            minString = array[0]
        elif getCharCount(array[j]) < getCharCount(minString):
            minString = array[j]
        j = j + 1
    return minString


file = open("wordcount.txt")
strings = []

for i in file:
    strings.append(i)

print(getMinString(strings))

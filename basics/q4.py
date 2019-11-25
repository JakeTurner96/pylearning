import re
# Given an input string, rearrange it such that lowercase letters come first

userInput = input("\nPlease input a string\n\n")
allUpper = re.findall(r"[A-Z]", userInput)
ans = re.sub("[A-Z]", "", userInput)

for i in allUpper:
    ans = ans + i

print(ans)

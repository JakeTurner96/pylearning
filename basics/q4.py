import re

userInput = input("\nPlease input a string\n\n")
allUpper = re.findall(r"[A-Z]", userInput)
ans = re.sub("[A-Z]", "", userInput)

for i in allUpper:
    ans = ans + i

print(ans)

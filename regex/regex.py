import re


def checkUppercasePattern():
    pattern = '^[A-Z]{1}[a-z]+'
    userInput = input("\n\nPlease enter a string\n")
    if re.fullmatch(pattern, userInput):
        print("True")
    else:
        print("False")


def checkPattern(pattern):
    userInput = input("\n\nPlease enter a string\n")
    if re.search(pattern, userInput):
        print("True")
    else:
        print("False")


lengthPattern = "^.{3,8}$"
numberPattern = '\d'
urlPattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
specialCharPattern = "[@_!#£$%^&*()<>?/\|}{~:]"
end = False

while not end:
    menuDecision = input("\nPlease select a number from the menu:\n\n" +
                         "1. Contains number\n2. Contains uppercase\n3. Contains special character\n4. Validate "
                         "URL\n5. Check length\n6. Exit\n\n")

    if menuDecision == "1":
        checkPattern(numberPattern)
    elif menuDecision == "2":
        checkUppercasePattern()
    elif menuDecision == "3":
        checkPattern(specialCharPattern)
    elif menuDecision == "4":
        checkPattern(urlPattern)
    elif menuDecision == "5":
        checkPattern(lengthPattern)
    elif menuDecision == "6":
        end = True
    else:
        print("Invalid Input")

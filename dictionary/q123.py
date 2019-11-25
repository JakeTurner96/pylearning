import datetime
import re
import calendar


def getMonth(key):
    if key in myDictionary:
        split = re.split("/", myDictionary[key])
        return int(split[1])


def getBdByName():
    userInput = input("Please input a name\n")

    if userInput in myDictionary:
        print(myDictionary[userInput])
    else:
        print("Record does not exist\n")


def getCurrentMonthBdName():
    print(f"\nPeople with a birthday in {calendar.month_name[month]}:\n")
    found = False
    for i in myDictionary:
        if getMonth(i) == month:
            found = True
            print(i)
    if found:
        userInput = input("\nEnter a name to get birthday\n")
        if userInput in myDictionary:
            print(myDictionary[userInput])
        else:
            print("\nInvalid input")
    else:
        print("None")


myDictionary = {
    "Jake": "16/08/1996",
    "Hannah": "11/09/1995",
    "John": "23/04/1984",
    "Bill": "02/12/1970",
    "Tina": "17/02/1977",
    "Mark": "17/11/2000"
}

date = datetime.datetime.now()
month = date.month
end = False

while not end:
    menuDecision = input("\nPlease select a number from the menu:\n\n" +
                         "1. Get birthday by name\n2. Get current month birthday names\n3. Exit\n\n")

    if menuDecision == "1":
        getBdByName()
    elif menuDecision == "2":
        getCurrentMonthBdName()
    elif menuDecision == "3":
        end = True
    else:
        print("Invalid decision")
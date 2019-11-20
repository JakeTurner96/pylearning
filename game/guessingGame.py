import random

guessed = False
randomInt = random.randint(1, 9)

userInput = input("\nI'm thinking of a number between 1 and 9, can you guess what it is?\n\n")

while not guessed:

    if int(userInput) == randomInt:
        guessed = True
        print("\nCorrect!\n")
    elif int(userInput) < randomInt:
        userInput = input("\nToo low, try again.\n\n")
    elif int(userInput) > randomInt:
        userInput = input("\nToo high, try again.\n\n")

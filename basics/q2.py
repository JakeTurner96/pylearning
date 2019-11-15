userInput = input("\nPlease enter a whole number\n\n")
reverse = userInput[::-1]

if reverse == userInput:
    print("\nTrue " + userInput + " is a palindrome")
else:
    print("\nFalse " + userInput + " is NOT a palindrome")

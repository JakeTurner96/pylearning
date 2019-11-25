# Given an input string, determine if the string is a palindrome
userInput = input("\nPlease enter a whole number\n\n")
reverse = userInput[::-1]

if reverse == userInput:
    print(f"\nTrue {userInput} is a palindrome")
else:
    print(f"\nFalse {userInput} is NOT a palindrome")

# Given an input string, display all chars at an even index
userInput = input("\nPlease enter a string\n\n")
newString = userInput[::2]

print(f"\nThe characters at an even index are: {newString}")

userInput = input("Please enter a string\n\n")
userFile = open("wordcount.txt", "a")
length = str(len(userInput))

userFile.write(f"{userInput}:{length}\n")
userFile.close()

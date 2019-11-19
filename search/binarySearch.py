def binarySearch(arr, l, h, target):

    if h >= l:
        mid = int(l+(h-l)/2)

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            return binarySearch(arr, l, mid-1, target)
        else:
            return binarySearch(arr, mid+1, h, target)
    else:
        return False


array = [4,8,12,16,20,24,28]

print("\nThe list of numbers is " + str(array))

userInput = input("Enter a number to search for \n\n")
print(binarySearch(array, 0, len(array)-1, int(userInput)))
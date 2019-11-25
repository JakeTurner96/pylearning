# Given two lists of integers, return a new list containing the intersection of both lists

listA = [1, 4, 7, 2, 9, 8]
listB = [5, 8, 3, 6, 9, 2, 4, 7]

ans = []

for i in listA:
    if i in listB:
        ans.append(i)
print(f"\nList A = {str(listA)}")
print(f"\nList B = {str(listB)}")
print(f"\nThe intersection of A and B = {str(ans)}")

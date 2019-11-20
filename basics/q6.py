listA = [1, 4, 7, 2, 9, 8]
listB = [5, 8, 3, 6, 9, 2, 4, 7]

ans = []

for i in listA:
    if i in listB:
        ans.append(i)
print("\nList A = " + str(listA))
print("\nList B = " + str(listB))
print("\nThe intersection of A and B = " + str(ans))

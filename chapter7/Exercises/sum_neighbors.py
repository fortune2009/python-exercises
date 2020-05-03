# If neighbors exists in a list then this code sum them up

# listA = [10,20,30,40,50] #Used to test code

put = int(input("Enter Numbers or type -1 to end: \n"))

# Variable initialization of two lists (A to hold input, B to hold sum of data-set).
listA = []
listB = []

# A sentinel was used here to allow Nth input from user
while put != -1:
    if put == -1:
        listA.pop()
        break
    else:
        listA.append(put)
        put = int(input(""))
print("All inputs are = ", listA)  # List shows input from user
print()

# I saved the length of the list
lastIndex = listA.__len__()
for i, e in enumerate(listA):  # This iteration used its index
    if i < (i + 1) < (i + 2):
        if listA[i] == listA[(lastIndex - 1)]:
            listing = listA[(i - 1)] + listA[i]
            listB.append(listing)
        elif i == 0:
            listing = listA[i] + listA[(1 + i)]
            listB.append(listing)
        else:
            listing = listA[(i - 1)] + listA[i] + listA[((i * 2) - (i - 1))]
            # print(listA[(i - 1)], " ", listA[i], " ", listA[((i * 2) - (i - 1))])
            listB.append(listing)

print("Neighbor Sum = ", listB)  # Print for the neighbor sum list

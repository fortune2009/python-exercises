#There are three ways to make a list
#let the element output "1"

mylist = []

#First of the three ways
for i in range(25):
    mylist.append(1)
print("First Way", mylist)
print()

#Second way
myval = 25
i = 0
myList = []
while i < myval:
    myList.append(i)
    my_comp = [(j - j) + 1 for j in myList]
    i += 1
print("Second Way", my_comp)

#Third
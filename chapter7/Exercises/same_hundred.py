myList = []

for numbers in range(100):
    myList.append(numbers)

for index, value in enumerate(myList):
    print('myList[{}] = {}'.format(index, value))


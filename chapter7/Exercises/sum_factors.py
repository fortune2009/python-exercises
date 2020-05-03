number = int(input("Enter a number to get it factors: "))

# factor = [(number*(number-(i-1))if i>4 else number*(number-(i+1))or i) if i>3 else i for i in range(1, number)]
numList = []

for element in range(number):
    element += 1
    if number % element == 0:
        numList.append(element)

print("Factors of {} are {} ".format(number, numList))

factor = [sum(numList) if number else 0 for i in numList]

print("Total = ", factor[-1])

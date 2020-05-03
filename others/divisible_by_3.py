#write an algorithm that determines whether a number is between 2 and 20 and
# is divisible by 3.

count = 2 #here i start counter with first number

while count <= 20 :
    if count % 3 == 0:
        print(count, end=' ')
    count = count + 1
print()    
print("total count= ",count * count)

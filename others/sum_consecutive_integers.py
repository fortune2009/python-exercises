# Write a program that prompts for an integer—let’s call it
#X—and then ﬁnds the sum of X consecutive integers starting at 1.

prompt = int(input("Enter an integer: "))
adder = 1
add = 1
suma = 0
sume = 0
suma2 = 0

#while adder <= prompt:
 #   suma = suma + adder 
  #  print(adder, end=' + ')
   # adder += 1
#print('0=', suma)


rex = ''

while adder <= prompt:
    rex = str(1)
    print(rex, end=' + ')
    while add <= adder:
        rex == rex
        suma = suma + add
        if add > 1:            
            print(int(rex)+1, end='')
        if add > 2:
            print(' +',int(rex)+2, end='')
        if add > 3:
            print(' +',int(rex)+3, end='')
        if add > 4:
            print(' +',int(rex)+4, end='')
        if add < 2:
            print(int(rex)-1, end='')
        print(' =', suma, end='\t\n')  
        add += 1
    adder += 1


def celsius_to_fahrenheit(param_float):
	return param_float*1.8+32.0


def d2f(c):
    if type(c) != int:
        return - 1
    return param_float*1.8+32.0


def c2f(c):
    if type(c) != int:
        print('invalid type')
    return
    return param_float*1.8+32.0


def charge_amount():
    amt = int(input('How much do you want to charge: '))
    if amt == 5 or amt == 10:
        return amt
    elif amt == 25:
        return amt + 3
    elif amt == 50:
        return amt + 8
    elif amt == 100:
        return amt + 20
    else:
        print('invalid Amount!')


s = 'ABC'

for x in s:
    for y in s:
        for z in s:
            if x != y and x != z and y != z:                
                print("{}{}{}".format(x,y,z,), end=',')
                #print(x,y,z, end=',')


def sq(num):
	print(num**2)

	
number = 2
sq(number)

def sq(num):
        num = 3
        print(num**2)

	
number = 2
sq(number)

def sq(num):
        print(num**2)
        num = 5
        print(num**2)

	
number = 2
sq(number)


li = [8,3,45,56,4]
li[0] = 7
li
li[:3] = [5,2,4]
li = [6,8] + [8,43,26,10]

li = [print, len]
s = 'jiloo'
li[1](s)


""" immutable methods of strings """

li = 'abu jide'
li = list(li)
li


'''print('{:>10s} is {:<10d} years old'.format('Bill', 24))


print('{:>10s} is {:>10d} years old'.format('Bill', 24))


print('{:>2s} is {:<10d} years old'.format('Bill', 24))



for c in enumerate('hello'):
    print(c)
print()    

for a, b in enumerate('hello'):
    print(a, b)
print()

col = input("ENTER 12 LETTERS: ")

for a, b in enumerate(col):
    a += 1
    if a%3==0:        
        print(b)
    a += 1    


river = 'Mississippi'
target = input('Input a character to find: ')

for index, letter in enumerate(river):
    if letter == target:
        print('Letter found at index', index)
        break
else:
    print('Letter', target, 'not found in',river) 


name = 'John Marwood Cleese'
name.split()

name.split('o')

name = input("Type str: ")

new_name = ''
for c in name:
    if c != "'" and c != ' ':
        new_name += c
# this proves the palidrome in boolean
new_name = new_name.lower()    
print(new_name == new_name[::-1])
print(new_name)
        

x = -2
b = 3
print('{0:0=+10d}{1:.>+10d}'.format(x, b))

print('{0:0=+10d}{1:0=+10d}'.format(x, b))'''

name = input("Enter Palindrome: ")

new_name= ''
for c in name:     
    new_name = c + new_name
print('name = {}, new_name = {}, is_palindrome = {}'.format(name, new_name, new_name == new_name))
print()
print('name = %s, new_name = %s, is_palindrome = %r'%(name, new_name, new_name == new_name))

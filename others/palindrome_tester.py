#palindrome tester
import string
import turtle
original_str = input('input a string: ')
modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation

for char in modified_str:
    if char in bad_chars:
        modified_str = modified_str.replace(char,'')

if modified_str == modified_str[::-1]:
    print(\
        'the original string is : {}\n\
         the modified string is : {}\n\
         the reversal is: {}\n\
         String is a palindrome'.format(original_str, modified_str, modified_str[::-1]))

else:
    print(\
        'the original string is: {}\n\
         the modified string is: {}\n\
         the reversal is: {}\n\
         String is not a palindrome'.format(original_str,modified_str,modified_str[::-1]))




turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)

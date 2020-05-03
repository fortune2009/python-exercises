#checking the user input for errors
# put some exception handling

txt = input('Please enter a number: ')

if txt.isdigit():
    print('Your input was Digits')
else:
    print('Kindly input Digits')


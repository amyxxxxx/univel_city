pass_word = input("Please enter a password: ")

if pass_word.find('a')
    print("Please enter a valid password")
if [a-z] not in pass_word:
    print("Please enter a valid password")
elif [A-Z] not in pass_word:
    print("Please enter a valid password")
elif [0-9] not in pass_word:
    print("Please enter a valid password")
# elif [$ # or @] not in pass_word:
#     print("Please enter a valid password")
elif len(pass_word) < 6:
    print("Please enter a valid password")
elif len(pass_word) > 16:
    print("Please enter a valid password")
else:
    print(pass_word)

import re
pass_word = input('Please enter your password: ')
x = True

while x:
    if (len(pass_word)<6 or len(pass_word)>16):
        break
    elif not re.search('[a-z]', pass_word):
        print('Password must contain a letter from (a-z)')
        break
    elif not re.search('[0-9]', pass_word):
        print('Password must contain a figure fro [0-9]')
        break
    elif not re.search('[A-Z]', pass_word):
        print('Password muust contain a letter from [A-Z]')
        break
    elif not re.search('[$#@]', pass_word):
        print('Password must contain a special character from [$#@]')
        break
    elif not re.search("\s", pass_word):
        break
    else:
        print('Valid Password is ', pass_word)
        x = False
        break
if x:
    print('The Password is not Valid')

side1 = input('Please enter the first length of the triangle : ')
side2 = input('Please enter the second length of the triangle: ')
side3 = input('Please enter the third length of the triangle: ')

if side1 == side2 == side3:
    print('This is an equilateral triangle')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('This is an isosceles triangle')
else:
    print('This is a scalene triangle')

Original list of dictionaries: [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

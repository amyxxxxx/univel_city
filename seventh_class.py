# for i in range(5):
#     print(i+1)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []

# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

# b = [i for i in a if i%2==0]
# print(b)

# a = [(0, 'Sheldon'), (1, 'Penny')]

# for e in a:
#     print(e)

# for e in a:
#     print(e[0])

# names = ['Sheldon', 'Penny', 'Howard', 'Leonard', 'Rajesh']
# for index, item in enumerate(names):
#     print(index,item)

# a = [0, 1, 2]
# b = [2, 4, 6]
# c = []

# for i in a:
#     for x in b:
#         c.append(i+x)
# print(c)

# a = ["Hello", "World"]
# b = ["World", "Baby"]

# for i in a:
#     for x in b:
#         c.append(i[0]+x[1])
# print(c)

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()

# for x,y in zip(list1, list2):
#     print(x, y)

# import time

# print('It\'s time for registration')
# Name = input('Please enter your name: ')
# Email = input('Please enter your email address: ')
# Password = input('Please enter a password: ')


# isValid = True
# special_char = ['$', '#', '@']

# if:
# if len(Password) < 8:
#     print('Password is too short')
#     isValid = False
# if not any(char.isdigit() for char in Password):
#     print('Password must contain a number from [0-9]')
#     isValid = False
# if not any(char.islower() for char in Password):
#     print('Password must contain a letter from [a-z]') 
#     isValid = False
# if not any(char.isupper() for char in Password):
#     print('Password must contain a letter from [A-Z]')
#     isValid = False
# if not any(char in special_char for char in Password):
#     print('Passsword must contain a special character from [$#@]')
#     isValid = False
# if isValid:
#     print('Password created\nYour password is ', Password)
# else:
#     print('Invalid password')

# time.sleep(3)

# print('If you have registered, please login with your details')

# E_mail = input('Please enter your email address: ')

# if Email == E_mail:
#     print('Email address registered\nPlease continue...')
# else:
#     print('Email address not registered')

# Pass_word = input('Please enter your password: ')

# if Password == Pass_word:
#     print('Password correct\nLogin successful')
# else:
#     print('Password incorrect')


# user_data = {}

# activity = input('Login or Sign up?\n')





x = 10
while x > 0:
    print(x)
    x-=1

# x = True
# while True:
#     print('I am a boy')
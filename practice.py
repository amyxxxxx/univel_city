# import time
# user_data = {}

# for i in range(10000):
#     activity = input("Login or Sign up?\n>>").lower()

#     if activity == 'login':
#         email    = input("Enter your email\n>>")
#         password = input("Enter your password\n>>")

#         time.sleep(2)
#         if email in user_data.keys():
#             actual_password = user_data.get(email)

#             if actual_password == password:

#                 print('Login successful')
#                 break
#             else:
#                 print("Please enter a valid email and password.")
#         else:
#             print("There is no active user with thie email")

#     elif activity == 'sign up':

#         for i in range(10000):
#             email = input("Enter your email\n>>")
#             password = input("Enter your password\n>>")
#             re_password = input("Confirm password \n>>")
#             special_char = ['#', '@', '$']
#             isValid = True

#             if password != re_password:
#                 print("Please enter matching passwords")
#                 continue
#             if (len(password) < 6) or (len(password) > 16):
#                 print ("Password length should not be less than 6")
#                 isValid = False
#             elif not any(char.isdigit() for char in password):
#                 print("Password should at least contain a number")
#                 isValid = False 
#             elif not any(char.islower() for char in password):
#                 print("Password should contain at least a lowercase letter [a-z]")
#                 isValid = False
#             elif not any(char.isupper() for char in password):
#                 print("Password should contain at least an uppercase letter [A-Z]")
#                 isValid = False
#             elif not any(char in special_char for char in password):
#                 print("Password should contain at least a special character [@#$]")
#                 isValid = False
#                 continue
#             else:
#                 user_data[email] = password
#                 break
#         con = input("Press 'y' to continue and any other key to quit\n>>")
#         if con == 'y':
#             continue
#         else:
#             break
#     else:
#         print("Please select a valid option")



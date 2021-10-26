import ast
import time

from bankapp3 import read_file_data

userdata = {}

running = True

while running:
    activity = input('WELCOME!!!\nWhat will you like to do?\nSign up or Login\n').lower()

    if activity == 'sign up':
        print('Please enter your details below')
        name = input('Please enter your name\n')
        phone_num = input('Please enter your phone number\n')

        isValid = True

        if len(phone_num) != 11:
            print('Phone number must have 11 digits')
            isValid = False
        elif not(char.isdigit() for char in phone_num):
            print('Invalid format')
            isValid = False
        elif not(char.startswith(0) for char in phone_num):
            print('Your phone number must begin with a 0')
            isValid = False
        else:
            isValid = True

        email = input('Please enter your email address\n').lower()
        specialchar = '@'

        isValid = True
        if not any(char in specialchar for char in email):
            print('Invalid format')
        else:
            isValid = True

        password = input('Please enter your password\n')
        re_password = input('Please confirm your password\n')

        special_char = ['#', '@', '$']
        isValid = True

        if password != re_password:
            print("Please enter matching passwords")
            continue
        if (len(password) < 6) or (len(password) > 16):
            print ("Password length should not be less than 6")
            isValid = False
        elif not any(char.isdigit() for char in password):
            print("Password should at least contain a number")
            isValid = False 
        elif not any(char.islower() for char in password):
            print("Password should contain at least a lowercase letter [a-z]")
            isValid = False
        elif not any(char.isupper() for char in password):
            print("Password should contain at least an uppercase letter [A-Z]")
            isValid = False
        elif not any(char in special_char for char in password):
            print("Password should contain at least a special character [@#$]")
            isValid = False
        else:
            data = [('name', name), ('number', phone_num), ('email', email), ('password', password)]
            userdata[email] = {}
            userdata[email].update(data)
            print(userdata)
            userdata[email] = password

            progress = input("Enter p to do something else and any key to logout.\n>>").lower()
            if progress == 'p':
                continue
            else:
                break

    elif activity == 'login':
        email = input('Please enter your email\n').lower()
        password = input('Please enter your password\n')

        time.sleep(1)
        if email in userdata.keys():
            pass_word = userdata.get(email)

            if pass_word == password:

                log_in = True
                while log_in:
                    log_activity = input(f"""Welcome {name}, you have successfully logged into your account.
What will you like to do?
    v to view your profile
    e to edit your profile
    c to change your password
    r to reset your password
    n to create a note
    _n to edit your note
    .n to clear note
Press any other key to log out\n""").lower()
                    if log_activity == 'v':
                        print(f'Welcome to your profile page {name}.title()\nNAME:{name}\nPHONE NUMBER:{phone_num}\nEMAIL ADDRESS:{email}\nPASSWORD:{password}')
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break                  
                    elif log_activity == 'e':
                        edited = input(f"""What will you like to do?
    1 to change name
    2 to change phone number
    3 to change email address
    4 to change password
""")
                        if edited == '1':
                            changed_name = input('Please enter new name\n')
                            userdata[email][name] = changed_name
                        elif edited == '2':
                            changed_num = input('Please enter new number\n')
                            userdata[email][phone_num] = changed_num
                        elif edited == '3':
                            changed_email = input('Please enter new email address\n')
                            userdata[email][email] = changed_email
                        elif edited == '4':
                            changed_pass = input('Please enter new password\n')
                            userdata[email][password] = changed_pass
                        else:
                            print('Please enter a valid option') 
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                    elif log_activity == 'c':
                        former_pass = input('Please input your old password\n')
                        if former_pass == password:
                            new_pass = input('Please input your new password\n')
                            re_new_pass = input('Please confirm your new password\n')
                            userdata[email][password] = new_pass
                        else:
                            print('Incorrect password') 
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break                           
                    elif log_activity == 'r':
                        repassword = input('Enter a new password\n')
                        repassword1 = input('Confirm your new password\n')
                        if repassword == repassword1:
                            userdata[email][password] = repassword
                            print(f'Your password has been changed successfully\nYour new password is {repassword}')
                        else:
                            print('Please enter matching passwords')
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                    elif log_activity == 'n':
                        file_name = input('Please enter your filename\n')
                        new_file = open(f"{file_name}.txt", mode = "x")
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break                        
                    # elif log_activity == '_n':
                        note = f'filepath.txt'
                        text = input('Please enter your note body\n')
                        with open(note, 'w') as note_file:
                            note_file.write(text)
                            print('Note successfully saved')
                        # new_file.write()

                        user_note = read_file_data(username)
                        if user_note == False:
                            print('You currently have no notes. Please add')
                        print(user_note)

                        edit = input('Enter e to edit your note or c to clear. Press any other key to continue\n'):
                            if edit == 'e':
                                print('Note that editing this note overwrites the original content. Copy your contents to a safe place before proceeding')

                    else:
                        break
            else:
                print('Password doesn\'t match')
        else:
            print('This email hasn\'t been registered')
    else:
        print('Please enter a valid option')

                      
        
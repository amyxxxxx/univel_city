import time
import random
userdata = {}
setup = True
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Account_no = str(random.randrange(13579,86420))

Account_balance = []

print('Welcome to Bank of Univelcity')

while setup:
    options = input('What will you like to do?\n>>Create account\n>>Login\n>>Withdraw money\n>>Deposit money\n>>Transfer money\n').lower()
    
    if options == 'create account':
        while setup:
            print('Please follow the instructions below')
            Name = input('Please enter your fullname: ')
            Age = int(input('Please enter your age: '))
            Email = input('Please enter your email: ')
            Passcode = input('Please enter a passcode: ')
            Re_passcode = input('Re-enter your passcode: ')        

            isValid = True

            if Passcode != Re_passcode:
                print('Please enter matching passcodes')
                isValid = False
            if len(Passcode) != 4:
                print('Passcode must have 4 digits')
                isValid = False
            elif not(char.isdigit() for char in Passcode):
                print('Passcode must be made up of digits')
                isValid = False
            elif Age < 18:
                print('Must be at least 18 years old to create an account')
            else:
                userdata[Account_no] = Passcode
                print(f"Passcode created\nYour passcode is {Passcode}\nYour account number is {Account_no}")
                break
        print(userdata)

    elif options == 'login':
        print('Please input your account number and passcode')
        Account_no = input('Account number: ')
        Passcode = input('Passcode: ')

        time.sleep(2)
        if Account_no in userdata.keys():
            PIN = userdata.get(Account_no)

            if PIN == Passcode:
                print('Login successful\nWelcome')
                continue

                if options == 'deposit money':
                    print('Enter your account number and PIN below')
                    Account_no = input('Account number: ')
                    PIN = input('PIN: ')

                time.sleep(2)
                if Account_no in userdata.keys():
                    PIN = userdata.get(Account_no)

                if PIN == Passcode:
                    print(f"Your account balance is {Account_balance}")    
                    Depo = input('How much do you want to deposit?\n')                   
                
                else:
                    print('Account number and PIN doesn\'t match')
            else:
                print('This user does not exist')
        
        if options == 'withdraw money':
            print(f"You have {Account_balance} in your account")
            Withdrawal = input('How much do you want to withdraw?\n') 
            # amount = 


        if options == 'transfer money':
            Trans = input('Enter the recepient\'s account number:\nHow much will you like to transfer? ')
            Details = input('Please enter your account number and PIN\nAccount number:\nPIN:')

            if Details in userdata.items():
                print('Transaction successful')        
            else:
                print('Account number and PIN doesn\'t match')
        else:
            print('This user does not exist')

        
        # if options == 'deposit money':
        #     print('Enter your account number and PIN below')
        #     Account_no = input('Account number: ')
        #     PIN = input('PIN: ')

        #     time.sleep(2)
        #     if Account_no in userdata.keys():
        #         PIN = userdata.get(Account_no)

        #         if PIN == Passcode:
        #             print(f"Your account balance is {Account_balance}")    
        #             Depo = input('How much do you want to deposit?\n')


                    
                
        #         else:
        #             print('Account number and PIN doesn\'t match')
        #     else:
        #         print('This user does not exist')
        
        # if options == 'withdraw money':
        #     print(f"You have {Account_balance} in your account")
        #     Withdrawal = input('How much do you want to withdraw?\n') 
        #     # amount = 


        # if options == 'transfer money':
        #     Trans = input('Enter the recepient\'s account number:\nHow much will you like to transfer? ')
        #     Details = input('Please enter your account number and PIN\nAccount number:\nPIN:')

        #     if Details in userdata.items():
        #         print('Transaction successful')
            # if 

            # else:

    

            
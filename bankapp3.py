import random
import time
import ast

def write_to_file(type, data):
    if type == 'customer':
        file = ''
    elif type == 'transaction':
        file = ''

    with open(file, 'w') as doc_file:
        doc_file.write(f'{data}')

def read_file_data():
    trans_file = ''
    customer_file = ''

    with open(customer_file, 'r') as customer:
        cus_data = customer.read()
        customer_data = ast.literal_eval(cus_data)
    with open(trans_file, 'r') as transaction:
        trans_data = transaction.read

user_data = {}
# banking_info = {}
transaction_record = {}
keep_running = True

# def save_banking_info(account_num, pin):
#     """This function takes details from a user and updates the banking file."""

#     newfile = open("bank_info.txt", mode = "a")
#     newfile.write({'Account number': account_num})
#     newfile.write({'PIN': pin})
#     banking_info[transaction_record].append(user_data)
#     return banking_info
    

# def use_banking_info(account_num, pin):
#     """This function takes details from the banking file and allows user to make use of it."""

#     newfile = open("bank_info.txt", mode = "r")
#     newfile.read({'Account number': account_num})
#     newfile.read({'PIN': pin})
#     newfile.close()


def update_transaction_record(amount, trans_type, transaction, account_num):
    """This function takes in the amount and other transaction details. Then it updates the transaction dictionary. It doesn't return anything."""

    trans_data = {
        'amount':amount,
        'trans_type':trans_type,
        'transaction':transaction
        }

    transaction_record[account_num].append(trans_data)

def generate_acc_num():
    num = [str(i) for i in range(10)]
    acc = ['9']
    acc.extend([random.choice(num) for i in range(9)])
    account_num = "".join(acc)

    if account_num in user_data.keys():
        return generate_acc_num()

    return account_num

while keep_running:
    user_activity = input("Enter s to signup, l to login and anyother key to quit\n>>").lower()
   
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")


        isValid = True

        if len(pin) != 4:
            print('PIN must have 4 digits')
            isValid = False
        elif not(char.isdigit() for char in pin):
            print('PIN must be made up of digits')
            isValid = False
        else:            
            num = [str(i) for i in range(10)]
            acc = ['9']
            acc.extend([random.choice(num) for i in range(9)])
            account_num = "".join(acc)
            data = [('name', name), ('pin', pin), ('balance', 0)]
            user_data[account_num] = {}
            user_data[account_num].update(data)
            print(user_data)
            print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.")

        # banking_info[account_num] = []       
        # save_banking_info(account_num, pin)

        #create empty transaction record

        transaction_record[account_num] = []

        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break
    
    elif user_activity=='l':
        print("Enter login details below".title())
        account_num = input("Account num:\n>>")
        pin = input("Enter 4 digit pin:\n>>")

        account_details = user_data.get(account_num, False)
        if account_details and account_details.get('pin') == pin:            
            logged_in = True
            while logged_in:
                action = input(f"""Welcome, {account_details.get('name')}!
What would you like to do?
    w for withdrawal
    a for account statement
    b for balance
    d for deposit
    t for transfer
Press any other key to logout\n>>""").lower()
                if action == 'w':
                    amount = float(input("Enter amount to withdraw\n>>"))

                    if amount >= account_details.get('balance', 0):
                        time.sleep(2)
                        print("Insufficient funds")                   
    
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                    else:
                        account_details['balance'] -= amount
                        print('Please take your cash')

                        #save transaction detail
                        update_transaction_record(amount,"Debit", "Withdrawal", account_num)

                        trans_data = {
                            'amount':amount,
                            'trans_type':'Debit',
                            'transaction':'Withdrawal'
                        }

                        transaction_record[account_num].append(trans_data)
                    
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break

                elif action == 'd':
                    amount = float(input("Enter amount to deposit\n>>"))


                    account_details['balance']+=amount
                    print('Deposit complete')

                    #save transaction detail
                    update_transaction_record(amount,"Credit", "Deposit", account_num)

                    trans_data = {
                        'amount':amount,
                        'trans_type':'Credit',
                        'transaction':'Deposit'
                    }

                    transaction_record[account_num].append(trans_data)

                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break  

                elif action == 't':
                    amount = float(input("Enter amount to transfer\n>>"))
                    recepient_account = input("Enter destination account number\n>>")

                    recepient = user_data.get(recepient_account, False)
                    if recepient:
                        if amount >= account_details.get('balance', 0):
                            print("Insufficient funds. GERROUT!")
                            time.sleep(2)
                            print("Insufficiant funds")

                            progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                            if progress == 'p':
                                continue
                            else:
                                break
                        else:
                            account_details['balance']-=amount
                            #save transaction detail

                            trans_data = {
                                'amount':amount,
                                'trans_type':'Debit',
                                'transaction':'Transfer'
                            }

                            transaction_record[account_num].append(trans_data)
                            update_transaction_record(amount,"Debit", "Transfer", account_num)

                            recepient['balance']+=amount
                            #save transaction detail

                            beneficiary_trans_data = {
                                'amount':amount,
                                'trans_type':'Credit',
                                'transaction':'Transfer'
                            }

                            transaction_record[recepient_account].append(beneficiary_trans_data)
                            update_transaction_record(amount,"Credit", "Transfer", recepient_account)

                            print("Transfer successful. Gerrout!")
                            progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                            print('Please take your cash')

                            #save transaction detail

                            trans_data = {
                                'amount':amount,
                                'trans_type':'Debit',
                                'transaction':'Withdrawl'
                            }

                            transaction_record[account_num].append(trans_data)

                            progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                            if progress == 'p':
                                continue
                            else:
                                break
                    else:
                        print('No active customer for this account number. Gerrout!')

                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break                       
                
                elif action == 'b':
                    print(f"Your current balance is NGN{account_details['balance']}\n")

                elif action == 'a':
                    if len(transaction_record[account_num]) > 0:
                        last_5_transactions = transaction_record[account_num][-5:]
                        print("Here is your last 5 transactions")

                        for transaction in last_5_transactions:
                            print("Amount: ", transaction['amount'])
                            print("Transaction Type: ", transaction['trans_type'])
                            print("Transaction Ref.: ", transaction['transaction'])
                            print()
                    else:
                        print("You have not made any transactions. Please make a transaction.")

                else:
                    break    

        else:
            print("Please enter a valid account number and pin")

    else:
        print("Sorry to see you go.")
        break


print(user_data)
print(transaction_record)

with open('bank_info.txt') as bank_info:
    bank_info.write(f"{user_data}")

myfile = open('bank_info.txt', mode = 'a')
myfile.write(f"{user_data}")
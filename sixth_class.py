get_data = input("Enter data here: ")
print(get_data)

sports = {"swimming", "boxing", "cricket"}
sports_count = len(sports)
print(sports_count)

scores = [50, 60, 70, 80]
print(sum(scores))

my_adder = lambda x:x+100
print(my_adder(1))
my_math = lambda x,y,z:x**2+y+z
print(my_math(5,6,7))

li = [1, 2, 3, 4, 5]
print(list(map(lambda i:i**2,li)))

price_list = input("Enter the list of prices here:\n>").split(',')
prices = list(map(lambda string:int(string), price_list))
print(sum(prices))
print(sum(prices)/len(prices))

first_iterable = [2, 4, 6, 8]
second_iterable = ["a", "b", "c", "d"]
pre_output = zip(first_iterable, second_iterable)
output = list(pre_output)
print(output)

artists = ["Ed Sheeran", "Usher", "Oxlade"]
output = enumerate(artists)
print(list(output))

mylist = [2, 3, 5, 7, 8, 20, 4, 1, 9]
o = list(filter(lambda a:a%2!=0, mylist))
print(o)

num = [20, 31, 45, 60, 10, 77]
my_filter = filter(lambda x:x%2,num)
print(list(my_filter))

print(list(range(2)))
print(list(range(2,5)))
print(list(range(2,5,2)))

import time
import random

from datetime import datetime
# import pyotp

print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.sleep(3))

user = input("Enter your name:\n>")
print("Creating account, please wait...")
time.sleep(3)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print("Almost there...")
time.sleep(2)
print(f"Welcome {user}, your account has been created!")

my_list = [2, 3, 5, 3, 1, 4, 56, 3]
print(random.shuffle(my_list))
print(random.sample(my_list, 3))
print(my_list)

random.seed(2)
print(random.randrange(3, 10))

print(datetime.now())

date = datetime.now()
print(datetime.strftime(date, "%A, %d %B %Y"))

def random_nums(n):
    return [random.randrange(n) for i in range(n)]

print("Welcome to this game")
list_of_numbers = [96, 60, 55, 67, 65, 57, 82, 52, 16, 91, 60, 46, 70, 1, 6]
choice = int(input(f"Guess number from:\n{list_of_numbers}\n>>"))

random.shuffle(list_of_numbers)

com_choice = random.choice(list_of_numbers)

if choice == com_choice:
    print("You win")
else:
    print("E be like say you no win. Sorry")

def random_nums(n):
    return [random.randrange(n) for i in range(n)]

print("WELCOME!!!:\nGame time:\nLet's play rock, paper and scissors:)")

time.sleep(2)

player_name = input("Please enter your name: ").title()
print(f"COMPUTER VS {player_name}")
possible_choices = ["Rock", "Paper", "Scissors"]

time.sleep(1)

player_choice = input(f"Choose from:\n{possible_choices}:\n").title()

random.shuffle(possible_choices)
computer_choice = random.choice(possible_choices).title()
print(computer_choice)

time.sleep(3)

if player_choice == computer_choice:
    print("Rematch")
elif player_choice == "Rock" and computer_choice == "Paper":
    print("Better luck next time")
elif player_choice == "Paper" and computer_choice == "Rock":
    print("WINNER")
elif player_choice == "Paper" and computer_choice == "Scissors":
    print("Better luck next time")
elif player_choice == "Scissors" and computer_choice == "Paper":
    print("WINNER")
elif player_choice == "Scissors" and computer_choice == "Rock":
    print("Better luck next time")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print("WINNER")
else:
    print("Select a possible input")
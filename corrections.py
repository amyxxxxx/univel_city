students_in_A = set(input().split())
students_in_B = set(input().split())

list_of_intersected_students = students_in_A.intersection(students_in_B)

print(list_of_intersected_students)
print(len(list_of_intersected_students))

### ROCK PAPER SCISSORS 
import random

print("Welcome to the game")
print("Rock Paper Scissors")

help = """
This is a simple game that follows the rule below: 
Rock wins Scissors
Paper wins Rock
Scissors wins Paper
"""

print(help)

player_choice = input("What do you choose?\n").lower()
choices = ['r', 'p', 's']
random.shuffle(choices)
com_choices = random.choice(choices)

if player_choice in choices:
    if (player_choice == 'r' and com_choice == 's') or 
    (player_choice == 'p' and com_choice == 'r') or
     (player_choice == 's' and com_choice == 'p'):





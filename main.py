import random

print('Welcome to the game Rock, Paper, Scissors')

options = ['rock', 'paper', 'scissors']

# record scores
computer_score = 0
user_score = 0

user_choice = ''

# the game will continue until the user decide to quit
while user_choice != 'q':
    computer_choice = random.choice(options)
    user_choice = input('\nChoose Rock, Paper, or Scissors or Q to quit: ')
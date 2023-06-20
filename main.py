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

# game logic
    if user_choice == 'rock' and computer_choice == 'rock':
        print(f'Computer chose {computer_choice}. This round is a draw')
    elif user_choice == 'rock' and computer_choice == 'paper':
        print(f'Computer chose {computer_choice}. You loose this round')
        computer_score += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print(f'Computer chose {computer_choice}. You win this round')
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print(f'Computer chose {computer_choice}. You win this round')
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'paper':
        print(f'Computer chose {computer_choice}. This round is a draw')
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print(f'Computer chose {computer_choice}. You loose this round')
        computer_score += 1
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print(f'Computer chose {computer_choice}. You loose this round')
        computer_score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'Computer chose {computer_choice}. You win this round')
        user_score += 1
    elif user_choice == 'scissors' and computer_choice == 'scissors':
        print(f'Computer chose {computer_choice}. This round is a draw')

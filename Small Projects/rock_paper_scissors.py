from operator import truth
import random

user_wins = 0
computer_wins = 0

while True:
  user_input = input('Type Rock/Paper/Scissors or Q to quit this game: ')
  # user_input.lower()
  if user_input.lower() == "Q":
    break
  elif user_input != "rock":
    print('Please type again:')
    continue
  elif user_input != 'Paper':
    print('Please type again:')
    continue

  elif user_input != 'Scissors':
    print('Please type again:')
    continue

print('Goodbye! ')
from operator import truth
from optparse import Option
import random

user_wins = 0
computer_wins = 0

options = ['Rock', 'Paper','Scissors']

while True:
  user_input = input('Type Rock/Paper/Scissors or Q to quit this game: ').lower()
  # user_input.lower()
  if user_input == "q":
    break

  if user_input not in options :
    continue

  random_number = random.randint(0,2)
  computer_pick = options[random_number]
  print('Computer picked' , computer_pick + '.')

  if user_input == 'rock' and computer_pick == 'scissors':
    print('You won!')
    user_wins += 1
    continue

  if user_input == 'paper' and computer_pick == 'rock':
    print('You won!')
    user_wins += 1
    continue

  if user_input == 'scissors' and computer_pick == 'paper':
    print('You won!')
    user_wins += 1
    continue

  else:
      print('You lost!')
      computer_wins += 1

  # elif user_input != "rock":
  #   print('Please type again: ')
  #   continue

  # elif user_input != 'Paper':
  #   print('Please type again: ')
  #   continue

  # elif user_input != 'Scissors':
  #   print('Please type again: ')
  #   continue

print(f'You won {user_wins} times.')
print(f'Computer won {computer_wins} times.')
print('Goodbye! ')
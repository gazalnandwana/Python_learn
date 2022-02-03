import numbers
import random

print('This is the Dice Rolling game:')
user_input = 'y'

while user_input == 'y':
  number = random.randint(1,6)
  if number == 1:
    print(' ----------')
    print('|          |')
    print('|     *    |')
    print('|          |')
    print(' ----------')
  if number == 2:
    print(' ----------')
    print('|          |')
    print('|   *  *   |')
    print('|          |')
    print(' ----------')
  if number == 3:
    print(' ----------')
    print('|     *    |')
    print('|   *   *  |')
    print('|          |')
    print(' ----------')
  if number == 4:
    print(' ----------')
    print('|   *   *  |')
    print('|   *   *  |')
    print('|          |')
    print(' ----------')
  if number == 5:
    print(' ----------')
    print('|   *   *  |')
    print('|   *   *  |')
    print('|     *    |')
    print(' ----------')
  if number == 6:
    print(' ----------')
    print('|   *   *  |')
    print('|   *   *  |')
    print('|   *   *  |')
    print(' ----------')

  user_input = input('Press Y to continue this game: ')

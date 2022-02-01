# Ask user to enter a number to figure out whether it is a 'fizz', 'buzz' or 'fizzbuzz'.
# Keep on asking the user to enter the number to play this fizzbuzz game until he presses 0 to exit the game

number = 100
while number != 0:
    number = int(input('Enter a number:  \nOr press 0 to exit this game.'))
    if number % 3 == 0 and number % 5 == 0:
      print('fizzbuzz')

    elif number % 5 == 0:
      print('buzz')

    elif number % 3 == 0:
      print('fizz')

else:
  print('The number you entered is not divisible by 3 and 5.')

print('Thanks for playing this games.  Goodbye!!')
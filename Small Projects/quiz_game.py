from multiprocessing.connection import answer_challenge
from tkinter.messagebox import YES


print('Welcome to  my computer quize game.')

playing =input('Do you want to play this game? ')
print(playing)

score = 0

if playing.lower() != 'yes':
  quit()

print("Ok!! Let's play :) ")

answer = input('What does CPU stands for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')

answer = input('What does GPU stands for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')

answer = input('What does RAM stands for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')

answer = input('What does PSU stands for? ')
if answer.lower() == 'power supply':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')

print('You got ' + str(score) + ' question correct!')

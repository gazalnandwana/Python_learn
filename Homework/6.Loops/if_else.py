# Problem 1
  # Ask user to enter a nnumber through console
  # if the number is divisible by 3 print 'fizz'
  # if the number is divisible by 5 print 'buzz'
  # if the number is divisible by both 3 and 5 print 'fizzbuzz'

from tkinter import N


numbers = int(input('Enter a number: '))
n = numbers
# for number in range(numbers):
if numbers % 3 == 0 and numbers % 5 == 0:
    print('fizzbuzz')

elif numbers % 5 == 0:
    print('buzz')

elif numbers % 3 == 0:
    print('fizz')

else:
    print('This number is not multiple of 3 and 5')

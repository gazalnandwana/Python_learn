# Problem 1
  # Ask user to enter a nnumber through console
  # if the number is divisible by 3 print 'fizz'
  # if the number is divisible by 5 print 'buzz'
  # if the number is divisible by both 3 and 5 print 'fizzbuzz'

numbers = int(input('Enter multiple numbers: '))

# for number in numbers:
if numbers % 3 == 0 and numbers % 5 == 0:
  print('fizzbuzz')

elif numbers % 5 == 0:
  print('buzz')

elif numbers % 3 == 0:
  print('fizz')

else:
  print('Number is not divisible by 3 and 5')

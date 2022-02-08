import random

top_of_range = int(input('Please enter the number: '))

if top_of_range <= 0:
  print('Please type a number greater than "0" next time: ')

# else:
#   print('Please typle a number next time: ')
#   quit()


random_number = random.randint(0 , top_of_range)
print(random_number)
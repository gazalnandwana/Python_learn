def add(a, b):
  z = a + b

  return z

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
print(add(first_number, second_number))


def user_input(sequence):
  num = int(input(f'Enter the {sequence} number:\t'))

  return num


# print(add(
#   int(input(f'Enter the first number:\t')),
#   user_input('second'),
#   user_input('third'),
#   user_input('fourth'),
#   user_input('fifth')
# ))
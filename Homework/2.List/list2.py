# 2) Ask users to enter 2 numbers separately through console
#   a) store both numbers into 2 different variables
#   b) display the result of addition, substraction, multiplication and division of those numbers in a separate line

print('Enter 2 numbers separately through console: ')
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
add = first_number + second_number
sub = first_number - second_number
mul = first_number * second_number
div = first_number / second_number
print(f'The sum of numbers is: {add}')
print(f'The diffrence between numbers is: {sub}')
print(f'The multiplication of numbers is: {mul}')
print(f'The division of numbers is: {div}')

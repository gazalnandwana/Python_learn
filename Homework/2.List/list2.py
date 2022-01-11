# 2) Ask users to enter 2 numbers separately through console
#   a) store both numbers into 2 different variables
#   b) display the result of addition, substraction, multiplication and division of those numbers in a separate line

print('Enter 2 diffrent numbers: ')
first_num = int(input('Enter first number: '))
sec_num = int(input('Enter second number: '))
add = first_num + sec_num
sub = first_num - sec_num
mul = first_num * sec_num
div = first_num / sec_num

print(f'The sum of two numbers are : {add}')
print(f'Then diffrence between two numbers are: {sub}')
print(f'Multiplication of two numbers are: {mul}')
print(f'division of two numbers are: {div}')
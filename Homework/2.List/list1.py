# 1) Ask user to input multiple numbers where each number is separated by a comma (eg: 10, 20, 30, 40, 1213, 123)
#   a) figure out how many numbers did the user enter through the console
#   b) store them in a list
#   c) determine the type of first 3 numbers
#   d) if the entered number is a string, convert it into a number store it into the same list
#      eg: ['10', '20', '30'] => [10, 20, 30]

input_number = input('Enter multiple numbers: ')
user_input = input_number.split(',')
print(f'User Enterd: {user_input}')
print(f'User Entered {len(user_input)} numbers through the console: ')
user_input[0] = int(user_input[0])
user_input[1] = int(user_input[1])
user_input[2] = int(user_input[2])
print(user_input)
print(f'The type of the first number is: {type(user_input[0])}')
print(f'The type of the second number is: {type(user_input[1])}')
print(f'The type of the third number is: {type(user_input[2])}')
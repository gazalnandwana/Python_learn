# 1) Ask user to input multiple numbers where each number is separated by a comma (eg: 10, 20, 30, 40, 1213, 123)
#   a) figure out how many numbers did the user enter through the console
#   b) store them in a list
#   c) determine the type of first 3 numbers
#   d) if the entered number is a string, convert it into a number store it into the same list
#      eg: ['10', '20', '30'] => [10, 20, 30]

input_numbers = input('Enter the diffrent number: ')
user_list = input_numbers.split(',')
# list_number = (f'You can enter only 5 numbers: {input_numbers [0:4]}')
print('List:', user_list)
print(f'Type of numbers is: {type(input_numbers)}')
print(f'The user entered {len(user_list)} numbers through the console')
print(f'The first number\'s type is : {type(user_list[0])}')
print(f'The second number\'s type is : {type(user_list[1])}')
print(f'The third number\'s type is : {type(user_list[2])}')

user_list[0] = int(user_list[0])
user_list[1] = int(user_list[1])
user_list[2] = int(user_list[2])
print(user_list)
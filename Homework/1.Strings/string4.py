# 3) Ask user to input multiple floating point numbers where each number is separated by a semicolon (eg: 10.5;20.1;30.4;40;1213;123)
#   a) figure out how many numbers did the user enter through the console

numbers = input('Enter multiple floating numbers: ')
count = numbers.split(';')
print(f'User entered "{len(count)}" floating numbers')
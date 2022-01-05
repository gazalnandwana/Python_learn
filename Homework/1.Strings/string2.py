# 2) Enter any string, and perform the following operations
#   a) first 5 characters x= [0:5]
#   b) last 10 characters x = [-10:]
#   c) 3rd character to 10th character x= [2:9]
#   d) replace every space in the sentence with '@'

string = 'Hello how are you:'
print(f'First 5 character of the string are : {string[0:5]}')
print(f'Last 10 character of the string are: {string[-10:]} ')
print(f'3rd character to 10th character of the string: {string[2:9]}')
new_string = string.replace(' ' , '@')
print('Replacing the " " into "@" into the sentence: ', new_string)
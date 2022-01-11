# 3) Create a list containing 10 different names of people
#   a) Display the last 5 names from the list
#   b) Sort the list alphabetically

names = ['bob' , 'alex' , 'jhon' , 'linda' , 'kail' , 'zack' , 'king' , 'kim' , 'avi' , 'foster']
print(f'The last five names from the list are: {names[-5:]}')
names.sort()
print(f'Names in the list are alphabetically sorted: {names}')
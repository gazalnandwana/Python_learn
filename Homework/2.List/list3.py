# 3) Create a list containing 10 different names of people
#   a) Display the last 5 names from the list
#   b) Sort the list alphabetically

list_name = ['bob' , 'alex' , 'john' , 'rex' , 'ram' , 'steve' , 'martin' , 'luther' , 'king' , 'trump' ]
print(f'The last 5 names in list are: {list_name[-5:]}')
list_name.sort()
print(f'Names in this list are alphabetically sorted : {list_name}')

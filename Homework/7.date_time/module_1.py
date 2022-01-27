# # from module_2 import print_my_name
# import module_2

# name = 'Gajki'

# module_2.print_my_name(name)

# import datetime
# from datetime import datetime

# current_time = datetime.now()
# print(type(current_time))

# print(type(current_time.strftime('%D')))

# Ask user to enter date of birth in 3 different parts i.e. year, month and day,
# then construct a date time object. Then calculate the current age of the user,
# print the day of the week the user was born, also calculate the number of days from his dob

from datetime import datetime


user_bday = input('Enter your birth date : ')
year_of_birth = int(input('Enter year of birth: '))
bday = datetime.strptime(user_bday ,'%Y/%m/%d')

print(f'Day: {bday.day}')
print(f'Month: {bday.month}')
print(f'Year: {bday.year}')


current_age = datetime.now() - bday
print(bday.strftime('%A'))
print(f'Number of days from your born: {current_age}')
age = datetime.now().year - year_of_birth
print(f'You are {age} years old')

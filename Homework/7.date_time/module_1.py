# # from module_2 import print_my_name
# import module_2

# name = 'Gajki'

# module_2.print_my_name(name)

# import datetime
# from datetime import datetime

# current_time = datetime.now(5, 6, 2022)
# print(type(current_time))

# print(type(current_time.strftime('%D')))

# Ask user to enter date of birth in 3 different parts i.e. year, month and day,
# then construct a date time object. Then calculate the current age of the user,
# print the day of the week the user was born, also calculate the number of days from his dob

from datetime import datetime
from time import strptime

user_bday = input('Enter your birth date : ')
bday = datetime.strptime(user_bday ,'%m/%d/%Y')

print(f'Day: {bday.day}')
print(f'Month: {bday.month}')
print(f'Year: {bday.year}')

current_age = datetime.now() - bday
print(bday.strftime('%A'))
print(f'Number of days from your birth: {current_age}')
age = datetime.now().year - bday.year
print(f'You are {age} years old')


marriage_date = input('Enter your marriage date: ')
marriage_day = datetime.strptime(marriage_date , '%m/%d/%Y')

print(f'Day: {marriage_day.day}')
print(f'Month: {marriage_day.month}')
print(f'Year: {marriage_day.year}')

current_date = datetime.now() - marriage_day
print(f'Overall days: {current_date}')

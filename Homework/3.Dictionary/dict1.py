# 1) Create a database of 5 students (list of dictionaries) and store the following details
#   a) roll_number
#   b) first_name
#   c) last_name
#   d) date_of_birth
#   3) gender

dict_student1 = {'roll_number' : 1, 'first_name' : 'Alex', 'last_name' : 'Hamilton', 'date_of_birth' : '02/2/1992', 'Gender' : 'Male'}
dict_student2 = {'roll_number' : 2, 'first_name' : 'Bob', 'last_name' : 'Ab', 'date_of_birth' : '12/2/1993', 'Gender' : 'Male'}
dict_student3 = {'roll_number' : 3, 'first_name' : 'Ruby', 'last_name' : 'Hamilton', 'date_of_birth' : '7/5/1991', 'Gender' : 'Female'}
dict_student4 = {'roll_number' : 4, 'first_name' : 'John', 'last_name' : 'Wick', 'date_of_birth' : '02/22/1994', 'Gender' : 'Male'}
dict_student5 = {'roll_number' : 5, 'first_name' : 'Linda', 'last_name' : 'Thomas', 'date_of_birth' : '09/30/1992', 'Gender' : 'Female'}

table = list()
table.append(dict_student1)
table.append(dict_student2)
table.append(dict_student3)
table.append(dict_student4)
table.append(dict_student5)

print(table)
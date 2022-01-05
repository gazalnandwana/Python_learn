# 3) Ask users to enter the following:
#   a) first name
#   b) last name
#   c) email
#   d) date of birth
#   e) address
#    Print the output in the following manner:

#    Hello 'firstname' 'lastname',
#    Thank you for booking your Airbnb with us.
#    You email addrees has been registered as 'email' and your date of birth is 'dob'.
#    Your rental address is 'address'

#    Use string formating

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
email = input('Enter your Email address: ')
dob = input('Enter your date of birth: ')
address = input('Enter your address: ')

message = f'''Hello "{first_name}" "{last_name}",
Thank you for booking your Airbnb with us.
You email addrees has been registered as "{email}" and your date of birth is "{dob}".
Your rental address is "{address}"'''

print(message)
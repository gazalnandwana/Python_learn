# # name = 'Gazal'


# def say_hi():
#   global name
#   name = 'Pritam'
#   print(f'Hello everyone from {name}')


# def say_bye():
#   b = 'Gajki'
#   print(f'Bye everyone from {name}')

# # print(name)
# # say_bye()
# say_hi()
# print(name)

# def add(*nums):
#   print(nums)
#   print(type(nums))

#   for num in nums:
#     print(num)


# add([1, 2, 3, 4] , [3, 77, 86, 54], 'b', 'a', 'c')
# add((1, 2, 3, 4))

# add(1, 2, 3 ,4)


def add(a, b):
  print(f'a = {a}')
  print(a + b)


add(b=2, a=1)

def create_person(**person):
  print(person)
  print(type(person))


create_person(id=1, first_name='John', last_name='Doe', email='johndoe@gmail.com')
#  Problem 2
# Input = 'Gazal Krishnakumar Varsha Nandwana'
# output = 'gazalKrishnakumarVarshaNandwana'


# full_name = 'Gazal Krishnakumar Varsha Nandwana'
# full_name = 'Pritamkumar Narotamkumar BOHRA'
# name = full_name[:5].lower() + full_name[5:]
# print(name.replace(' ' ,''))


# camel case = camelCase   pritamkumarNarotamkumarBohra
# snake case = snake_case  pritamkumar_narotamkumar_bohra

# from unittest import result


full_name = 'Pritamkumar Narotamkumar BOHRA Gazal Krishnakumar Varsha Nandwana'
# names = full_name.split(' ')
# result = names[0].lower()
# for name in names[1:]:
#   result = result + name.title()
# print(result)

names = full_name.split(' ')
# result = names[0].lower()
# for name in names[1:]:
#   result = result + '_' + name.lower()

# print(result)
result = ''
for name in names:
  result = f'{result}_{name[0].lower()}{name[1:].upper()}'
  # result = result + '_' + name[0].lower() + name[1:].upper()

print(result)
#  Problem 2
# Input = 'Gazal Krishnakumar Varsha Nandwana'
# output = 'gazalKrishnakumarVarshaNandwana'

full_name = ('Gazal Krishnakumar Varsha Nandwana')
name = full_name[:5].lower() + full_name[5:]
print(name.replace(' ' ,''))
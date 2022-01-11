# name = [['abc', 'xyz', [10,20,30]], ['gaz', 'nand'], ['pri', 'boh', {'name': 'John'}]]
# print(name[2][2]['name'])

EmpInfo = [{'name': 'Bob', 'job': 'Mgr'}, {'name': 'Kim', 'job': 'Dev'}, {'name': 'Sam', 'job': 'Dev'}]
# print(EmpInfo[2]['name'])
#print(EmpInfo[1]['job'])

EmpInfo = {
  'emp1': {'name': 'Bob', 'job': 'Mgr'},
  'emp2': {'name': 'Kim', 'job': 'Dev'},
  'emp3': {'name': 'Sam', 'job': 'Dev'}
}
# print(EmpInfo['emp2']['job'])
# print(EmpInfo['emp3']['name'])

EmpInfo = {
  1: {'name': 'Bob', 'job': 'Mgr'},
  '2': {'name': 'Kim', 'job': 'Dev'},
  3: {'name': 'Sam', 'job': 'Dev'}
}
print(EmpInfo['2']['job'])
print(EmpInfo[3]['name'])
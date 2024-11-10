# You cannot have a duplicate key in a dictionary, it will overwrite the existing one
myDict = {1: 'Test', 'Name': 'Jim', 1: 'Not a test'}

print(type(myDict))

print(myDict[1])

myDict[2] = 'Test 2'

myDict[1] = 'Not a test!'

del myDict[1]

for x in myDict:
  print(x)
  
for key, value in myDict.items():
  print(str(key) + " : " + value)


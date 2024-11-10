with open('Module2/sample.txt', 'r') as file:
  print(file.read())
  
with open('Module2/sample.txt', 'r') as file:
  print(file.read(44))

with open('Module2/sample.txt', 'r') as file:
  print(file.readline())

with open('Module2/sample.txt', 'r') as file:
  data = file.readline()

  for x in data:
    print(x)
    
with open('Module2/sample.txt', 'r') as file:
  for x in file:
    print(x)
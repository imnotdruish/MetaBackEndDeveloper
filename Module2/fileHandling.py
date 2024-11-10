# Using Open
file = open('Module2/test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

# Using with open
with open('Module2/test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)
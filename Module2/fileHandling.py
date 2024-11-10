# Using Open
file = open('test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

# Using with open
with open('test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)
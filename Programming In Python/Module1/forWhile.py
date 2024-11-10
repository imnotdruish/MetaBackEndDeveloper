# Loops
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

# for loop
for item in favorites:
  print('I like this desert', item)

for idx, item in enumerate(favorites):
  print(idx, ':', item)

# while loop
count = 0

while count < len(favorites):
  print('I like this desert', favorites[count])
  count += 1;

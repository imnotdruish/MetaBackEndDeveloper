menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def findCoffee(coffee):
  if coffee[0] == 'c':
    return coffee

# Map takes all objects in a list and applies a function.
mapCoffee = map(findCoffee, menu)
print(mapCoffee)

for x in mapCoffee:
  print(x)

# Does the same as map, but take the results and creates a new list with only the true values.
filterCoffee = filter(findCoffee, menu)
print(filterCoffee)
for x in filterCoffee:
  print(x)

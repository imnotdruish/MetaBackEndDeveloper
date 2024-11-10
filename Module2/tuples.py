myTuple = (1, 'strings', 4.5, True)
print(myTuple[1])
print(type(myTuple))
print(myTuple.count('strings'))
print(myTuple.index(4.5))

for x in myTuple:
  print(x)

# Tuples are immutable, so this will raise an error
myTuple[0] = 5
      
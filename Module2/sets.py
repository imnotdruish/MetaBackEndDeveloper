# Sets do not allow duplicate values
setA = {1,2,3,4,5}
print(setA)

setA.add(6)
setA.remove(2)
setA.discard(3)

setB = {4,5,6,7,8}

print(setA.union(setB))
print(setA | setB)

print(setA.intersection(setB))
print(setA & setB)

print(setA.difference(setB))
print(setA - setB)

print(setA.symmetric_difference(setB))
print(setA ^ setB)

# Sets are not ordered and cannot be printed by index
print(setA[0])
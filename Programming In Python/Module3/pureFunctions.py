#global scope
# globalList = [1, 2, 3]

# NOT A PURE FUNCTION - Changes the global list
# def addTo(item):
#   return globalList.append(item)

# addTo(4)

# print(globalList)

# Pure Function - Does not change the global list
# def addToList(lst, item):
#   nl = lst.copy()
#   nl.append(item)
  
#   return nl


# Known Outcome
# Consistent and reliable
# Cache
# Multi-threaded programs

# Altering Functions

# Non-Pure Function
myList = [1, 2, 3]

def addToList(item):
  return myList.append(item)

addToList(4)

print(myList)
# Modified Function to make it pure

# Arguments is not the list variable
def addToList(lst, item):
  # Create a copy of the list to avoid altering the original list
  nl = lst.copy()
  # Appending to the copy of the list
  nl.append(item)
  # Returning the new list
  return nl
# Adding change to the new list
newList = addToList(myList, 4)

#Printing Original List
print(myList)
# Printing new list
print(newList)
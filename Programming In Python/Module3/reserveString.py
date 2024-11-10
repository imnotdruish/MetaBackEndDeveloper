# Reserving a String

# Slice Function str[start:stop:step]
trial = 'reversal'
newTrial = trial[::-1]
print(newTrial)

# Slice Function with Reversion
def stringReverse(str):
  if len(str) == 0:
    return str
  else:
    return stringReverse(str[1:]) + str[0]

str = "reversal"
reverse = stringReverse(str)
print(reverse)

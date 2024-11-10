# Looping Solution
def findFactorialByLooping(n):
  if n<0:
    return 0
  else:
    factorial = 1
    for i in range(1,n+1):
      factorial=factorial*i
    return factorial
  
print(findFactorialByLooping(5))

# Recursive Solution
def findFactorialRecursive(n):
  if n == 1:
    return 1
  else:
    return n * findFactorialRecursive(n - 1)
  
print(findFactorialRecursive(5))

# Advantages
  # Neat Code
  # Sub-problems
  # Easy Sequences
  
# Disadvantages
  # Hard to Follow
  # Memory are expensive and inefficient
  # Can be Difficult to Debug
  
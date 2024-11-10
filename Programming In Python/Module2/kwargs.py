# Arguments
def sumOf1(a, b):
  return a + b
def sumOf2(*args):
  sum = 0
  for x in args:
    sum += x
  return sum

print(sumOf1(4, 5))
print(sumOf2(4, 5, 6))

# Key word arguments
def sumOf3(**kwargs):
  sum = 0
  for k, v in kwargs:
    sum += v
  return round(sum, 2)

print(sumOf3(coffee=2.99, cake=4.55, juice=2.99))


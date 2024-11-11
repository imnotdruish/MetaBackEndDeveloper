# Single Inheritance
class A:
    pass
class B(A):
    pass
  
# Multiple Inheritance
# Example 1
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# Multi-level Inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

# Built-in Functions

# issubclass(class A, class B)

# print(issubclass(A,B))
# print(issubclass(B,A))

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)

class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
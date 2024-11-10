# SCOPES

# Global scope
myGlobal = 10;

def fn1():
  # Enclosed Scope
  enclosedV = 8
  def fn2():  
    #Local Scope
    localV = 5
    print('Access to Global', myGlobal) 
    print('Access to enclosed', enclosedV)
 
# Will not be able to access the variables
print(enclosedV)
print(localV)

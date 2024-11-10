# Functions
def calculateTax(bill, taxRate):
  return round((bill * taxRate) / 100.00)

print('Total Tax:', calculateTax(175.00, 15))
print('Total Tax:', calculateTax(164.33, 22))
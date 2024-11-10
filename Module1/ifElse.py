# Conditional Statements
# if else elif(else if)

billTotal = 210
discount1 = 10
discount2 = 20

if billTotal > 100 and billTotal < 200:
  print("Bill is greater than 100!")
  billTotal = billTotal - discount1
elif billTotal > 200:
  print("Bill is greater than 200!")
  billTotal = billTotal - discount2
else:
  print("Bill is less than 100!")
  
print("Total Bill: " + str(billTotal))

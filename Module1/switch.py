# Statement using if/else code
httpStatus = 200

if httpStatus == 200 or httpStatus == 201:
   print("Success!")
elif httpStatus == 400:
   print("Bad Request!")
elif httpStatus == 404:
   print("Not Found!")
elif httpStatus == 500 or httpStatus == 501:
   print("Server Error!")
else:
   print("Unknown!")
   
# Statement using match code
match httpStatus:
  case 200 | 201:
    print("Success!")
  case 400:
    print("Bad Request!")
  case 404:
    print("Not Found!")
  case 500 | 501:
    print("Server Error!")
  case _:
    print("Unknown!")

with open('Module2/newfile.txt', 'w') as file:
  file.write("This is a new file created!")

try:
  with open('Module2/newfile.txt', 'a') as file:
    file.writelines('This is another line to be added', '\nThis is a third line!')
except FileNotFoundError as e:
  print("ERROR", e)
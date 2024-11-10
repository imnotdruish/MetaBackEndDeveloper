import random

f = open("Module2/petnames.txt", "r")
fContent = f.read()
fContentList = fContent.split("\n")
f.close()
print(random.choice(fContentList))
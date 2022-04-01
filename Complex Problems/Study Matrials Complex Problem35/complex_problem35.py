import re

s = input("Enter a string")

x = re.search('^f(z*)$' ,s)

if x:
    print("Matching....")
else:
    print("Not Matching")
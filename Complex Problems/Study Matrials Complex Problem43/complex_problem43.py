import re

str = input("Enter a str")

# String end with number (0 to 5)
x = re.search('[0-5]+$', str)

if x:
    print("Matching....")
else:
    print("Not Matching")
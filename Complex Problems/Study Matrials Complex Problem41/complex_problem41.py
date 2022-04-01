import re

str = input("Enter a str")

# uppercase, lowercase, number and underscore
x = re.search('[A-Z]+[a-z]+[0-9]+[_]+', str)

if x:
    print("Matching....")
else:
    print("Not Matching")
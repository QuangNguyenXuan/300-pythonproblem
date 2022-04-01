import re
# a to f

s = input("Enter a char")
x = re.search('[a-f]', s)
if x:
    print("Matching...")
else:
    print("Not Matching...")

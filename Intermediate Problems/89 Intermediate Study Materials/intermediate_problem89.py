import re 
text = input("Enter a string")
x = re.search('^[0-9]+[a-zA-Z]*[0-9]+$', text)
if x:
    print("Valid, start and end with number")
else:
    print("Not valid")

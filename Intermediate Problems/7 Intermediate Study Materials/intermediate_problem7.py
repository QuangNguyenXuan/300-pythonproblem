import re
email = input("Enter a email ")

x = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)
if x:
    print("Email is valid")
else:
    print("Email is invalid")
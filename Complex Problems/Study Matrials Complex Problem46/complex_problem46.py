import re

pwd = input("Enter a Password")

# lowercase, uppercase, specail char, number,
x = re.search('^[a-z]+[A-Z]+[!@#$^%]+[0-9]+$', pwd)

if x:
    print("Password is Strong....")
else:
    print("Password is weak")
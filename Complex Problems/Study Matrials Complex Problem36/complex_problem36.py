import re

sent = input("Enter a sentence")
char = input("Enter a char or set of char")

x = re.search(char+'$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")
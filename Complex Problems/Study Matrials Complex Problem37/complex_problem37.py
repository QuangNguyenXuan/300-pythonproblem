import re

sent = input("Enter a sentence")

x = re.search('^[A-Z+[a-z]+$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")
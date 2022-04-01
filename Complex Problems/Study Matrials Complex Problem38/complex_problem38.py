import re

sent = input("Enter a sentence")

# ^ means at start 
# . means any char
# * 0 or many
# $ means at end 
x = re.search('^m.*0$', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")
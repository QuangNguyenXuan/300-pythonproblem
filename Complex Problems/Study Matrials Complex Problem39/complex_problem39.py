import re

sent = input("Enter a sentence")

# ^ means at start 
# . means any char
# * 0 or many
# $ means at end 
# \w means a to z, A to Z , 0 to 9 and _
x = re.search('^\w+', sent)

if x:
    print("Matching....")
else:
    print("Not Matching")
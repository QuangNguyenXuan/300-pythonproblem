import re

w = input("Enter a word")


x = re.search('m', w)

if x:
    print("Matching....")
else:
    print("Not Matching")
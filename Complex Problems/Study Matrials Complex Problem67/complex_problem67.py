import re

text = "adshfaskl32khskldkf88asdfk83ksdk8384kdfsjasd34983394348"
x = re.search("[0-9]{5}",text)
if x:
    print("Matching...")
else:
    print("Not Matching")
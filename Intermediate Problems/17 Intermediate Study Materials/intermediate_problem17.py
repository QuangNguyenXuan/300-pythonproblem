import re
word = input("Enter a word")
x = re.search('[a-z]+[A-Z]+', word) # faISAL
lst = []
if x:
    for i in word:
        if i.isupper():
            new_char = i.lower()
            lst.append(new_char)
        if i.islower():
            new_char = i.upper()
            lst.append(new_char)

else:
    print("NO")

print(lst)
converted_word = "".join(lst)
print(converted_word)
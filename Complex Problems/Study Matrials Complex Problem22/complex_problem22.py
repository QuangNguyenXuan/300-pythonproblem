s = input("Enter a string")
u = 0
l = 0

for i in s:
    if i.isupper():
        u += 1
    if i.islower():
        l += 1
print("Total numebr of uppercase = "+str(u))
print("Total numebr of Lowercase = "+str(l))
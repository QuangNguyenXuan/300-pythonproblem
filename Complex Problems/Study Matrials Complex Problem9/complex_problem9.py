lst = []

for i in range(5):
    lst.append(input("Enter a item"))

for i in lst:
    if i != lst[0] and i != lst[-1] and len(i) != 5:
        print(i)
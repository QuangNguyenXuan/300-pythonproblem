lst = []
for i in range(10):
    item = int(input("Enter element"))
    lst.append(item)

new_list = [i for i in lst if i%4 == 0 if i%5 == 0]
print(new_list)
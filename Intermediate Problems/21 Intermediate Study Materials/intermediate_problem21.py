lst = []
for i in range(5):
    item = int(input("Enter a item"))
    lst.append(item)
print(lst)

new_lst = [i*i*i for i in lst]
print(new_lst)
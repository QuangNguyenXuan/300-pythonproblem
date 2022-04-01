list = [1,2,3,4,20,21,24,4,5,8,9,10,18,19]
new_list = [i for i in list if i < 20 if i > 5]
print(new_list)

add = 0

for i in new_list:
    add += i
print(add)
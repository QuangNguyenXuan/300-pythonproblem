lst = [1,2,3,-4,5,-3,9,-8]
print(lst)
n = int(input("Enter a number"))
new_list = [n*i for i in lst]
print(new_list)
ne_list = [1,2,3,[2,2],["Jafri","Faisal"],[1.2,0.4]]

list_total = 0
for i in ne_list:
    if type(i) == list:
        list_total += 1
print(list_total)
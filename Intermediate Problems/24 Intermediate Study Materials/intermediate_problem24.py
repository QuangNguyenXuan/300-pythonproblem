d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
print(d)
for k,v in d.items():
    if k%2 != 0:
        print(v)
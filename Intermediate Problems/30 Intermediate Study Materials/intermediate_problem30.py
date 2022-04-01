d = {1:100,14:14000,2:2000,6:6000,9:9000}
print(d)

keys = []
for k in d.keys():
    keys.append(k)
print(keys)
addition = 0
for i in keys:
    addition += i
print(addition)

values = []
for v in d.values():
    values.append(v)
print(values)
product = 1
for i in values:
    product *= i
print(product)
import numpy as np
num = int(input("Enter a number")) # 6
ar = np.zeros(num, dtype=np.int64) # 6

for i in range(len(ar)):
    element = int(input("Enter array element"))
    ar[i] = element
print(ar)
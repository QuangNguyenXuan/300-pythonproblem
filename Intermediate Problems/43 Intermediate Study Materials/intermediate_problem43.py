import numpy as np
ar = np.array([1,2,3,4,5,6])
file = open("file.txt","w+")
file.write(str(ar))
file.close()

r_file = open("file.txt","r")
con = r_file.read()
print(con)
r_file.close()
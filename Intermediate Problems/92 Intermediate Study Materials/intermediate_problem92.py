from array import *
ar = array('i',[1,1,1,13,4,5,6,7])
print(ar)
n = int(input("Enter a number"))
result = ar.count(n)
print(str(result)+ " time "+str(n)+" existed")
myfile = open("mytable.txt","w")

num = int(input("Enter a number"))
product = 1
for i in range(1, 11):
    # 1 * 2 = 2 
    table  = str(i)+" * "+str(num)+" = "+str(i*num)
    myfile.write(str(table)+" \n")
    product *= i*num
print("Product = "+str(product))
myfile.write(str(product))
myfile.close()
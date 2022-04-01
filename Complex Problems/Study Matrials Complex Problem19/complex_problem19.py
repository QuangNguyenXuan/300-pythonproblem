file = input("Enter a file name") # my file
flag = "No"
for i in file:
    if i.isspace():
        flag = "Yes"

if flag == "Yes":
    print("File contain space")
else:
    print("File name is "+file+" there is no space")
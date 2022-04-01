file = open("input.txt","r")
r = file.readlines()
line = int(input("Enter a line number")) # 1
print(r[line-1]) 
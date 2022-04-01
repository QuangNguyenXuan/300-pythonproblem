lst = []
for i in range(10):
    s = input("Enter Student Name")
    lst.append(s)
print("Student List"+str(lst))
std_name = input("Enter Stduent name, you wnat to delete")
lst.remove(std_name)
print("Student List"+str(lst))


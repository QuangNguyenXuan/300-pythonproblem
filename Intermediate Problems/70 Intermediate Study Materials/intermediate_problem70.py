import csv
file = open("problem70.csv",'r')
read = csv.reader(file)
print(read)
for i in read:
    print(i)
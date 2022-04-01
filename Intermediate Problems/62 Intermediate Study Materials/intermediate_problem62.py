import xlwings
wb = xlwings.Book("xlwings.xlsx").sheets["Sheet1"]
data = wb.range("A2").value
print(data)
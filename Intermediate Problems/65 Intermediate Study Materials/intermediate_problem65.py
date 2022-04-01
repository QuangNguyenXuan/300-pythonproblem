import pandas as pd
col = [1,2,3]
e = pd.read_excel("xlswriter_wb2.xlsx", usecols=col)
print(e)

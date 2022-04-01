import pandas as pd
file = pd.read_excel("problem66.xlsx")
m = file["marks"].max()
mn = file["marks"].min()
print("Max = "+str(m))
print("Min = "+str(mn))

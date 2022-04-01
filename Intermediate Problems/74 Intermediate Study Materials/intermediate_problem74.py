import filecmp
import pandas as pd
file = pd.read_csv("problem74.csv")
file_col = file.columns
print(file_col)
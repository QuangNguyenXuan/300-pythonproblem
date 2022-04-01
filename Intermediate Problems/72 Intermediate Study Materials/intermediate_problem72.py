import pandas as pd
file = pd.read_csv("problem72.csv")
file.loc[3, "age"] = 30
file.loc[2, "name"] = "Faisal Jafri"
file.to_csv("problem72.csv")
print(file)
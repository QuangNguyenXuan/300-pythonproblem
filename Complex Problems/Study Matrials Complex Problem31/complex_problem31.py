import pandas as pd

s = pd.Series([1,2,3,4,5,6,61])
print(s)

n = 4
new_ps = s[s < n]
print(new_ps)
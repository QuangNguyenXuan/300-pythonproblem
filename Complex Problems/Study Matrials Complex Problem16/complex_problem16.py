import pandas as pd

ps = pd.Series([1,2,3,4,5,6])
print(ps)
ps_updated = ps.append(pd.Series([7,8,9]))
print(ps_updated)
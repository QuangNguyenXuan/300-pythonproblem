import pandas as pd
color_dict = {}
for i in range(3):
    code = input("Enter a color code")
    color = input("Enter a color value")
    color_dict[code] = color
print(color_dict)

ps = pd.Series(color_dict)
print(ps)
d = {"color1":"Red","color2":"Blue","color3":"Yellow","color4":"Black","color5":"Green"}
print(d)
a = 0
for i in d.keys():
    a  += len(i)

print(a)
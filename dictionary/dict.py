name = "jashwanth kumar v"
d = {}
for i in name:
    if i != " ":
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(d)
    
    
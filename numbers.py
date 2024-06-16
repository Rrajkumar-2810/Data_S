lst = [(0,1),(0,2),(1,2),(2,3)]
d={}
for i,j in lst:
    if i in d:
        d[i].append(j)
    else:
        d[i] = [j]
for i,j in lst:
    if j in d:
        d[j].append(i)
    else:
        d[i] = [j]
print(d)

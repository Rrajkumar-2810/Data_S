from collections import defaultdict
d = defaultdict(list)
for i in [45, 12, 5, 6, 5, 6]:
    x=i*i
    d[i].append(x)
print(d)

d1 = defaultdict(list)
for i in range(0, 5):
    x=i*i
    d1[i].append(x)
print(d1)

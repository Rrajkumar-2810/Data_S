def fun():
    yield 1
    yield 2
    yield 3
    return 0
print(fun())
for i in fun():
    print(i)

def fun1():
    yield 4
    yield 5
    yield 6
for j in fun1():
    print(j)

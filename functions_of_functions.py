def double(x):
    return 2*x
def apply_to_one(f):
    return f(1)
x= apply_to_one(double)
print(x)

double = lambda x: x*2
print(double(1))

y = apply_to_one(lambda x: x*2)
print(y)

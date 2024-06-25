lst = [23,12,45,78,56,37,6,23]
lsg = [14,45,23,89,46,34,7,48]

def mean(lst):
    return sum(lst)/len(lst)

def median(lst):
    lst.sort()
    if len(lst)%2==0:
        m= len(lst)//2
        return len(lst[m-1]+lst[m])
    else:
        return lst(len(lst)//2)
print("Median=",median(lst))

from collections import Counter
def mode(lst):
    c= Counter(lst)
    max_count= max(c.values())
    return [x for x, c in c.items() if c==max_count]
print("Mode=",mode(lst))


from collections import Counter
import math
   
def dot(v, w):
    assert len(v)==len(w)
    return sum(vi *wi for vi, wi in zip(v, w))

def sumofsquares(v):
    return dot(v,v)

def Variance(lst):
    xbar = sum(lst)/len(lst)
    lst1= [i-xbar for i in lst]
    return sumofsquares(lst1)/(len(lst)-1) #Using Function Call
print("Variance=",Variance(lst))


#from matplotlib import pyplot as plt
def de_mean(xs):
    x_bar = mean(xs)
    return [x-x_bar for x in xs]

def Covariance(lst,lsg):
    assert len(lst) == len(lsg)   
    return dot(de_mean(lst), de_mean(lsg))/ (len(lst)-1)
print("Covariance=",Covariance(lst, lsg))

#plt.plot([10,20,30,40,50],[2,4,6,8,11],markers='0')

def Standard_Deviation(lst):
    math.sqrt(Variance(lst))

def Correlation(x, y):
    stdev_x = Standard_Deviation(x)
    stdev_y = Standard_Deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return Covariance(x, y)/ (stdev_x*stdev_y)
    else:
        return 0
Cor = Correlation([10,20,30,40,50],[2,4,6,8,11])
print(Cor)

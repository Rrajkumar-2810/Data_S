# PDF of uniform Distribution
'''
from matplotlib import pyplot as plt
def Pdf_Uniform(x,a=0,b=1):
    if x>=a and x<=b:
        return 1/(b-a)
    else:
        return 0
print("PDF_Uniform=",Pdf_Uniform(0.6))

x=[-5,-4,-3,-2,-1,-.0009,0,1,1.0001,2,3,4,5]
y=[Pdf_Uniform(i) for i in x]
plt.plot(x,y)
plt.ylabel("Points")
plt.xlabel("Numbers")
plt.bar(x,y) '''

# CDF of Unifrom Distribution
'''
def cdf_uniform(x,a=0,b=1):
    if x<a:
        return 0
    if x>=a and x<=b:
        return (x-a)/(b-a)
    if x>b:
        return 1
print("CDF_Uniform=",cdf_uniform(0.5))
x=[-5,-4,-3,-2,-1,5,-.0009,0,1,1.0001,2,3,4,5,-5]
y=[cdf_uniform(i) for i in x]
plt.plot(x,y)
'''

# PDF of Normal Distribution
'''
import math
a=math.sqrt(2*math.pi)
e=2.718281828459045
def normal_distribution(x,mew=0,sigma=1):
#    return (1/(sigma*math.sqrt(2*math.pi)))*e*math.exp(-(x-mew)**2/(2*(sigma**2)))
    return (math.exp(-(x-mew)**2 / (2*sigma**2))/(a*sigma))
print("Normal Distribution PDF=",normal_distribution(5))

x=[-5,-4,-3,-2,-1,-.0009,0,1,1.0001,2,3,4,5,-5]
y=[normal_distribution(i) for i in x]
xs = [x for x in range(-50,50)]
plt.plot(x,y)
plt.plot(xs,[normal_distribution(x,sigma=3) for x in xs])
plt.plot(xs,[normal_distribution(x,mew=2,sigma=5) for x in xs])
plt.plot(xs,[normal_distribution(x,mew=0, sigma=1) for x in xs])
plt.plot(xs,[normal_distribution(x,mew=0, sigma=2) for x in xs])
plt.plot(xs,[normal_distribution(x,mew=0, sigma=0.5) for x in xs])
plt.plot(xs,[normal_distribution(x,mew=-1, sigma=1) for x in xs])
'''
# Pdf of Normal CDF
'''
from matplotlib import pyplot as plt
import math
def normal_CDF(x,mu=0,sigma=1):
    return (1+math.erf((x-mu)/(sigma*math.sqrt(2))))/2
print("Normal CDF=",normal_CDF(1,0,1))

xs = [x for x in range(-50,50)]
plt.plot(xs,[normal_CDF(x,mu=0,sigma=3) for x in xs])
plt.plot(xs,[normal_CDF(x,mu=5,sigma=4) for x in xs])
'''

#Binomial distribution

from matplotlib import pyplot as plt
import math
import random
def bernoulli_distribution(p):
    return 1 if random.random()<p else 0
def binomial_distribution(n,p):
    return sum(bernoulli_distribution(p) for x in range(n))
print("Bernoulli distribution=",bernoulli_distribution(0.8))
print("Binomial Distribution=",binomial_distribution(10, 0.5))
'''
xs = [x for x in range(-50,50)]
plt.plot(xs,[binomial_distribution(10, 0.5) for x in xs])
plt.bar(xs,[binomial_distribution(8, 0.8) for x in xs])
'''

#

from collections import Counter
y=[binomial_distribution(100,.5) for _ in range(10000)]
hist=Counter(y)
from matplotlib import pyplot as plt
plt.bar(hist.keys(),[i/10000 for i in hist.values()])

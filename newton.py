import math
import numpy as np
from sympy import *

def func(x):
    return pow(x,2)-2

def funcdiff(x):
    return 2*x

count = 0
x0 = 0
x1 = 0
e = pow(10,-7)

x0 = float(input('input x(0) : '))

while(abs(func(x0)) > e) :
    x1=x0-(func(x0)/funcdiff(x0))
    x0=x1
    count = count+1
    print(count , x0)
import math

def func(x):
    return pow(x,2)-2

a = float(input('input a : '))
b = float(input('input b : '))
e = pow(10,-7)
c = 0

count = 0
if (func(a)*func(b) < 0) :
    while(abs(func(c))) >= e:
        c = (a+b)/2
        if(func(a)*func(c) > 0):
            a = c
        else :
            b = c
        count = count+1
        print(count , c)

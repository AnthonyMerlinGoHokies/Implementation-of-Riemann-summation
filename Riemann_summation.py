#This will be code of an implementation of Riemann summation, Using a functions
#I also calculated the trapizoidal sum
#also I like math so why not :) 

import math 
def leftSum(f, dx, start, end):
    sum = 0 
    x = start
    while (x < end):
        sum += f(x)
        x = x + dx
    return sum*dx


def rightSum(f, dx, start, end):
    sum = 0 
    x = start 
    while (x < end):
        x = x + dx 
        sum += f(x)
    return sum*dx

def trapSum(f, dx, start, end):
    rs = rightSum(f,dx,start,end)
    ls = leftSum(f,dx,start,end)
    return (rs + ls)/2

def trapSumInLine(f, dx, start, end):
    sum = 0 
    x = start
    while(x < end):
        sum += f(x)
        x = x + dx 
        sum += f(x)
    return sum*dx/2

def midSum(f, dx, start, end):
    sum = 0 
    x = start + dx 
    while(x < end):
        sum += f(x)
        x = x + 2*dx 
    return sum*2*dx


ls = leftSum(math.sin, .1, 0, .6)
print("Left sum")
print(ls)

exact = -math.cos(0.6) - -math.cos(0)
print("Exact sum")
print(exact)

rs = rightSum(math.sin, .1, 0, .6)
print("Right sum")
print(rs)

print("Left Right average sum")
print((rs + ls)/2)

print("Trapezoidal Sum")
print(trapSum(math.sin, .1, 0, 0.6))

print("Stand alone trapezoidal sum")
print(trapSumInLine(math.sin, .1, 0, .6))


print("Midpoint Sum")
print(midSum(math.sin, .1, 0, 0.6))




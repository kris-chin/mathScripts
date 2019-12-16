#code written by Krischin Layon. SID: 862112168

from fractions import Fraction
from math import log,exp,cos,factorial
from sympy import *

#performs horners algorithm on a given polynomial
def solution1(polynomial, c):
    #polynomial = list of coefficients of the polynomial, in decreasing order of degree
    #c = compute the polynomial about x = c
    #for convenience, returns a 2-tuple of the new factored polynomial and the remainder term
    q = [] #list of coefficients for the factored polynomial
    for i in range(len(polynomial)): #horners algorithm
        if i == 0: q.append(polynomial[i])
        else: q.append( (q[i-1]*c) + polynomial[i])
    remainder = q.pop() #take out remainder

    #print solution
    print("f(x) = ( ",end="")
    for i in range(len(q)):
        print("(" + str(q[i]) + ")x^" + str(len(q)-1-i),end="")
        if i != len(q)-1: print(" + ",end="")
    print(" )(x-" + str(c) +") + (" + str(remainder) +")" )
    return (q,remainder)
    
#creates and plugs x into the taylor series of f(x) = ( e^(-x) - cosx)/(ln (x+1) ) to n terms.
def solution2(n,x,round_digits):
    #n = number of terms + 1
    #x = value to approximate
    #round_digits = number of digits to round to
    coefficients = [] #list of coefficients of taylor series. (length should be n)

    #we're gonna use sympy to compute the kth derivatives
    _x = symbols('x')
    f = ((exp((-_x)) - cos(_x))/log(_x+1)) #the actual function, we use x_sym since x is already the name of a paramater
    
    for k in range(n+1): #determine the coefficients
        dk = round(diff(f,_x,k).evalf(subs={_x:x}),round_digits) #compute the kth derivative
        print("f^" + str(k) + "(" + str(x) + "): " + str(dk))
        coefficients.append(round(round(dk,round_digits)/factorial(k),round_digits)) #add coefficient to coefficients list
    approx = 0 #appoximation value
    for k in range(n+1): #compute taylor series to nth term
        approx += round(coefficients[k]*(x**k),round_digits) #add the taylor terms.
        print("(" + str(coefficients[k]) + ")x^" + str(k) +"",end = "")
        if k != n: print(" + ",end="")
        else: print("\n")
    return approx

#SOLUTION 1:
print("Solution 1:")
print("Coefficients: " + str(solution1([1,-1,-3,-5,0,10],2)[0]))

#SOLUTION 2:
print("Solution 2:")
print("f(0.006) = " + str(solution2(10,0.006,10)))
import math
from decimal import *
from RootFinding import bisect, newton, secant

#-----------------------------------------------------------------------------------------------

def problem1(x): return ( Decimal(math.exp( (Decimal(math.sin(x)**3)) )) + (x**6) + (-2*(x**4)) - (x**3) - Decimal(1) )
def problem1_prime(x): return ( (3*Decimal(math.exp( (Decimal(math.sin(x)**3)) ))  *Decimal(math.cos(x))*(Decimal(math.sin(x)**2)) ) + (6*(x**5)) + (-8*(x**3)) + (-3*(x**2)) )

#part a)
print("1A")
interval = (Decimal(-2),Decimal(-1))
for i in range(50):
    #print("iteration " + str(i) + ": " + str(interval))
    interval = bisect(problem1,interval)
print("Computed Root: " + str((interval[0] + interval[1]) / 2))

interval = (Decimal(1),Decimal(2))
for i in range(50):
    #print("iteration " +str(i) + ": " + str(interval))
    interval = bisect(problem1,interval)
print("Computed Root: " + str((interval[0] + interval[1]) / 2))

#part b)
print("1B")

init = Decimal(-2)
for i in range(50):
    print("iteration " + str(i) + ": " + str(init))
    init = newton(problem1,problem1_prime,init)
print("Computed Root: " + str(init))

init = Decimal(1)
for i in range(50):
    print("iteration " + str(i) + ": " + str(init))
    init = newton(problem1,problem1_prime,init)
print("Computed Root: " + str(init))

init = Decimal(2)
for i in range(50):
    print("iteration " + str(i) + ": " + str(init))
    init = newton(problem1,problem1_prime,init)
print("Computed Root: " + str(init))
print("")

#-----------------------------------------------------------------------------------------------"

def problem2(x): return ( (x**3) - (2*Decimal(math.sin(x))) )
def problem2_prime(x): return ( (3*(x**2)) - (2*Decimal(math.cos(x))) )

#part a)
print("2A")
init = Decimal(0.5)
for i in range(10): # "print out the first 10 iterations"
    print("iteration " + str(i) + ": " + str(init))
    init = newton(problem2,problem2_prime,init)
    if init == 0: break

print("")

#part b)
print("2B")
init1 = Decimal(0.5)
init2 = Decimal(newton(problem2,problem2_prime,init1))
for i in range(10): # "print out the first 10 iterations"
    print("iteration " + str(i) + ": " + str(init1))
    temp = init2
    init2 = init1
    init1 = secant(problem2,init1,temp)
    if init1 == 0: break
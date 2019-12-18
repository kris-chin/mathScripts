def bisect(f,interval):
    #computes a single iteration of the bisection method
    #returns a tuple of the new resulting interval.
    #assumes a and b are opposite signs

    #f = function to plug in
    #interval = tuple of interval

    a = interval[0]
    b = interval[1]

    if f((a+b)/2) > 0: 
        if a < 0: return ( (a+b)/2, b) 
        elif a > 0: return (a, (a+b)/2 ) 

    if f((a+b)/2) < 0:
        if a < 0: return (a, (a+b)/2 ) 
        elif a > 0: return ( (a+b)/2, b) 

    if f((a+b)/2) == 0:
        print("u")  

def newton(f,f_prime,initial):
    #computes a single iteration of newton's method
    #returns the next term

    #f = function to plug in
    #f_prime = deriviatve function
    #initial = initial value to start with

    return ( initial - (f(initial)/f_prime(initial)) )
    

def secant(f,initial,initial2):
    #complutes a single iteration of the secant method
    #returns the next term

    #f = function to plug in
    #initial = first initial value ( x_i )
    #initial2 = second initial value( x_(i-1) )

    try:
        fraction = ( (f(initial)*(initial-initial2)) / ( f(initial) - f(initial2) ) )
    except:
        print("divided by 0")
        return initial

    return initial - fraction
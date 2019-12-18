#performs horners algorithm on a given polynomial
def horners_method(polynomial, c):
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
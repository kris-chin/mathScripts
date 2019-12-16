'''

    SimpleLinearRegression.py

    A simple linear regression class by scratch.
    For use when you have one explanatory variable and one scalar response.

'''
from math import sqrt

def SimpleLinearRegression(x,y):
    #x is an array-like of x values of the points
    #y is an array-like of y values of the points
    #returns a tuple with the first element being a single regression coefficient and the second element being the intercept term

    #Y = a + bX
    #b = r*stddev(y)/stddev(x)
    #a = mean(y)- b*mean(x)
    #pearson's R = sum(xy) / sqrt( sum(x^2)*sum(y^2) )
    #stdev = sqrt( sum( (X-mean)^2 ) / N )

    #convert values to python ints to avoid overflow. (just in case)
    x = [int(i) for i in x]
    y = [int(i) for i in y]

    #calculate the respective summations for the formulas for mean, standard deviation, and pearson correlation
    N = len(x) #count. assuming the number of x values is the same as the number of y values
    x_bar = sum(x)/N #mean of the x values
    y_bar = sum(y)/N #mean of the y values
    std_x = sqrt( sum( (i-x_bar)**2 for i in x ) / N ) #standard deviation of the x values
    std_y = sqrt( sum( (i-y_bar)**2 for i in y ) / N ) #standard devation of the y values
    
    r = sum(a*b for a,b in zip(x,y)) / sqrt(sum(i**2 for i in x) * sum(i**2 for i in y)) #pearson's r in one line of code.

    #compute our respective b and a values for the line
    b = r*(std_y/std_x) #regression coefficient
    a = y_bar-b*x_bar #regression intercept

    return (b,a)
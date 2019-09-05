'''

    MultipleLinearRegression.py

    A multiple linear regression class by scratch.
    For use when you have multiple explanatory variables and one scalar response


'''

import math
import numpy as np

def MultipleLinearRegression(x,y):
    #x is a numpy matrix. its dimensions are (number of points)x(number of explanatory variables)
    # -each row represents a point. (a single point cointaining an x0, x1, x2, etc)
    # -each column is an additional explanatory variable (column of x0's, column of x1's, column of x2's, etc)

    #y is an array-like of the dependent variables.
    # -must be the same length as x's height. (number of points)

    #returns a list of regression coefficients from increasing order wtih it's length being (the number of explanatory variables + 1)
    #the first item is beta0, the regression intercept

    #----------------------------------------------------

    

    betaCoefficients = []


    return betaCoefficients
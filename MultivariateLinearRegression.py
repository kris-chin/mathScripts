'''

    MultivariateLinearRegression.py

    A multivariate linear regression class by scratch.
    For use when you have multiple explanatory variables and multiple response variables.
    (Also referred to as the General Linear Model)

    refer to bruh.jpg for a representation of the model

'''

import math
import numpy as np

def MultivariateLinearRegression(x,y):
    #x = numpy matrix. each row is a point. each column is an independent variable
    #y = numpy matrix. each row is a point. each column is a dependent variable.
    #----------------------------------------------------

    #the model is similar to the multiple regression model. except Y and B are now matrices instead of vectors

    #format: X = [1 x11 x12 ... x1p    Y = [y11 y12 ... y1j     Beta = [B11 B12 ... B1j
    #             1 x21 x22 ... x2p         y21 y22 ... y2j             B21 B22 ... B2j
    #             .              .           .           .               .           .
    #             .              .           .           .               .           .
    #             .              .           .           .               .           .
    #             1 xi1 xi2 ... xip]        yi1 yi  ... yij]            Bp1 Bp2 ... Bpj]
    #
    #        X is a i by p matrix         Y is a i by j matrix        Beta is a p by j matrix

    # i = number of points
    # p = number of independent variables (x0, x1, ... , xp)
    # j = number of dependent variables (y0, y1, ... ,yj)
    
    #this means the entire entire plot can be represented by a rank-3 tensor (i x p x j)

    #returns a p by j matrix of regression coefficients. (beta)

    #----------------------------------------------------


    print("todo")
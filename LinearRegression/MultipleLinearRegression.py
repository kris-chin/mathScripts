'''

    MultipleLinearRegression.py

    A multiple linear regression class by scratch.
    For use when you have multiple explanatory variables and one scalar response

    the equations for this were found on:
    http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf


'''

import math
import numpy as np

def MultipleLinearRegression(x,y):
    #x is a numpy matrix. its dimensions are:
    #(n = number of points) x (1 + k = number of explanatory variables)
    #    -each row represents a point. (a single point cointaining an 1, x0, x1, x2, etc) (the 1 is for the regresison intercept)
    #    -each column is an additional explanatory variable (column of 1's, column of x0's, column of x1's, etc)

    #format: X = [1 x11 x12 ... x1k    Y = [y1     Beta = [B0
    #             1 x21 x22 ... x2k         y2             B1
    #             .              .          .              .
    #             .              .          .              .
    #             .              .          .              .
    #             1 xn1 xn2 ... xnk]        yn]            Bk]

    #y is an array-like of the dependent variables.
    # -must be the same length as x's height. (n)
    # -we will turn it into a nx1 matrix.

    #returns a list of regression coefficients from increasing order wtih it's length being (the number of explanatory variables + 1)
    #the first item is beta0, the regression intercept

    #----------------------------------------------------

    #Y0 = b0 + b1*x00 + b2*x01 + ...
    #Y1 = b0 + b1*x10 + b2*x11 + ...
    #Y2 = b0 + b1*x20 + b2*x21 + ...
    #Y3 = b0 + b1*x30 + b2*x31 + ...

    #BETA MATRIX =  (X'X)^-1 X'y 

    #----------------------------------------------------

    #convert y into a nx1 numpy matrix (if not already)
    if isinstance(y,np.ndarray) == False:
        #print("y is not an nx1 numpy matrix. converting...")
        y = np.asarray([y]).T #convert list to a transposed numpy matrix
    
    #compute the beta matrix
    tXy = np.dot(x.T,y)
    #try the inverse of X' * X
    try:
        inverseXtX = np.linalg.inv(np.dot(x.T,x))
        beta = np.dot(inverseXtX, tXy) #compute the beta using the inverse
        #print("The determininant of X'X is computable")
        
    except:
        print("The determininant of X'X is 0. Solution may not be unique")
        beta = tXy #if inverse doesn't exist

    #convert beta into a list
    beta = [x[0] for x in beta.tolist()]

    return beta
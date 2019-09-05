'''
    Author: Krischin Layon

    practice_linreg
    
    -linear regression algorithms coded by scratch for demonstration purposes

    #TODO: implement multiple linear regression (x is a vector)
    #TODO: implement multivariate/general linear regression (x AND y are vectors)

    uses:
        -numpy for matrices only.
        -matplotlib for plotting

'''
import numpy as np
from matplotlib import pyplot as plt

from SimpleLinearRegression import SimpleLinearRegression #Simple Linear Regression from Scratch

#generates a Countx2 matrix. the first column is the x value. the second column is the y value. Every row is a point on the scatterplot
def generate_simple_data(count,spread):
    #count = how many values to generate
    #spread = the maximum magnitude offset of the y values
    coords = np.zeros((1,2),int) #start with a 1x2 array of 0s
    for i in range(count-1):
        if spread != 0: noise = np.random.randint(-spread,spread) #generate noise for the y value
        else: noise = spread
        coords = np.vstack((coords,[i,i+noise])) #vertically stack a new 1x2 row to the coords matrix, effectively adding a new point to the scatterplot
    return coords

#i just renamed this so i don't have to keep testing simple regression
def testSimpleReg():
    #initialize plt
    fig = plt.figure()
    ax = plt.axes()

    #generate and plot the random data
    plot = generate_simple_data(100,25) #the first column of a matrix is refered to as plot[:,0], the second column of a matrix is refered to as plot[:,1]
    scatter = plt.scatter(plot[:,0],plot[:,1]) #plot the random values

    #generate and plot the simple linear regression
    simpleLinReg = SimpleLinearRegression(plot[:,0],plot[:,1]) #generate the simple linear regression
    print("b = " + str(simpleLinReg[0]) + "\na = " + str(simpleLinReg[1])) #print for demonstration purposes
    y = plot[:,0]*simpleLinReg[0] + simpleLinReg[1] #this is the equation of the manual simpleLinReg line
    plt.plot(plot[:,0], y,'-r') #plot the manual simplelinReg Line

    #show plt
    ax.set_ylim(bottom=0,top=100) #set the plot to focus on the scatterplot
    plt.title("Demonstration of Linear Regression From Scratch")
    plt.show()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def generate_multiple_reg_data():
    print("TODO")

def testMultipleReg():
    #initalize plt
    fig = plt.figure()
    ax = plt.axes()

    #show plt
    plt.title("Demonstration of Multiple Regression From Scratch")
    plt.show()


testMultipleReg()
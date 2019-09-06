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
from mpl_toolkits import mplot3d #3d compatibility for multiple regression
import math

from SimpleLinearRegression import SimpleLinearRegression #Simple Linear Regression from Scratch
from MultipleLinearRegression import MultipleLinearRegression #Multiple Linear Regression from Scratch

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
def generate_multiple_reg_data(N,k,spread):
    #returns a tuple of a x numpy matrix and a y numpy matrix
    #N = number of points
    #k = number of explanatory variables. there will be k+1 columns with the first column being all 1s

    xmatrix = np.zeros((N,k+1),int) #N by (k+1) matrix
    for x in xmatrix: x[0] = 1 #set the first column to 1. (the intercept column)

    #set random explanatory variable values
    for x in xmatrix: x[1] = np.random.randint(-spread,spread) #generate random points like this for now
    for x in xmatrix: x[2] = np.random.randint(-spread,spread) #generate random points like this for now

    ymatrix = np.zeros((N,1),int) #N by 1 matrix
    #set random response values
    ymatrix = [math.sin(x) for x in xmatrix[:,1]] #idk, i'll set it to the sine function for now :P
    #for y in ymatrix: y[0] = np.random.randint(-spread,spread)

    return (xmatrix,ymatrix)

def testMultipleReg():
    #initalize plt
    fig = plt.figure()
    ax = plt.axes(projection = "3d")

    spreadValue = 10 #this is our test spread value

    #we'll just start with 2 explanatory variables. (the plot's x and y)
    #our response variable will be the plot's z
    plot = generate_multiple_reg_data(100,2,spreadValue)
    ax.scatter3D(plot[0][:,1],plot[0][:,2],plot[1])
    
    coefficients = MultipleLinearRegression(plot[0],plot[1]) #generate the correlation coefficients for each explanatory variable
   
    regX = np.linspace(-spreadValue,spreadValue,30) #set up a linspace for the prediction surface
    regY = np.linspace(-spreadValue,spreadValue,30) #set up another linspace for the prediciton surface
    def z(x,y): return coefficients[0]+coefficients[1]*x+coefficients[2]*y #this is our 2-explanatory variable equation. z = b0 + b1*x1 + b2*x2
    multiRegX, multiRegY = np.meshgrid(regX,regY)

    ax.plot_wireframe(multiRegX, multiRegY, z(multiRegX,multiRegY),color="red") #plot our prediction
    
    #show plt
    plt.title("Demonstration of Multiple Regression From Scratch")
    plt.show()

testMultipleReg()
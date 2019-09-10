'''
    Author: Krischin Layon

    practice_linreg
    
    -linear regression algorithms coded by scratch for demonstration purposes

    uses:
        -numpy for matrices only.
        -matplotlib for plotting

'''
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d #3d compatibility for multiple regression
import math
import random

from SimpleLinearRegression import SimpleLinearRegression #Simple Linear Regression from Scratch
from MultipleLinearRegression import MultipleLinearRegression #Multiple Linear Regression from Scratch
from MultivariateLinearRegression import MultivariateLinearRegression #Multivariate Linear Regression from Scatch

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

    #this is our actual regression requation designed for 2 explanatory variables
    def z(x,y): return coefficients[0]+coefficients[1]*x+coefficients[2]*y

    multiRegX, multiRegY = np.meshgrid(regX,regY)

    ax.plot_wireframe(multiRegX, multiRegY, z(multiRegX,multiRegY),color="red") #plot our prediction
    
    #show plt
    plt.title("Demonstration of Multiple Regression From Scratch")
    plt.show()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def generate_multivaraite_reg_data(spread,n):
    #spread = range of random values
    #n = number of points to generate
    #returns just a list.

    return [random.randint(-spread,spread) for i in range(n)]


def testMultivariateReg():

    spread = 100
    count = 250

    #i = 5, p = 3, 
    independentVar1 = generate_multivaraite_reg_data(spread,count)
    independentVar2 = generate_multivaraite_reg_data(spread,count)
    xMatrix = np.array([[1 for i in independentVar1],independentVar1,independentVar2]).T
    print("xmatrix:\n" + str(xMatrix))

    dependentVar1 = [a+b for a,b in zip(independentVar1,independentVar2)]
    dependentVar2 = [b-a for a,b in zip(independentVar1,independentVar2)]
    yMatrix = np.array([dependentVar1, dependentVar2]).T
    print("ymatrix:\n" + str(yMatrix))
    
    maxval = max([max(dependentVar1),max(dependentVar2)])
    betaMatrix = MultivariateLinearRegression(xMatrix,yMatrix).astype(int)

    #this is our regression formula
    def yHat(x):
        #x is a tuple of 2 independent variables. (as provided in our example of 2 independent variables)
        #returns a tuple of 2 dependent variables. (as provided by our example of 2 dependent variables)
        y1 = betaMatrix[0,0] + (x[0]*betaMatrix[1,0]) + (x[1]*betaMatrix[2,0])
        y2 = betaMatrix[0,1] + (x[0]*betaMatrix[1,1]) + (x[1]*betaMatrix[2,1])
        return (y1,y2)
        
    print("betaMatrix:\n"+ str(betaMatrix))

    #compute regression
    regX1 = [math.sin(i)*(spread/2) for i in np.linspace(-maxval,maxval,count/4)]
    regX2 = [math.cos(i)*(spread/2) for i in np.linspace(-maxval,maxval,count/4)]
    
    regX_matrix = np.array([[1 for i in range(count)],regX1,regX2]).T #set up x

    regY1 = []
    regY2 = []
    for a,b in zip(regX1,regX2):
        Y = yHat((a,b))
        regY1.append(Y[0])
        regY2.append(Y[1])

    #we will plot the independent vars and dependant vars on 2 seperate 2D subplots. (i can't think of a proper way to vizualize them)

    #initialize plt
    fig = plt.figure()
    ax1, ax2 = fig.subplots(2)

    #first plot our pre-defined values
    colorList = [(a*b) for a,b in zip(independentVar1,independentVar2)] #this maps the color of the x's to the color of the y's.

    ax1.scatter(independentVar1,independentVar2,c=colorList,cmap='hsv',s=10)
    ax1.set(xlabel="x0",ylabel="x1",aspect='equal',xlim=[-spread,spread],ylim=[-spread,spread])
    ax1.spines['left'].set_position('center')
    ax1.spines['bottom'].set_position('center')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')

    ax2.scatter(dependentVar1,dependentVar2,c=colorList,cmap='hsv',s=10)
    ax2.set(xlabel="y0",ylabel="y1",aspect='equal',xlim=[-maxval,maxval],ylim=[-maxval,maxval])
    ax2.spines['left'].set_position('center')
    ax2.spines['bottom'].set_position('center')
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')

    #plot the regression predictions

    #coloring for the regression
    colorList2 = [(a*b) for a,b in zip(regX1,regX2)]

    ax1.scatter(regX1,regX2,c=colorList2,cmap='twilight_shifted')
    ax2.scatter(regY1,regY2,c=colorList2,cmap='twilight_shifted')

    plt.show()


#--------------------------------------------------------------------------------------------------------------------------------------------------------

#testSimpleReg()
#testMultipleReg()
testMultivariateReg()
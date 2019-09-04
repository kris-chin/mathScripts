'''
    Author: Krischin Layon

    practice_linreg
    
    -linear regression algorithm coded by scratch for demonstration purposes

    uses numpy and matplotlib

'''

import numpy as np
from matplotlib import pyplot as plt

def leastSquaresRegressionLine(coords):
    #coords is a Countx2 matrix with the first column being the x value and the second column being the y calue

    #returns a tuple containing a slope value and a y-intercept value
    N = len(coords)
    x = coords[:,0]
    
    y = coords[:,1]

    m = (N*sum(x*y) - sum(x)*sum(y) ) / (N*sum(x^2) - sum(x)^2) 
    b = (sum(y) - m*sum(x)) / N

    return (m,b)


#generates a Countx2 matrix. the first column is the x value. the second column is the y value. Every row is a point on the scatterplot
def generate_xy_data(count,spread):
    #count = how many values to generate
    #spread = the maximum magnitude offset of the y values
    coords = np.zeros((1,2),int) #start with a 1x2 array of 0s
    for i in range(count-1):
        noise = np.random.randint(-spread,spread) #generate noise for the y value
        coords = np.vstack((coords,[i,i+noise])) #vertically stack a new 1x2 row to the coords matrix, effectively adding a new point to the scatterplot
    return coords

def main():
    plot = generate_xy_data(100,25)
    fig = plt.figure()
    ax = plt.axes()

    #the first column of a matrix is refered to as plot[:,0] 
    #the second column of a matrix is refered to as plot[:,1]

    scatter = plt.scatter(plot[:,0],plot[:,1])

    line = leastSquaresRegressionLine(plot)

    print("m = " + str(line[0]) + "\nb = " + str(line[1]))

    y = plot[:,0]*line[0] + line[1] #this is the equation of the line

    plt.plot(plot[:,0], y,'-r')

    ax.set_ylim(bottom=0,top=100) #set the plot to focus on the scatterplot

    #labels#
    plt.title("Linear Regression Demonstration")
    plt.show()


main()
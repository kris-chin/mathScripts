'''
    Author: Krischin Layon

    practice_linreg
    
    -linear regression algorithm coded by scratch for demonstration purposes

    uses:
        -numpy for matrices only.
        -matplotlib for plotting
        -scipy's pearson R and numpy's standard deviation for comparision purposes only

'''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import math

def simpleLinearRegression(coords):
    #coords is a Countx2 matrix with the first column being the x values (independent) and the second column being the y values (dependent)
    #returns a tuple with the first element being a single regression coefficient and the second element being the intercept term

    #Y = a + bX
    #b = r*stddev(y)/stddev(x)
    #a = mean(y)- b*mean(x)
    #pearson's R = sum(xy) / sqrt( sum(x^2)*sum(y^2) )
    #stdev = sqrt( sum( (X-mean)^2 ) / N )

    #convert the numpy values to python ints. (to avoid overflow)
    x = [int(i) for i in coords[:,0]]
    y = [int(i) for i in coords[:,1]]

    #calculate the respective summations for the formulas for mean, standard deviation, and pearson correlation
    N = len(coords) #count

    x_bar = sum(x)/N #mean of the x values
    y_bar = sum(y)/N #mean of the y values
    std_x = math.sqrt( sum( (i-x_bar)**2 for i in x ) / N ) #standard deviation of the x values
    std_y = math.sqrt( sum( (i-y_bar)**2 for i in y ) / N ) #standard devation of the y values
    
    r = sum(a*b for a,b in zip(x,y)) / math.sqrt(sum(i**2 for i in x) * sum(i**2 for i in y)) #pearson r in one line of code.

    #comparing the manual method to traditional module methods.
    print("manual R: " + str(r) + "\n scipy R: " + str(stats.pearsonr(x,y)[0]))
    print("manual STD_X: " + str(std_x) + "\n numpy STD_X: " + str(np.std(x)))
    print("manual STD_Y: " + str(std_y) + "\n numpy STD_Y: " + str(np.std(y)))

    #compute our respective b and a values for the line
    b = r*(std_y/std_x)
    a = y_bar-b*x_bar

    return (b,a)

#generates a Countx2 matrix. the first column is the x value. the second column is the y value. Every row is a point on the scatterplot
def generate_xy_data(count,spread):
    #count = how many values to generate
    #spread = the maximum magnitude offset of the y values
    coords = np.zeros((1,2),int) #start with a 1x2 array of 0s
    for i in range(count-1):
        if spread != 0: noise = np.random.randint(-spread,spread) #generate noise for the y value
        else: noise = spread
        coords = np.vstack((coords,[i,i+noise])) #vertically stack a new 1x2 row to the coords matrix, effectively adding a new point to the scatterplot
    return coords

def main():
    fig = plt.figure()
    ax = plt.axes()

    #the first column of a matrix is refered to as plot[:,0] 
    #the second column of a matrix is refered to as plot[:,1]
    plot = generate_xy_data(100,25)
    scatter = plt.scatter(plot[:,0],plot[:,1]) #plot the random values

    simpleLinReg = simpleLinearRegression(plot)
    print("b = " + str(simpleLinReg[0]) + "\na = " + str(simpleLinReg[1]))
    y = plot[:,0]*simpleLinReg[0] + simpleLinReg[1] #this is the equation of the manual simpleLinReg line
    plt.plot(plot[:,0], y,'-r') #plot the manual simplelinReg Line

    ax.set_ylim(bottom=0,top=100) #set the plot to focus on the scatterplot

    #labels#
    plt.title("Demonstration of Linear Regression From Scratch")
    plt.show()

main()
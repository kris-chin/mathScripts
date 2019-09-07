'''
    unit testing for multiple linear regression. tests with real multiple linear regression examples found online

'''

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import numpy as np

from MultipleLinearRegression import MultipleLinearRegression

class TestMultipleLinearRegression(unittest.TestCase):

    def test_R_tutorial_data(self):
        #checks data from this R tutorial: https://datatofish.com/multiple-linear-regression-in-r/
        #they don't compute the linear regression by hand. but we do. so this can kinda be our unit test to see if our computations are like R's computation
        #they have their regression based on stock index price vs (interest rate and unemployment rate)
        interestRate = [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75]
        unemploymentRate = [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1]
        stock_index_price= [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]

        inputXmatrix = np.array([[1 for i in interestRate],interestRate,unemploymentRate]).T #the first column is all 1s. the 2nd is interest_rate. the 3rd is unemployment rate
        
        #we compare up to the first decimal point since that is the most sigfigs we can compare to given the example
        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,stock_index_price)[0],1798.4,1) #intercept
        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,stock_index_price)[1],345.5,1) #interest rate coefficient
        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,stock_index_price)[2],-250.1,1) #unemployment rate coefficient

if __name__ == "__main__":
    unittest.main()
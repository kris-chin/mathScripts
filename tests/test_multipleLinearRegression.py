'''
    unit testing for multiple linear regression. tests with real multiple linear regression examples found online

'''


import unittest
import numpy as np

from MultipleLinearRegression import MultipleLinearRegression

class TestMultipleLinearRegression(unittest.TestCase):

    def test_example(self):
        #TODO: find an online example to try this on!! >:(
        inputXmatrix = np.ndarray((3,3)) #add values based on the online example to this
        inputYmatrix = np.nd_grid((3,1)) #add values based on the online example to this

        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,inputYmatrix)[0],-1,5) #replace -1 with the actual coefficient from the example
        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,inputYmatrix)[1],-1,5) #replace -1 with the actual coefficient from the example
        self.assertAlmostEqual(MultipleLinearRegression(inputXmatrix,inputYmatrix)[2],-1,5) #replace -1 with the actual coefficient from the example


if __name__ == "__main__":
    unittest.main()
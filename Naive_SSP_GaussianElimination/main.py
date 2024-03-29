import numpy as np
from GaussianElimination import gauss_elimination

problem1_A = np.array([[0.4096, 0.1234, 0.3678, 0.2943],
                       [0.2246, 0.3872, 0.4015, 0.1129],
                       [0.3645, 0.1920, 0.3781, 0.0643],
                       [0.1784, 0.4002, 0.2786, 0.3927]
                       ])

problem1_b = np.array([[0.4043],
                       [0.1550],
                       [0.4240],
                       [0.2557]    
                        ])

gauss_elimination(problem1_A, problem1_b, True)

#----------------------------------------------------------------

problem2_A = np.array([  [1.3840, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,-0.1248],
                         [0.0000, 1.5124, 0.0000, 0.0000, 0.0000,-0.3750, 0.0000],
                         [0.0000, 0.0000, 1.7890, 0.0000,-0.2879, 0.0000, 0.0000],
                         [0.0000, 0.0000, 0.0000, 2.2718, 0.0000, 0.0000, 0.0000],
                         [0.0000, 0.0000,-0.4230, 0.0000, 1.5432, 0.0000, 0.0000],
                         [0.0000,-0.0358, 0.0000, 0.0000, 0.0000, 1.8774, 0.0000],
                         [0.1127, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.9125]
                        ])

problem2_b = np.array([ [2.3715],
                        [0.7887],
                       [-4.5612],
                        [3.6233],
                        [0.7819],
                       [-2.1352],
                        [0.1435]
                        ])


gauss_elimination(problem2_A, problem2_b,False)
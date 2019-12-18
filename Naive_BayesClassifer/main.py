'''
    Author: Krischin Layon

    practice_naiveBayes

    a practice naive bayes classifier from scratch for demonstration purposes

    #TODO: rename things so they make more sense
    #TODO: add unit tests

    input taken from https://www.geeksforgeeks.org/naive-bayes-classifiers/

'''

import numpy as np
from Naive_Bayes import classify
#from QuantitativeRange import qunaititativeRange

def main():
    #test code for quantitativeRange()
    '''
    testValues = [1,10,100,10,1,1000]
    conv = [(0,9,"Ones"),(10,99,"Tens"),(100,999,"Hundreds")]
    print(quantitativeRange(testValues,conv))
    '''

    outlooks = ['rainy','rainy','overcast','sunny','sunny','sunny','overcast','rainy','rainy','sunny','rainy','overcast','overcast','sunny']
    temperature = ['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
    humidity = ['high','high','high','high','normal','normal','normal','high','normal','normal','normal','high','normal','high']
    windy = ['false','true','false','false','false','true','true','false','false','false','true','true','false','true']
    features = np.array([outlooks,temperature,humidity,windy]).T

    playGolf = ['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
    responseVector = np.array([playGolf]).T

    today = ('sunny','hot','normal','false')
    classification = classify(features,responseVector,today)
    print(classification)
    

main()
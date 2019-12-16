'''
    Author: Krischin Layon

    practice_naiveBayes

    a practice naive bayes classifier from scratch for demonstration purposes

    #TODO: rename things so they make more sense
    #TODO: add unit tests

    input taken from https://www.geeksforgeeks.org/naive-bayes-classifiers/

'''

import numpy as np

def quantitativeRange(vals,ranges):
    #vals = an n-sized list of quantitative values
    #ranges = a list of 3-tuples. the first item is the lower bound (inclusive), the second item is the upper bound (inclusive), and the last item is the string of the category. ex. "medium distance"
    #     -an 'i' means negative or positive infinity. (on the lower bound, it means negative. if the upper bound, it means positive)
    #returns an n-size list of categorical strings based on the quantitative values
    categories = []

    for v in vals:
        passFails = 0
        for r in ranges:
            inBoundPasses = 0 #get 2 and you pass

            #test lower bound
            if r[0] == 'i': inBoundPasses += 1
            elif v >= r[0]: inBoundPasses += 1

            #test upper bound
            if r[1] == 'i': inBoundPasses += 1
            elif v <= r[1]: inBoundPasses += 1

            #if the value in the appropriate range
            if inBoundPasses == 2:
                categories.append(r[2])
                break
            else: passFails += 1
            
        if passFails >= len(ranges):
            print("WARNING: \"" + str(v) + "\" does not fit in any of the provided ranges. Inputing as \"N/A\"")
            categories.append("N/A")

    return categories

def classify(featureMatrix,responseVector,input):
    #featureMatrix is a n-width numpy matrix of categorical strings.
    #responseVector is a numpy vector of strings for training. 
    #    -each column of the feature matrix is a different categorical variable. each row is an entry
    #input is a n-tuple of input features to attempt to classify
    
    #returns a response string based on the 3rd argument
    #-------------------------------------------------------------------------------------------

    # P(y|x1,x2,...,xn) = ( product( p(xi|y) ) * P(y) ) / product ( p(xi) )

    N = len(featureMatrix[:,0])
    X = featureMatrix.T
    
    #compute the full table for easier computations
    full_table = np.hstack((featureMatrix,responseVector))
    unique_responses = np.unique(responseVector.T).tolist()

    #get p(xi|y)
    p_feature_given_response = [] #a list of len(X)-1 arrays each internal list is len(responseVector) long
    for i in range(len(full_table.T) - 1): #go through every individual feature
        featureList = X[i] 
        unique_features = np.unique(featureList).tolist()

        responseCounts = np.zeros((len(unique_features),len(unique_responses)))

        for val,response in zip(featureList,full_table[:,len(full_table.T) - 1]):
            responseIndex = unique_responses.index(response)
            featureIndex = unique_features.index(val)

            responseCounts[featureIndex,responseIndex] += 1
        
        #print("      " + str(unique_responses))
        
        #for feature in unique_features:
            #print(feature + ": " + str(responseCounts[unique_features.index(feature)]))
        #print("----------------------------------------")


        p_feature_given_response.append(responseCounts)

    #get p(y)s
    p_response = [] #a list of probabilities of the given feature
    for response in unique_responses:
        p_response.append(responseVector.T.tolist()[0].count(response))

    #print("      " + str(unique_responses))
    #print(p_response)

    #calculate p(y|input) for all possible responses
    p_response_given_input = []
    
    for response in unique_responses:
        p_givens = []
        responseIndex = unique_responses.index(response)
        for i in range(len(p_feature_given_response)):
            featureIndex = np.unique(X[i]).tolist().index(input[i])

            p_givens.append(p_feature_given_response[i][featureIndex,responseIndex]/p_response[responseIndex])
        #print(p_givens)
        p_xi = np.product(p_givens) #first multiply all probabilities of input together
        p_response_given_input.append(p_xi*(p_response[responseIndex]/N))

    #print(p_response_given_input)

    #normalize these values
    p_response_given_input = [i/sum(p_response_given_input) for i in p_response_given_input]
    print("      " + str(unique_responses))
    print(p_response_given_input)

    #make prediction based on response with the highest value
    highest_i = 0
    for i in range(len(p_response_given_input)):
        if p_response_given_input[i] == max(p_response_given_input):
            highest_i = i
    return unique_responses[i] #return prediction

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
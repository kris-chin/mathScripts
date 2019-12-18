import numpy as np

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
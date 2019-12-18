import numpy as np

def gauss_elimination(A, b,partialPivoting):
    #A = ixj numpy array
    #b = numpy array
    #partialPivoting = bool. if true, enables partial pivoting. if false, computes naive gauss elimination

    #convert A to its augmented matrix
    oldA = A #for error calculation later
    A = np.append(A,b,1)

    #---------forward elimination--------------------------------
    for j in range(len(A[0]) - 1): #j = collumn
        
        #compute scales and swap rows if necessary
        if partialPivoting:
            s = [0]*(len(A[0])-1-j) #the number of elements in this s list are for the maxes for every row that needs to be compared. we are using 0's for now

            #get the maxes of each row
            for i0 in range(j,len(A)):
                for j0 in range(len(A[0])):
                    #print(i0-j)
                    if abs(A[i0,j0]) > abs(s[i0-j]): s[i0-j] = abs(A[i0,j0]) #get the s values for every non-eliminated row in the matrix

            #get the index of the row with the largest s
            largest_index = 0
            for index in range(len(s)):
                if s[index] > s[largest_index]: largest_index = index

            #swap the current row with the index of the row with the largest s
            A[ [j, j+largest_index] ] = A[ [j+largest_index, j]]
            

        #eliminate
        for i in range(j,len(A)): #i = row
            if (i == j): #if pivot value
                pivot = A[i,j]
                pivot_row = i
            else: #if you're on a row below the pivot value
                c = 0
                for x in range(len(A[i])): #go through the whole row and do row math
                    if c == 0: c = round(A[i,j]/pivot,4) #set coefficient if havent yet
                    A[i,x] = round( (A[i,x] - (c*A[pivot_row,x]) ), 4) #do row math

    #--------backwards substitution-------------------------------

    values = []
    for x in range(len(A)): values.append(None)

    for i in range(len(A.T[0]) - 1,-1,-1): #rows'
        solved_sum = 0
        for j in range(len(A)-1,i-1,-1): #collumns
            if values[j] != None: #multiply the value if it's respective X already exists
                solved_sum += round(A[i,j]*values[j],4)
                A[i,j] -= A[i,j]
            else:
                #subtract the last column value by the sum of all the solved terms 
                A[i,len(A)] -= solved_sum
                #divide, append.
                A[i,len(A)] = round(A[i,len(A)]/A[i,j],4)
                A[i,j] /= A[i,j]
                #print(A[i,len(A)])
                values[j] = A[i,len(A)]

    #--------printing----------------------------------------------
    
    values = np.array([values]).T #convert from list to vector
    print("x: ")
    print(values)
    r = np.dot(oldA,values) - b #caluclate residual by plugging in X and subtracting it from B to see how far from B the value is
    print("residual: ")
    print(r)

    #----------END------------------------------------------------------

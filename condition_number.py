""""program to estimate condition number via sage"""

##First part of program to get norms



#matrix norms, imported from pnormwork...
from sage.misc.prandom import randrange
from sage.misc.randstate import current_randstate


total_sum = 0

def pNorm(vec,p):
    run_sum = 0
    length = len(vec)
    for i in range(0,length):
        sum_vector = abs(vec[i])^p
        run_sum = sum_vector + run_sum
    return n(run_sum^(1/p))  ##n will give us a readable number


def matrixPnorm(mat,vec,p):  #give a matrix and a vector, & p value. will output matrix norm
    w = mat * vec
    w = pNorm(w,p)
    v = pNorm(vec,p)
    return n(w/ v)



##random matrix

def randomMatrix(size):
  matrix = random_matrix(ZZ,size,size)
    return matrix

    #create random vector with 1 as first value in vector
    def randomVec(size): #where size is the number of elements
        import random
        vect = vector(QQ,size)
        vect[0] = 1
        vect[1] =  random.uniform(0.01 , math.pi) #note don't know if this is correct operation for unit sphere
        vect[2] =  random.uniform(0.01, math.pi*2)
        return N(vect)

#script to estimate a condition number
def condEstimate(matrix,y, p): #plug in matrix, z, y , and p -value
    z = matrix * y

    ratio = pNorm(y,p) / pNorm(z,p) #defaulting 1 to p-value
    #matrix_norm = matrixPnorm((matrix)^-1, y, p)
    return ratio


    #script to run about 12 times
def condition_estimate(size): #where size is the n x n matrix
        

    condition_values = vector(QQ,12) #store the values of the condition number
    mean_values = vector(QQ,5)

    for x in range(0,5):

        matrix = randomMatrix(size) #random nxn mat
        for i in range(0,12):
            rand_vector = randomVec(size)

            condition_estimate = condEstimate(matrix,rand_vector,1)

            condition_values[i] = condition_estimate


                #print("condition estimate", condition_estimate)
                #true_value = matrixPnorm((matrix)^-1, rand_vector, 1) # where 1 is p-value
                #print(           "true value:       " , true_value )



                means = mean(condition_values)
                mean_values[x] = means
        print("\n")
        print(N(condition_values))


    print("\n")
    print(N(mean_values))  #where mean_values is a vector that contains 5 averages

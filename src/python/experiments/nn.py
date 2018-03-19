#!/usr/bin/env python

# Import numpy for using matrix operations
import numpy as np

# define an actovation function
def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# 0 0 1 0
# 0 1 1 0
# 1 0 1 1
# 1 1 1 1

# define an input matrix
X = np.array([ [0,0,1], [0,1,1], [1,0,1], [1,1,1] ])

# define an output matrix
y = np.array([[0,0,1,1]]).T

# seed numpy
np.random.seed(1)

# generate some weights
syn0 = 2*np.random.random((3,4)) - 1

# define how often the calculations should be run

n = 100000

# loop
for i in range(n):
    # define the first layer
    l0 = X

    # define the second layer using the first layer and the weights
    l1 = sigmoid(np.dot(l0,syn0))

    # calculate an error
    l1_error = y - l1

    # calculate how fatal the error is
    l1_delta = l1_error * sigmoid(l1,True)

    # adjust the weights
    syn0 += np.dot(l0.T,l1_delta)

    # print some information
    if (i % (n / 10000) == 0):
        print("l1: " + str(l1))

print("")
print("Output After Training:")
print(l1)

l0 = np.array([0, 1, 0])
l1 = sigmoid(np.dot(l0, syn0))
print(l1)

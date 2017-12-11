#!/usr/bin/env python

# Import some libraries
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import sys

# Defining some variables
sigma = 200
f_0 = 0.1
R_s = 1e4

# Defining some constants
pi = math.pi
e = math.e
G = 4.302e-3

# rho function
def rho(r):
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    return a * b

# phi function
def phi(x):
    if x == 0:
        return -4 * pi * f_0 * G * R_s**2
    else:
        a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
        b = np.log(1. + (x / R_s) )
        return a * b

# Defining a list to store the rho-values for plotting
list_rho = []

# Define the path to where the data should be stored
path = 'data/' + str(sys.argv[2]) + '.csv'

# get the start time
start = time.time()

# define the number of stars using system arguments
stars = int(float(sys.argv[1]))

# open the file where the information should be written to
with open(path, "a") as data:

    # for every star
    for i in range(0, stars):

        # calculate the rho value
        rho_i = rho(i/10)

        # append the rho value to list_rho for plotting
        # list_rho.append(rho_i)

        # print the distance to the center of the universe and the rho value to
        # the user
        print(str(i) + ", " + str(rho_i))

        # write the data into the file
        data.write(str(i) + ", " + str(rho_i) + "\n")

# get the end time
end = time.time()

# calculate the runtime
runtime = end - start

# print some information to the user
print("\n Runtime: ", end="")
print(str(runtime) + " seconds")

print(" Stars: " + str(stars))

print(" Rho-values per second: ", end="")
print(str(stars / runtime))

# plt.plot(list_rho)
# plt.xscale('log')
# plt.yscale('log')
# plt.grid()
# plt.show()

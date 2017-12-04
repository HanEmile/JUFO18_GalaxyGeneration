#!/usr/bin/env python

from numpy import genfromtxt
import numpy as np
import math
import os
import socket
import time
host = socket.gethostname()

# variables
sigma = 200
f_0 = 0.1
R_s = 1e4

# constants
pi = math.pi
e = math.e
G = 4.302e-3

# rho function
def rho(r):
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    c = a * b
    return c

# phi function
def phi(x):
    if x == 0:
        return -4 * pi * f_0 * G * R_s**2

    a = - ( 4 * pi * G * f_0 * R_s ** 3 ) / x
    b = np.log(1. + (x / R_s) )
    c = a * b
    return c

def gen_stars(stars):
    stars = int(stars)

    # lists
    listrho = []

    # create new file for every calculation
    path = "data/" + str(host) + "_" + str(os.getpid()) + ".csv"
    print("path: " + str(path))

    # define the size of the galaxy
    length = 1.5e6

    # define the borders
    range_min = -int(length)
    range_max = int(length)

    # define the rho range
    rand_min = rho(0)
    rand_max = rho(math.sqrt(length**2 + length**2))

    # create random stars
    for r in range(0, stars):
        x = np.random.uniform(range_min, range_max, size=1)
        y = np.random.uniform(range_min, range_max, size=1)
        rand_val = np.random.uniform(rand_min, rand_max, size=1)
        rho_xy = rho(math.sqrt(x**2 + y**2))

        print("{:<20}{:<20}{:<20}{:<20}".format(str(x), str(y), str(rho_xy), str(rand_val)))

        # if the random value is smaller than the rho value, generate a star
        if rand_val < rho_xy:

            # open a file to write to
            with open(path, "a") as data:

                # write the data to the file
                data.write(str(x).strip("[]") + "," + str(y).strip("[]") + "\n")
                print(str(x) + ", " + str(y))

    print("range_min: " + str(range_min))
    print("range_max: " + str(range_max))

    print("rand_min: " + str(rand_min))
    print("rand_max: " + str(rand_max))

# generate n stars
gen_stars(1e5)

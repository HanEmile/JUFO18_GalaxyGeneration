from numpy import genfromtxt
import numpy as np
import math
import os
import socket
host = socket.gethostname()

# variables
sigma = 200
f_0 = 0.1
R_s = 1e4

# M..
Mxx = 0
Mxy = 8e-6
Myy = 0

# constants
pi = math.pi
e = math.e
G = 4.302e-3

# rho function
def rho(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    a = (1) / (math.sqrt( 2 * pi ) * sigma )
    b = math.exp( - (phi(r) / sigma ** 2 ) )
    c = a * b
    return c

def rho_new(x, y, z):
    a = (1 - ((1) / (2 * (sigma ** 2))) * ( Mxx * x**2 + 2 * Mxy * x * y + Myy * y**2 ) )
    return rho(x, y, z) * a

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

    time_start = time.time()

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
    rand_min = rho_new(0, 0, 0)
    rand_max = rho_new(length, 0, 0)

    # create random stars
    for r in range(0, stars):
        x = np.random.uniform(range_min, range_max, size=1)
        y = np.random.uniform(range_min, range_max, size=1)
        z = np.random.uniform(range_min, range_max, size=1)
        rand_val = np.random.uniform(rand_min, rand_max, size=1)

        # if the random value is smaller than the rho value, generate a star
        if rand_val < rho(x, y, z):

            # open a file to write to
            with open(path, "a") as data:

                # write the data to the file
                data.write(str(x).strip("[]") + "," + str(y).strip("[]") + "," + str(z).strip("[]") + "\n")

# generate n stars
gen_stars(5e7)

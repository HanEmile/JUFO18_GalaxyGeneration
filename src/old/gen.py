#!/usr/bin/env python

from numpy import genfromtxt
import numpy as np
import math
import os
import socket
import time
import matplotlib.pyplot as plt
host = socket.gethostname()

listx = []
listy = []

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

        # if the random value is smaller than the rho value, generate a star
        if rand_val < rho_xy:

            # open a file to write to
            with open(path, "a") as data:

                # write the data to the file
                data.write(str(x).strip("[]") + "," + str(y).strip("[]") + "\n")
                listx.append(x)
                listy.append(y)
                print(str(x) + ", " + str(y))

    print("range_min: " + str(range_min))
    print("range_max: " + str(range_max))

    print("rand_min: " + str(rand_min))
    print("rand_max: " + str(rand_max))

# generate n stars
gen_stars(1e6)

# plot the stars coordinates in 2D space
plt.scatter(listx, listy)
plt.show()

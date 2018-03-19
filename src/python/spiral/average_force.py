#!/usr/bin/env python

# import stuff
import sys
import matplotlib.pyplot as plt
import numpy as np
import time
from subprocess import call

# define from where to get the star data
path = "stars/" + sys.argv[1] + ".csv"

# define a list to store the coordinates
listx = []
listy = []
listz = []
list_force = []

# define constants
G = 6.674e-11

def glaw(m1, m2, a1, b1):
    a = m1 * m2
    b = np.power(a1 - b1, 2)
    c = np.sqrt(b)
    d = a / c
    e = G * d
    return e

# start the timer
start = time.time()

# open the data file
with open(path) as f:

    # read the individial lines from the data file
    data = f.readlines()

    # for each line
    for i in range(0, len(data)):

        # parse the first value in each line
        v_i_x = data[i].split(", ")[0]
        v_i_y = data[i].split(", ")[1]
        v_i_z = data[i].split(", ")[2]

        print("{:20}{:20}{:20}".format("v_i_x", "v_j_x", "v_f_x"))
        # print it
        # print("{:20}{:20}{:20}".format(v_i_x, v_i_y, v_i_z))

        # append it to lista for further usage
        listx.append(v_i_x)
        listy.append(v_i_y)
        listy.append(v_i_z)

        for j in range(0, len(data)):
            v_j_x = data[j].split(", ")[0].strip("\n")
            v_j_y = data[j].split(", ")[1].strip("\n")
            v_j_z = data[j].split(", ")[2].strip("\n")

            if(v_j_x != v_i_x):
                pv_f_x = glaw(int(1), int(2), float(v_i_x), float(v_j_x))
                print("{:20}{:20}{:20}".format(v_i_x.strip("\n"), v_j_x, v_f_x))

            if(v_j_y != v_i_y):
                v_f_y = glaw(int(1), int(2), float(v_i_y), float(v_j_y))
                print("{:20}{:20}{:20}".format(v_i_y.strip("\n"), v_j_y, v_f_y))

            if(v_j_z != v_i_z):
                v_f_z = glaw(int(1), int(2), float(v_i_z), float(v_j_z))
                print("{:20}{:20}{:20}".format(v_i_z.strip("\n"), v_j_z, v_f_z))


        print("---\n")

print("")
end = time.time()
whole_time = end - start
out = ">> Finished calculating the forces in " + str(whole_time) + " seconds\n"
print(out)

try:
    call(["telegram-send", "--pre", str(out) ])
except Exception:
    print("Failed to send telegram message D:")


# # initialize some variables
# sum_a = 0
# avarage_a = 0
#
# # calculate the average value
# for i in range(0, 40):
#     sum_a += float(lista[i])
#
# # calculate the average
# avarage_a = sum_a / 40
#
# # print the average
# print("avarage_a: " + str(avarage_a))

# sort lista and store the result in listb
# listb = sorted(lista)

# plot listb using a normal line, red color and round markers
# plt.plot(lista, "-ro")

# dispaly the plot
# plt.show()

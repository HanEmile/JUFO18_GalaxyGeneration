#!/usr/bin/env python

import numpy as np

num = 1e6

# generate random coordinates
rand_a = (np.random.rand(num, 3) * 2000) - 1000
print(rand_a)

# Out goal is to define a 6D array in wich the first three dimension describe
# the a point, in out case, the corner of a cell containing some stars.
# The other three dimensions are used to store a vector descibing the overall
# forces in the cell.

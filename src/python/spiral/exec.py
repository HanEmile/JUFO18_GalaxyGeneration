#!/usr/bin/env python3

import galaxytools as galaxytools
import time as time
# import matplotlib.pyplot as plt

# start the timer
start = time.time()

# generate a new galaxy
galaxy = galaxytools.new_galaxy(64)

# generate 100 stars
galaxy.gen_new_stars(1000)

# galaxy.print_stars()

# calculate the forces acting inbetween the stars
galaxy.calc_all_forces()

# print out the individual forces acting on each star
# galaxy.print_individual_forces()

galaxy.gen_sphere_positions(0.0001)
# galaxy.gen_forces_after_t(1)

galaxy.is_star_in_sphere_all()

# save the stop time
end = time.time()

# calculate the elapsed time
whole_time = end - start

# print the time and append it to a list
print("Time:")
print(whole_time)

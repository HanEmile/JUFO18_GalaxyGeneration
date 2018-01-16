#!/usr/bin/env python

# import libraries
import time
import numpy as np
import sys
from subprocess import call

# define the number of stars that should be generated
nos = int(sys.argv[1])

# define various paths
path = "data/2e7.csv"
save_path = "stars/" + sys.argv[2] + ".csv"

# define the random-value range [rho_min; rho_max]
rand_min = 0
rand_max = 1477.1586582000994

# define the range (size) of the galaxy
range_min = -1e8
range_max = -range_min

# main function
def main():

    # define the variables for storing the amount of stars kept or kicked away
    stars_kept = 0
    stars_kicked = 0

    # start the timer
    start = time.time()

    # open the rho file
    with open(path) as data:
        # read out the lines from the rho file
        rho_file = data.readlines()

        # for every star...
        while(stars_kept < nos):

            # generate the random star-coordinates
            x = np.random.uniform(range_min, range_max, size=1)
            y = np.random.uniform(range_min, range_max, size=1)
            z = np.random.uniform(range_min, range_max, size=1)

            # calculate the distance of the star to the center of the galaxy
            r = np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

            # generate a random value in the range [rand_min; rand_max]
            a = np.random.uniform(rand_min, rand_max, size=1)

            # read out the corresponding rho value from the lookuptable (rho-file)
            b = float(rho_file[round(int(r / 10), 0)].split(", ")[1].strip("\n"))

            # if the random value is smaller than the corresponding rho value
            if(a < b):

                with open(save_path, "a") as stars_data:
                    stars_data.write(str(float(x)) + ", " + str(float(y)) + ", " + str(float(z)) + "\n")

                # increment the stars_kept counter
                stars_kept += 1
                print(stars_kept)

            else:
                # increment the star_kicked counter
                stars_kicked += 1

    print("")
    end = time.time()
    whole_time = end - start
    out = ">> Finished generating stars in " + str(whole_time) + " seconds\n"
    print(out)

    # time_all = whole_time + time_write_file
    time_all = whole_time

    time_min = round(time_all / 60, 1)

    # print some stats
    print("")
    print("{:<20}{:<20}".format("Time (complete)", str(round(time_all, 4)) + " seconds"))
    print("{:-<40}".format(""))
    print("{:<20}{:<20}".format("Number of Stars", str(nos)))
    print("{:<20}{:<20}".format("Stars Kicked:", str(stars_kicked)))
    print("{:<20}{:<20}".format("Percent: ", str( nos / stars_kicked * 100 ) + "%"))

    hour = int( time_all // 3600 )
    time_all = time_all % 3600
    minutes = int( time_all // 60 )
    time_all = time_all % 60
    seconds = int( time_all )

    a = "stars/" + str(sys.argv[2]) + ".csv"

    time_a = str(hour) + ":" + str(minutes) + ":" + str(seconds)
    b = "{:<20}{:<20}".format("Time (h:m:s)", time_a )
    c = "{:<20}{:<20}".format("Number of Stars", str(nos))
    d = "{:<20}{:<20}".format("Stars Kicked:", str(stars_kicked))
    e = "{:<20}{:<20}".format("Percent: ", str( nos / stars_kicked * 100 ) + "%")

    f = a + "\n" + b + "\n" + c + "\n" + d + "\n" + e

    call(["telegram-send", "--pre", str(f) ])
    call(["telegram-send", "-f", str(a) ])


if __name__ == "__main__":
    main()

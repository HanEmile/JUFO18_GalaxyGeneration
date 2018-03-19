#!/usr/bin/env python

# import libraries
import time                             # time how long operations take
import numpy as np                      # advanced math
import argparse                         # fancy parsing
from multiprocessing import Process     # multiprocessing!
import multiprocessing                  # mor multiprocessing (corecount)

# get the amount of cores in the system
cpu_count = multiprocessing.cpu_count()

# generate a parser
parser = argparse.ArgumentParser(
    description="Star Coordinate Generator",
    usage='./%(prog)s <number of stars> <path> [-l LOOKUP] [-r RANGE] [-m CORES] [-h]',
)

# add some arguments to the parser
parser.add_argument("nos", help="Number of stars that should be generated")
parser.add_argument("path", help="Name of the file where the coordinates of the stars should be saved")
parser.add_argument("-l", dest="lookup", help="Define a custom lookuptable filepath", default="1e7")
parser.add_argument("-r", dest="range", help="Define a custom range in where the stars should be generated", default="1e7")
parser.add_argument("-m", dest="cores", help=f"Enable Multithreading with up to {cpu_count} cores", default="2")

# extract the arguments for further use
args = parser.parse_args()

# define the number of stars that should be generated
nos = int(args.nos)

# define the file where the stars should be saved
save_path = "stars/" + str(args.path) + ".csv"

# define the path to the lookuptable
# (The default args.lookup value is 1e7)
path = "data/" + str(args.lookup) + ".big.csv"

# define a varible storing how many cores should be user to compute
cores = int(args.cores)

def gen_stars(nos, threads):
    # define the range (size) of the galaxy
    range_max = int(float(args.range))
    range_min = - range_max

    # define the random-value range [rho_min; rho_max]
    rand_min = 0
    rand_max = 1477.1586582000994

    stars_kept = 0
    stars_kicked = 0

    local_nos = int(nos / threads)

    np.random.seed()

    # open the rho file
    with open(path) as data:

        # read out the lines from the rho file
        rho_file = data.readlines()

        # the anticipated amount of stars is not reached...
        while(stars_kept < local_nos):

            # generate the random star-coordinates
            x = np.random.uniform(range_min, range_max, size=1)
            y = np.random.uniform(range_min, range_max, size=1)
            z = np.random.uniform(range_min, range_max, size=1)

            # calculate the distance of the star to the center of the galaxy
            r = np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
            # print(round(int(r), 0))

            # generate a random value in the range [rand_n; rand_max]
            a = np.random.uniform(rand_min, rand_max, size=1)

            # read out the corresponding rho value from the lookuptable (rho-file)
            # print(round(int(r), 0))
            b = float(rho_file[round(int(r), 0)].split(", ")[1].strip("\n"))

            # if the random value is smaller than the corresponding rho value
            if(a < b):

                # open the stars_data file and save the coordinates
                with open(save_path, "a") as stars_data:
                    stars_data.write(str(x) + ", " + str(y) + ", " + str(z) + "\n")

                # increment the star_kept counter
                stars_kept += 1
                print(f"Stars Kept: {stars_kept}")

            else:
                # increment the star_kicked counter
                stars_kicked += 1

# main function
def main():

    # start the timer
    start = time.time()

    # calculate how many stars each core should generate
    # BUG: local_nos might be wrong because of int rounding down
    local_nos = int(nos / cores)

    print(f"Generating {local_nos} Stars using the {path} lookuptable utilizing {cores} cores")

    # define a base threads and stor it n times in a list
    threads = [Process(target=gen_stars, args=(nos, cores, )) for i in range(0, cores)]

    # start the threads in the lsit
    # for thread in threads:
    for i in range(0, len(threads)):
        threads[i].start()
        print(f"Thread {i} Started!")
        # thread.start()

    # join the threads
    # for thread in threads:
    for i in range(0, len(threads)):
        threads[i].join()
        # thread.join()

    # time stuff
    end = time.time()
    time_all = end - start
    out = ">> Finished generating stars in " + str(time_all) + " seconds\n"
    print(out)

if __name__ == "__main__":
    main()

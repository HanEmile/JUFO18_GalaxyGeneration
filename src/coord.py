#!/usr/bin/env python

# import libraries
import time
import numpy as np
import sys

# define the number of stars that should be generated
# (this is not the final value -> the final value is about 1000 times smaller)
nos = int(sys.argv[1])

# define some arrays for storing the values
arr_stars = np.zeros((int(nos), 3))
arr_r = np.zeros((int(nos), 1))
arr_saved_stars = np.zeros((int(nos), 3))

# define various paths
path = "data/rho6.csv"
save_path = "stars/star18.csv"
# star13 -> 586 stars

# define the random-value range [rho_min; rho_max]
rand_min = 0
rand_max = 1477.1586582000994

# define the range (size) of the galaxy
range_min = -1e7
range_max = 1e7

# main function
def main():

    time_start_gen_array = time.time()

    # generate n=nos stars
    for i in range(0, nos):

        # generate the random values
        arr_stars[i][0] = np.random.uniform(range_min, range_max, size=1)
        arr_stars[i][1] = np.random.uniform(range_min, range_max, size=1)
        arr_stars[i][2] = np.random.uniform(range_min, range_max, size=1)

        # calculate the distance of the star to the center of the galaxy
        arr_r[i][0] = np.sqrt(pow(arr_stars[i][0], 2) + pow(arr_stars[i][1], 2) + pow(arr_stars[i][2], 2))

    # print the randomly generated arrays
    print(arr_stars)
    print(arr_r)

    time_end_gen_array = time.time()
    time_all_gen_array = time_end_gen_array - time_start_gen_array
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
        for i in range(0, nos):
            # print(i)

            # random value
            a = np.random.uniform(rand_min, rand_max, size=1)

            # corresponding rho value
            b = float(rho_file[int(round(arr_r[i][0], 0))].split(", ")[1].strip("\n"))

            # if the random value is smaller than the corresponding rho value
            if( a < b):
                # add the coordinate to arr_saved_stars
                arr_saved_stars[stars_kept][0] = arr_stars[i][0]
                arr_saved_stars[stars_kept][1] = arr_stars[i][1]
                arr_saved_stars[stars_kept][2] = arr_stars[i][2]

                # increment the star_kept counter
                stars_kept += 1

            else:
                # increment the star_kicked counter
                stars_kicked += 1

            if(i % (nos/(nos/10)) == 0):
                if(i != 0):
                    a = str(round(i / nos * 100, 1)) + "%"
                    time_temp = time.time()
                    time_past = round(time_temp - start, 2)
                    print("{:<10}{:<20}".format(a, time_past))

    print("")
    end = time.time()
    whole_time = end - start
    print(">> Finished generating stars in " + str(whole_time) + " seconds\n")

    start_delete_rows = time.time()

    # delete all unused rows
    print(">> Deleting unused rows in the arr_saved_stars array")
    # for i in range(nos - stars_kicked, nos):
    #     np.delete(arr_saved_stars, (i), axis=0)
    end_delete_rows = time.time()
    time_delete_rows = end_delete_rows - start_delete_rows
    print(">> Finished deleting stars in " + str(round(time_delete_rows, 4)) + " seconds \n")

    start_write_file = time.time()

    # write the star coordinates to a file
    print(">> Writing the star-data to " + save_path)
    with open(save_path, "a") as stars_data:
        for i in range(0, nos):
            x = arr_saved_stars[i][0]
            y = arr_saved_stars[i][1]
            z = arr_saved_stars[i][2]

            stars_data.write(str(x) + ", " + str(y) + ", " + str(z) + "\n")

    end_write_file = time.time()
    time_write_file = end_write_file - start_write_file
    print(">> Finished writing star-data to " + save_path + " in " + str(round(time_write_file, 4)) + " seconds\n")


    stars_percent = stars_kept / nos * 100

    time_all = whole_time + time_write_file + time_delete_rows

    # print some stats
    print("")
    print("{:<30}{:<30}".format("Time (complete)", str(round(time_all, 4)) + " seconds"))
    print("{:<30}{:<30}".format("Time (gen arrays)", str(round(time_all_gen_array, 4)) + " seconds"))
    print("{:<30}{:<30}".format("Time (calculate stars)", str(round(whole_time, 4)) + " seconds"))
    print("{:<30}{:<30}".format("Time (delete rows)", str(round(time_delete_rows, 4)) + " seconds"))
    print("{:<30}{:<30}".format("Time (write to file)", str(round(time_write_file, 4)) + " seconds"))
    print("{:-<40}".format(""))
    print("{:<20}{:<20}".format("Number of Stars", str(nos)))
    print("{:<20}{:<20}".format("Stars Kept:", str(stars_kept)))
    print("{:<20}{:<20}".format("Stars Kicked:", str(stars_kicked)))
    print("{:<20}{:<20}".format("Stars Percent", str(round(stars_percent, 4)) + "%"))

if __name__ == "__main__":
    main()

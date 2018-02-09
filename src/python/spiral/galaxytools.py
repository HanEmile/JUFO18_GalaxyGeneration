# Import libraries
import math as math  # general math
import numpy as np  # advanced math

# import matplotlib.pyplot as plt  # plotting things


# class used to create galaxies
class new_galaxy(object):

    # Initialisation
    def __init__(self, galaxy_range):
        print(
            """>>> Initialising the list storing coordinates, forces and other
            values"""
        )

        # list used for storing the coordinates os the stars
        self.list_coords = []

        # list storing the overall force acting on one star
        self.list_force_star = []

        # list storing the coordinates of the midpoints of the spheres dividing
        # the galaxy into equaly big sized cells
        self.list_sphere_coords = []

        # self.list_sphere_stars = np.array(3, )

        print("\tDone\n")
        print(">>> Initialising variables and constants")

        # variable storing the number of stars generated
        self.num_of_stars = 0

        self.galaxy_range = int(galaxy_range)

        # define the universal gravitational constant
        self.G = 6.67408 * 10e11

        print("\tDone\n")

    # generate n new stars and store the coordinates in list_coords
    # n = number of stars to be generated
    # galaxy_range = size of the galaxy
    def gen_new_stars(self, n):
        print(">>> Generating Stars...")

        # for a given number of stars
        for i in range(0, n):

            # generate a temporary random coordinate inside a given range using
            # numpy
            self.temp_coord = np.random.uniform(
                low=0, high=self.galaxy_range, size=(4, ))

            # append the random coordinate to the list storing the coordinates
            self.list_coords.append(self.temp_coord)

        # increment the generated star counter
        self.num_of_stars += n
        print("\tDone")
        print("\tGenerated " + str(n) + " Stars\n")

    # print out all the coordinates in list_coords
    def print_stars(self):
        print(">>> Listing the coordinates of all stars:")
        # print the coordinates of every star
        for value in self.list_coords:
            print(value)

        print("\tDone\n")

    # calculate the forces acting between two stars on a specified axis
    # star1 = coordinates of the first star
    # star2 = coordinates of the second star
    # axes = "x", "y" or "z" (CASE SENSITIVE!)
    def calc_forces(self, star1, star2, axes):
        if axes == "x":
            mass = star1[3] * star2[3]
            distance = math.sqrt(math.pow(star1[0] - star2[0], 2))
        elif axes == "y":
            mass = star1[3] * star2[3]
            distance = math.sqrt(math.pow(star1[1] - star2[1], 2))
        elif axes == "z":
            mass = star1[3] * star2[3]
            distance = math.sqrt(math.pow(star1[2] - star2[2], 2))

        # stop division by zero
        if distance == 0:
            pass
        else:
            # return the acting force
            return self.G * mass / math.pow(distance, 2)

    # calculate all the forces acting in the current galaxy
    def calc_all_forces(self):
        print(">>> Calculating all the forces acting inbetween the stars:")

        if (self.num_of_stars <= 5):
            # print some information above the columns
            print(">>> Printing the forces acting inbetween every star")
            print("{:-<60}".format(""))
            print("\t| {:<3}| {:<3}| ".format("a", "b"))
            print("\t+{:-<4}+{:-<4}+{:-<60} ".format("", "", ""))

        else:
            print("\t[W] Too many stars to print out!")
            print("{:-<60}".format(""))

        # for every star
        for i in range(0, self.num_of_stars):

            # initialize
            self.force = 0

            # every other star:
            for j in range(0, self.num_of_stars):

                # don't calculate the force between a star and and itself
                if i != j and i < j:
                    self.arr_force = np.array((0, 0, 0))

                    # calculate the force between the two stars
                    force_x = self.calc_forces(self.list_coords[i],
                                               self.list_coords[j], "x")
                    force_y = self.calc_forces(self.list_coords[i],
                                               self.list_coords[j], "y")
                    force_z = self.calc_forces(self.list_coords[i],
                                               self.list_coords[j], "z")

                    # print("overall force: ", end="")
                    self.arr_force = np.array((force_x, force_y, force_z))

                    if (self.num_of_stars <= 5):
                        print("\t| {:<3}| {:<3}| {:<60}".format(
                            str(i), str(j), str(self.arr_force)))
                    """
                    force_x = 42
                    force_y = 36
                    force_z = 24

                    (0, 0, 0) --> (42, 36, 24)
                    """

            # append the variable to the list storing all the forces
            self.list_force_star.append(self.arr_force)

        print("{:-<60}".format(""))
        print("\tDone\n")

    # print the individual forces acting on a star
    def print_individual_forces(self, n=None, print_confirm=False):
        print(">>> Printing the individual forces acting on every star")

        if self.num_of_stars > 10:
            print("\t[W] Too many stars to print out!")
            print("{:-<60}".format(""))

            for i in range(0, 3):
                print("\t" + str(i) + " " + str(self.list_force_star[i]))

            print("\n\t...\n")

            for i in range(
                    int(len(self.list_force_star) - 3),
                    len(self.list_force_star)):
                print("\t" + str(i) + " " + str(self.list_force_star[i]))
            print("{:-<60}".format(""))

        else:
            print("{:-<60}".format(""))
            if n is None:
                # for value in self.list_force_star:
                for i in range(0, len(self.list_force_star)):
                    print("\t" + str(i) + " " + str(self.list_force_star[i]))
            else:
                print(self.list_force_star[n])

            print("{:-<60}".format(""))
            print("\tDone\n")

    # star      [x, y, z, m]
    # sphere    [x, y, z, r]
    def is_star_in_sphere(self, star, sphere):

        # define the sphere values
        self.sphere_x = sphere[0]
        self.sphere_y = sphere[1]
        self.sphere_z = sphere[2]
        self.sphere_r = sphere[3]

        # define the star coordinates
        self.star_x = star[0]
        self.star_y = star[1]
        self.star_z = star[2]

        self.sphere_x_neg = self.sphere_x - self.sphere_r
        self.sphere_x_pos = self.sphere_x + self.sphere_r

        self.sphere_y_neg = self.sphere_y - self.sphere_r
        self.sphere_y_pos = self.sphere_y + self.sphere_r

        self.sphere_z_neg = self.sphere_z - self.sphere_r
        self.sphere_z_pos = self.sphere_z + self.sphere_r

        # find out if the star is inside the sphere
        if self.sphere_x_neg < self.star_x < self.sphere_x_pos:
            if self.sphere_y_neg < self.star_y < self.sphere_y_pos:
                if self.sphere_z_neg < self.star_z < self.sphere_z_pos:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # find out which stars in in which spheres
    def is_star_in_sphere_all(self):

        # define a counter for indexing the spheres
        tmp_counter = 0

        # cycle through all the stars
        for star in self.list_coords:

            # cycle through all the spheres
            for value in self.list_sphere_coords:

                # parse the needed values from the sphere list
                sphere = np.array((value[0:4]))

                # if the star is inside the sphere
                if (self.is_star_in_sphere(star, sphere) is True):

                    # print stuff
                    print(tmp_counter, end=" ")
                    print(star, end=" ")
                    print(sphere)

                    # increment the counter
                    tmp_counter += 1

                    # break the loop to stop possible multiple assignments
                    break

    # function generating the positions of the sphere cells
    def gen_sphere_positions(self, sampling_rate):

        # calculate the distance between the midpoints of the spheres
        sphere_distance = int(round(self.galaxy_range / sampling_rate, 0))

        # define the sphere_radius
        tmp_var = math.pow(sphere_distance, 2)
        sphere_radius = math.sqrt(tmp_var + tmp_var + tmp_var)

        # define a sphere counter for "labeling" the spheres
        tmp_counter = 0

        # cycle through all potential points
        for i in range(-self.galaxy_range, self.galaxy_range, sphere_distance):
            for j in range(-self.galaxy_range, self.galaxy_range,
                           sphere_distance):
                for k in range(-self.galaxy_range, self.galaxy_range,
                               sphere_distance):

                    # generate a temporary array combining all values
                    temp_arr = np.array((i, j, k, sphere_radius, tmp_counter))

                    # append the array to the list storing the sphere infos
                    self.list_sphere_coords.append(temp_arr)

                    # increment the sphere counter
                    tmp_counter += 1

    def calc_forces_sphere():
        pass

    def calc_forces_sphere_all():
        pass

    def gen_print_forces_after_t(t):
        pass

    # def all_stars_in_sphere(self, star, se)

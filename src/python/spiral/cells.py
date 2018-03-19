#!/usr/bin/env python

import numpy as np
from numpy import genfromtxt
import json
import bpy
import time
import sys

num = 100                   # number of stars that should be generated
range_max = 10              # define the range in which the coordinates should be generated
axes = 3                    # define the number of axes
data = "galaxy"             # define the name of the galaxy
path = "cell_stars/1.csv"   # define the path where the galaxy should be saved

# generate random coordinates
# rand_a = (np.random.rand(num, axes) * 2 * rand_range) - rand_range


for i in range(0, num, 1):

    # generate the random star-coordinates
    x = np.random.uniform(-range_max, range_max, size=1)
    y = np.random.uniform(-range_max, range_max, size=1)
    z = np.random.uniform(-range_max, range_max, size=1)

    with open(path, "a") as star_data:
        x_a = str(float(x)) + ", "
        y_a = str(float(y)) + ", "
        z_a = str(float(z))

        star_data.write(x_a + y_a + z_a + "\n")

for data in path:
    verts = genfromtxt(path, delimiter=', ', skip_header=0, usecols = (0, 1, 2))

    # create mesh and object
    mesh = bpy.data.meshes.new(data)
    object = bpy.data.objects.new(data,mesh)

    # set mesh location
    object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)

    # create mesh from python data
    mesh.from_pydata(verts,[],[])
    mesh.update(calc_edges=True)

    bpy.ops.object.select_all(action='SELECT')

# parsed_json = json.loads(stars)
# print(parsed_json["s1"])
#
#
# # The Vector array contains vectors describing forces acting inside the cells.
# cell_num = 3            # number of cells
#
# vector_arr = np.zeros((cell_num, cell_num, cell_num))
#
# vector_arr[0][1][2] = Vector(1, 2, 3)
#
# print(vector_arr[0])

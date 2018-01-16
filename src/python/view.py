import bpy
from numpy import genfromtxt
import os
import sys

directory = "other_stars/"

files = [sys.argv[4] + ".csv"]

for data in files:
    path = str(directory) + str(data)
    print(path)

    verts = genfromtxt(path, delimiter=' ', skip_header=0, usecols = (0, 1, 2))

    #print(verts)

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

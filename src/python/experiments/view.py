import bpy
from numpy import genfromtxt
import os
import sys

directory = "stars/"
# # print(directory)
#
files = [sys.argv[3]]

# print("### \n\n")
#
# for data_file in os.listdir(directory):
#     files.append(data_file)
#     print(data_file)
#
# print("### \n\n")

for data in files:
    path = str(directory) + str(data)
    print(path)

    verts = genfromtxt(path, delimiter=', ', skip_header=0)

    print(verts)

# verts = [(-1.0, 1.0, 0.0), (-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (1.0, 1.0, 0.0)]

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

for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for region in area.regions:
            if region.type == 'WINDOW':
                override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
bpy.ops.view3d.view_all(override)

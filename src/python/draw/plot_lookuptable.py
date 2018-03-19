#!/usr/bin/env python3

import matplotlib.pyplot as plt

lookup_arr_a = []
lookup_arr_b = []

path = "data/2e7.csv"

print("opening data...")

with open(path) as data:
    print("opened " + path)

    lookup = data.readlines()
    for i in range(0, len(lookup)):
        lookup_arr_a.append(lookup[i].split(", ")[0])
        lookup_arr_b.append(lookup[i].split(", ")[1])

plt.plot(lookup_arr_a, lookup_arr_b)
plt.show()

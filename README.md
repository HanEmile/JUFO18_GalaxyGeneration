# JUFO18_GalaxyGeneration
__Generating Galaxies and Visualizing them using Blender.__

The Project began during my Intership at the
[ZAH](https://zah.uni-heidelberg.de/welcome/)
(Zentrum Für Astronomie der Uni Heidelberg) thank's to
[@tugi](https://github.com/tugi).

The Repo we created during that time can be found
[here](https://github.com/HanEmile/Heidelberg)

The Code is split up into two parts (03.12.17): The first part creates the
data using [Python](https://python.org) so the second part can visualize it in
[Blender](https://blender.org).

---

### Benchmarks (03.12.17)


| Nr. of stars | time |
| --- | --- |
| 1e5 | ~ 3 seconds |
| 1e6 | ~ 29 seconds |
| 1e7 | ~ 315 seconds
| 1e9 | ~ 9 hours |

##### Knockouts:
| Nr. of stars | Nr. of stars knocked out |
| --- | --- |
| 1e9 | ~ 45000 |

##### File sizes
| Filesize | Nr. of Stars |
| --- | --- |
| 1 MB | 10000 |

---

### Notes:

- lookuptable for the rho-function
- pypy

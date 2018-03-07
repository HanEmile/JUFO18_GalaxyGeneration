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

### HowTo:

- Generate the Lookup table:


    $ ./lookup <where_to_save> <nr_of_stars>

    Example:

    $ ./lookup 42 1e7


- Generate the Coordinates:


    $ ./coord <nr_of_stars> <where_to_save>

    Example

    $ ./coord.py 1000 11

- Display the Stars using Blender:


    $ blender --python view.py -- <star_data_location>

    Example

    $ blender --python view.py -- 11

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

| Name                  | Value                 |
| ---                   | ---                   |
| Time (hour min sec)   | 1:30:45               |
| Number of Stars       | 1000                  |
| Stars Kicked:         | 327718674             |
| Percent:              | 0.000305139767531221% |

##### File sizes
| Filesize | Nr. of Stars |
| --- | --- |
| 1 MB | 10000 |

---

### Notes:

- lookuptable for the rho-function
- pypy

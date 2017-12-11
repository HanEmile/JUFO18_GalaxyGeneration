# README

| Name                | Value                 |
| ---                 | ---                   |
| Time (hour min sec) | 1:30:45               |              
| Number of Stars     | 1000                  |               
| Stars Kicked:       | 327718674             |            
| Percent:            | 0.000305139767531221% |

### workflow:

---

#### Generate the lookuptable


    $ ./lookup.py <number of values> <filename>

- the __number of values__ can be given using the scientific notaion e.g. 1e7.
- the __filename__ should not overlap with any existing filename

---

#### Generate the coordinates


    $ ./coord.py <number of stars> <save_to_file_location>


#### Display the stars using Blender

    $ blender --python view.py <star_coordinates_file>

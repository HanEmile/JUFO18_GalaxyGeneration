# README

### workflow:

---

#### Generate the lookuptable


    $ ./lookup.py <number of values> <filename>

- the __number of values__ can be given using the scientific notaion e.g. 1e7.
- the __filename__ should not overlap with any existing filename

---

#### Generate the coordinates


    $ ./coord.py <number of stars>


#### Display the stars using Blender

    $ blender --python view.py

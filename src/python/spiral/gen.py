# general libraries
import numpy as np

list_a = []

class spiral:
    def __init__(self):
        self.list_a = []

    def print_list_a(self):
        for value in self.list_a:
            print(value)

    # def gen_stars(self, n, list_a)


# define a function generating n stars
def gen_stars(n, list_a):
    for i in range(0, n):
        list_a.append(np.random.random((3)))

if __name__ == "__main__":
    gen_stars(n)

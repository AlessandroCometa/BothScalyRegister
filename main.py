from random import randint
from string import ascii_uppercase as up
from itertools import *
from math import comb

#Graph generation
nodes = (up)
distances = [randint(100, 1000) for _ in range(comb(len(nodes), 2))]
links = tuple(zip(tuple(combinations(nodes, 2)), distances))
print(links)
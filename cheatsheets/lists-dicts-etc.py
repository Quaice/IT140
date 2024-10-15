# Iterables
from collections import namedtuple

# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# tuple. immutable
x = (1, 2, 3)

# tuple/sequence unpacking
# assign the vars on the left to the values in the sequence on the right.
a, b, c = x

# names tuple. immutable
# namedtuple(typename, field_names)
Vector2 = namedtuple('Vector2', ['x', 'y'])
position = Vector2(1, 2)
new_pos = [12, 25]
Vector2._make(new_pos)
pos_dict = position._asdict()

# https://docs.python.org/3/tutorial/introduction.html#lists
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# list. mutable
nums: list = [1, 2, 3, 4, 5]

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# dict. mutable
at_characters: dict = {"Finn": 13, "Jake": 35, "Princess Bubblegum:": 18, "Marcy": 1000}
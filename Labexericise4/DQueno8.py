""" Write a Python script to merge two Python dictionaries"""


d1 = {'a': 100, 'b': 500}
d2 = {'x': 300, 'y': 500}
d = d1.copy()
d.update(d2)
print(d)
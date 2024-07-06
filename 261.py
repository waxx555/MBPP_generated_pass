'''
Write a function to perform mathematical division operation across the given tuples.
'''

def division_elements(t1, t2):
    return tuple([i // j for i, j in zip(t1, t2)])


assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)

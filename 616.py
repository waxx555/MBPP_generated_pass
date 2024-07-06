'''
Write a function to perfom the modulo of tuple elements in the given two tuples.
'''

def tuple_modulo(t1, t2):
    return tuple([i % j for i, j in zip(t1, t2)])


assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

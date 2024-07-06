'''
Write a function to extract the elementwise and tuples from the given two tuples.
'''

def and_tuples(t1, t2):
    return tuple([i & j for i, j in zip(t1, t2)])


assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
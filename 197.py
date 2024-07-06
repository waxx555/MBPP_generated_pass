'''
Write a function to perform the exponentiation of the given two tuples.
'''

def find_exponentio(t1, t2):
    return tuple([i ** j for i, j in zip(t1, t2)])


assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
assert find_exponentio((11, 5, 6, 7), (6, 7, 8, 6)) == (1771561, 78125, 1679616, 117649)
assert find_exponentio((12, 6, 7, 8), (7, 8, 9, 7)) == (35831808, 1679616, 40353607, 2097152)

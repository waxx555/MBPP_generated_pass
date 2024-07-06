'''
Write a function to repeat the given tuple n times.
'''

def repeat_tuples(tup, n):
    return (tup,) * n


assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
assert repeat_tuples((1, 2), 3) == ((1, 2), (1, 2), (1, 2))
assert repeat_tuples((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))

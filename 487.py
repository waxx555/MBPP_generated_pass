'''
Write a function to sort a list of tuples in increasing order by the last element in each tuple.
'''

def sort_tuple(tuples):
    return sorted(tuples, key=lambda x: x[-1])


assert sort_tuple([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]
assert sort_tuple([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]
assert sort_tuple([(3, 9), (6, 7), (4, 3)] ) == [(4, 3), (6, 7), (3, 9)]

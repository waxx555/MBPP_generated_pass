'''
Write a function to remove all tuples with all none values in the given tuple list.
'''

def remove_tuple(tup):
    return str([i for i in tup if not all(j == None for j in i)])


assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'
assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'
assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'

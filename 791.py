'''
Write a function to remove the nested record from the given tuple.
'''

def remove_nested(t):
    return tuple([x for x in t if type(x) != tuple])


assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)

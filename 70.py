'''
Write a function to find whether all the given tuples have equal length or not.
'''

def get_equal(tuples, n):
    for i in tuples:
        if len(i) != n:
            return 'All tuples do not have same length'
    return 'All tuples have same length'


assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
assert get_equal([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
assert get_equal([(1, 2), (3, 4)], 2) == 'All tuples have same length'

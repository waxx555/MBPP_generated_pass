'''
Write a function to find the minimum difference in the tuple pairs of given tuples.
'''

def min_difference(lst):
    return min([abs(i-j) for i, j in lst])


assert min_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 1
assert min_difference([(4, 6), (12, 8), (11, 4), (2, 13)]) == 2
assert min_difference([(5, 17), (3, 9), (12, 5), (3, 24)]) == 6

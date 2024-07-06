'''
Write a function to find the maximum difference between available pairs in the given tuple list.
'''

def max_difference(lst):
    return max(max(a)-min(a) for a in lst)


assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

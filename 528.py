'''
Write a function to find the list of lists with minimum length.
'''

def min_length(lst):
    return min([(len(i), i) for i in lst])


assert min_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
assert min_length([[1], [5, 7], [10, 12, 14,15]])==(1, [1])
assert min_length([[5], [15,20,25]])==(1, [5])

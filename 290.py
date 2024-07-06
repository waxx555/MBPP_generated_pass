'''
Write a function to find the list of lists with maximum length.
'''

def max_length(lst):
    return max([(len(i),i) for i in lst])


assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
assert max_length([[5], [15,20,25]])==(3, [15,20,25])
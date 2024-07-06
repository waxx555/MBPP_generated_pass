'''
Write a function to find the maximum of similar indices in two lists of tuples.
'''

def max_similar_indices(l1, l2):
    return [max(i) for i in zip(l1, l2)]


assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]
assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]

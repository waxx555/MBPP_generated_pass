'''
Write a function to find the maximum product from the pairs of tuples within a given list.
'''

def max_product_tuple(lst):
    return max([i[0]*i[1] for i in lst])


assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484

'''
Write a function to find the minimum product from the pairs of tuples within a given list.
'''


def min_product_tuple(lst):
    return min([x*y for x,y in lst])


assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100

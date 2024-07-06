'''
Write a python function to calculate the product of all the numbers of a given tuple.
'''

def mutiple_tuple(tup):
    result = 1
    for i in tup:
        result *= i
    return result


assert mutiple_tuple((4, 3, 2, 2, -1, 18)) == -864
assert mutiple_tuple((1,2,3)) == 6
assert mutiple_tuple((-2,-4,-6)) == -48

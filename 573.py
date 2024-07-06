'''
Write a python function to calculate the product of the unique numbers of a given list.
'''

def unique_product(lst):
    product = 1
    for i in set(lst):
        product *= i
    return product


assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
assert unique_product([1, 2, 3, 1,]) == 6
assert unique_product([7, 8, 9, 0, 1, 1]) == 0

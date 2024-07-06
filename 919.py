'''
Write a python function to multiply all items in the list.
'''

def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result


assert multiply_list([1,-2,3]) == -6
assert multiply_list([1,2,3,4]) == 24
assert multiply_list([3,1,2,3]) == 18

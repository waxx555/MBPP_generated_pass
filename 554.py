'''
Write a python function to find odd numbers from a mixed list.
'''

def Split(lst):
    return [i for i in lst if i % 2 != 0]


assert Split([1,2,3,4,5,6]) == [1,3,5]
assert Split([10,11,12,13]) == [11,13]
assert Split([7,8,9,1]) == [7,9,1]

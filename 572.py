'''
Write a python function to remove two duplicate numbers from a given number of lists.
'''

def two_unique_nums(lst):
    return [i for i in lst if lst.count(i) == 1]


assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

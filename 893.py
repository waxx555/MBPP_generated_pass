'''
Write a python function to get the last element of each sublist.
'''

def Extract(lst):
    return [i[-1] for i in lst]


assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']
assert Extract([[1, 2, 3], [4, 5]]) == [3, 5]

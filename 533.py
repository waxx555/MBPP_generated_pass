'''
Write a function to remove particular data type elements from the given tuple.
'''

def remove_datatype(t, dt):
    return [i for i in t if type(i) != dt]


assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
assert remove_datatype((7, 8, 9, "SR"), str) == [7, 8, 9]
assert remove_datatype((7, 1.1, 2, 2.2), float) == [7, 2]

'''
Write a python function to find the first even number in a given list of numbers.
'''

def first_even(lst):
    for i in lst:
        if i % 2 == 0:
            return i
    return None


assert first_even ([1, 3, 5, 7, 4, 1, 6, 8]) == 4
assert first_even([2, 3, 4]) == 2
assert first_even([5, 6, 7]) == 6

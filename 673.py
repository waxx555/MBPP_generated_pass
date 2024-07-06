'''
Write a python function to convert a list of multiple integers into a single integer.
'''

def convert(lst):
    return int(''.join(map(str,lst)))


assert convert([1,2,3]) == 123
assert convert([4,5,6]) == 456
assert convert([7,8,9]) == 789

'''
Write a function to substract the contents of one tuple with corresponding index of other tuple.
'''

def substract_elements(t1, t2):
    return tuple([i - j for i, j in zip(t1, t2)])


assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)

'''
Write a function to substract the elements of the given nested tuples.
'''

def substract_elements(t1, t2):
    return tuple((a[0]-b[0], a[1]-b[1]) for a, b in zip(t1, t2))

assert substract_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((-5, -4), (1, -4), (1, 8), (-6, 7))
assert substract_elements(((13, 4), (14, 6), (13, 10), (12, 11)), ((19, 8), (14, 10), (12, 2), (18, 4))) == ((-6, -4), (0, -4), (1, 8), (-6, 7))
assert substract_elements(((19, 5), (18, 7), (19, 11), (17, 12)), ((12, 9), (17, 11), (13, 3), (19, 5))) == ((7, -4), (1, -4), (6, 8), (-2, 7))

'''
Write a function to convert the given tuple to a floating-point number.
'''

def tuple_to_float(t):
    return float(str(t[0]) + '.' + str(t[1]))

assert tuple_to_float((4, 56)) == 4.56
assert tuple_to_float((7, 256)) == 7.256
assert tuple_to_float((8, 123)) == 8.123

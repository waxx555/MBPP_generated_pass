'''
Write a function to convert the given binary number to its decimal equivalent.
'''

def binary_to_decimal(n):
    return int(str(n), 2)



assert binary_to_decimal(100) == 4
assert binary_to_decimal(1011) == 11
assert binary_to_decimal(1101101) == 109

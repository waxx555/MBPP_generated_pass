'''
Write a function to convert the given binary tuple to integer.
'''

def binary_to_integer(binary):
    return str(int(''.join(map(str, binary)), 2))


assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
assert binary_to_integer((0, 1, 1, 0, 0, 1, 0, 1)) == '101'
assert binary_to_integer((1, 1, 0, 1, 0, 1)) == '53'

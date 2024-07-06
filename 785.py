'''
Write a function to convert tuple string to integer tuple.
'''

def tuple_str_int(s):
    return tuple(map(int, s[1:-1].split(', ')))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)

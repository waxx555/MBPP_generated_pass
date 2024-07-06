'''
Write a function to concatenate each element of tuple by the delimiter.
'''

def concatenate_tuple(t):
    return '-'.join(map(str,t))


assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

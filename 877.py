'''
Write a python function to sort the given string.
'''

def sort_String(s):
    return ''.join(sorted(s))


assert sort_String("cba") == "abc"
assert sort_String("data") == "aadt"
assert sort_String("zxy") == "xyz"

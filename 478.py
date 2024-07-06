'''
Write a function to remove lowercase substrings from a given string.
'''

def remove_lowercase(s):
    return ''.join([i for i in s if i.isupper()])


assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG')

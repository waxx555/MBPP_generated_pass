'''
Write a function to check for a number at the end of a string.
'''

import re

def end_num(s):
    return bool(re.match(r'^.*\d$', s))


assert end_num('abcdef')==False
assert end_num('abcdef7')==True
assert end_num('abc')==False

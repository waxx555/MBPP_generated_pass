'''
Write a function to check that the given string contains only a certain set of characters(in this case a-z, a-z and 0-9) by using regex.
'''

import re

def is_allowed_specific_char(s):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    s = charRe.search(s)
    return not bool(s)


assert is_allowed_specific_char("ABCDEFabcdef123450") == True
assert is_allowed_specific_char("*&%@#!}{") == False
assert is_allowed_specific_char("HELLOhowareyou98765") == True

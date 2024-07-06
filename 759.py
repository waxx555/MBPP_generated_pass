'''
Write a function to check a decimal with a precision of 2.
'''

import re

def is_decimal(num):
    return bool(re.match(r'^\d+\.\d{2}$', num))


assert is_decimal('123.11')==True
assert is_decimal('e666.86')==False
assert is_decimal('3.124587')==False

'''
Write a function to check the given decimal with a precision of 2 by using regex.
'''

import re

def is_decimal(num):
    return bool(re.match(r'^\d+\.\d{2}$', num))



assert is_decimal('123.11') == True
assert is_decimal('0.21') == True
assert is_decimal('123.1214') == False

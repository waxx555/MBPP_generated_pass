'''
Write a function to check whether the given string is starting with a vowel or not using regex.
'''

import re

def check_str(s):
    return 'Valid' if re.match(r'^[aeiouAEIOU]', s) else 'Invalid'


assert check_str("annie") == 'Valid'
assert check_str("dawood") == 'Invalid'
assert check_str("Else") == 'Valid'

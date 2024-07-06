'''
Write a function to remove multiple spaces in a string by using regex.
'''

import re

def remove_multiple_spaces(s):
    return re.sub(r'\s+', ' ', s)


assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
assert remove_multiple_spaces('Quad      Core') == 'Quad Core'
assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'

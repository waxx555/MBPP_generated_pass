'''
Write a function to search some literals strings in a string by using regex.
'''

import re

def check_literals(s,literals):
    for i in literals:
        if re.search(i,s):
            return 'Matched!'
    return 'Not Matched!'


assert check_literals('The quick brown fox jumps over the lazy dog.',['fox']) == 'Matched!'
assert check_literals('The quick brown fox jumps over the lazy dog.',['horse']) == 'Not Matched!'
assert check_literals('The quick brown fox jumps over the lazy dog.',['lazy']) == 'Matched!'

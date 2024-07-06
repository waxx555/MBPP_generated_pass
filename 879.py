'''
Write a function that matches a string that has an 'a' followed by anything, ending in 'b' by using regex.
'''

import re

def text_match(s):
    return re.search(r'a.*b$', s) and 'Found a match!' or 'Not matched!'


assert text_match("aabbbbd") == 'Not matched!'
assert text_match("aabAbbbc") == 'Not matched!'
assert text_match("accddbbjjjb") == 'Found a match!'

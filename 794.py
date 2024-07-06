'''
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
'''

import re

def text_starta_endb(s):
    return re.search(r'^a.*b$', s) and 'Found a match!' or 'Not matched!'


assert text_starta_endb("aabbbb")==('Found a match!')
assert text_starta_endb("aabAbbbc")==('Not matched!')
assert text_starta_endb("accddbbjjj")==('Not matched!')

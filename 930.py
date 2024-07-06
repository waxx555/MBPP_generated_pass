'''
Write a function that matches a string that has an a followed by zero or more b's by using regex.
'''

import re

def text_match(txt):
    pattern = 'ab*'
    if re.search(pattern, txt):
        return 'Found a match!'
    else:
        return 'Not matched!'
    

assert text_match("msb") == 'Not matched!'
assert text_match("a0c") == 'Found a match!'
assert text_match("abbc") == 'Found a match!'

'''
Write a function to check if the given string starts with a substring using regex.
'''

import re

def check_substring(s, sub):
    if re.match(sub, s):
        return 'string starts with the given substring'
    return 'string doesnt start with the given substring'


assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'
assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'

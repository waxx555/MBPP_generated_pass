'''
Write a function to remove multiple spaces in a string.
'''

import re

def remove_spaces(s):
    return re.sub(' +', ' ', s)


assert remove_spaces('python  program')==('python program')
assert remove_spaces('python   programming    language')==('python programming language')
assert remove_spaces('python                     program')==('python program')

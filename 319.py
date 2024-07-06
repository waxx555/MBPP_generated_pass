'''
Write a function to find all five characters long word in the given string by using regex.
'''

import re

def find_long_word(s):
    return re.findall(r'\b\w{5}\b', s)


assert find_long_word('Please move back to strem') == ['strem']
assert find_long_word('4K Ultra HD streaming player') == ['Ultra']
assert find_long_word('Streaming Media Player') == ['Media']

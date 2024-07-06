'''
Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs by using regex.
'''

import re

def find_literals(s, pattern):
    match = re.search(pattern, s)
    if match:
        return (pattern, match.start(), match.end())
    return None


assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)

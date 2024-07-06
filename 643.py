'''
Write a function that matches a word containing 'z', not at the start or end of the word.
'''

import re

def text_match_wordz_middle(s):
    return re.search(r'\Bz\B', s) and 'Found a match!' or 'Not matched!'


assert text_match_wordz_middle("pythonzabc.")==('Found a match!')
assert text_match_wordz_middle("xyzabc.")==('Found a match!')
assert text_match_wordz_middle("  lang  .")==('Not matched!')

'''
Write a function to put spaces between words starting with capital letters in a given string by using regex.
'''

import re

def capital_words_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()


assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

'''
Write a function to replace whitespaces with an underscore and vice versa in a given string by using regex.
'''

import re

def replace_spaces(s):
    return re.sub(r'\s', '_', s)


assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('The Avengers') == 'The_Avengers'
assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

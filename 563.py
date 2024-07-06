'''
Write a function to extract values between quotation marks of a string.
'''

import re

def extract_values(s):
    return re.findall(r'"(.*?)"', s)


assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
assert extract_values('"python","program","language"')==['python','program','language']
assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']

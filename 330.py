'''
Write a function to find all three, four, five characters long words in the given string by using regex.
'''

import re

def find_char(s):
    return re.findall(r'\b\w{3,5}\b', s)


assert find_char('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']
assert find_char('Certain service are subject to change MSR') == ['are', 'MSR']
assert find_char('Third party legal desclaimers') == ['Third', 'party', 'legal']

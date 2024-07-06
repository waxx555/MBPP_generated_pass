'''
Write a function to extract the maximum numeric value from a string by using regex.
'''

import re

def extract_max(s):
    return max(map(int, re.findall(r'\d+', s)))


assert extract_max('100klh564abc365bg') == 564
assert extract_max('hello300how546mer231') == 546
assert extract_max('its233beenalong343journey234') == 343

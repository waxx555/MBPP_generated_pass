'''
Write a function to remove all whitespaces from the given string using regex.
'''

import re

def remove_whitespaces(s):
    return re.sub(r'\s+', '', s)


assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

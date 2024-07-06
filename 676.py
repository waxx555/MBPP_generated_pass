'''
Write a function to remove everything except alphanumeric characters from the given string by using regex.
'''

import re

def remove_extra_char(s):
    return re.sub(r'\W', '', s)


assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'
assert remove_extra_char('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'
assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'

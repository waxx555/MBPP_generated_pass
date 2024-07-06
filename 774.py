'''
Write a function to check if the string is a valid email address or not using regex.
'''

import re

def check_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return 'Valid Email'
    return 'Invalid Email'


assert check_email("ankitrai326@gmail.com") == 'Valid Email'
assert check_email("my.ownsite@ourearth.org") == 'Valid Email'
assert check_email("ankitaoie326.com") == 'Invalid Email'

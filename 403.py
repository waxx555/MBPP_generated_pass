'''
Write a function to check if a url is valid or not using regex.
'''

import re

def is_valid_URL(url):
    return bool(re.match(r'^https?://(www\.)?([a-zA-Z0-9-]+)\.([a-z]+)$', url))


assert is_valid_URL("https://www.google.com") == True
assert is_valid_URL("https:/www.gmail.com") == False
assert is_valid_URL("https:// www.redit.com") == False

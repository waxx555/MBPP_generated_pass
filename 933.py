'''
Write a function to convert camel case string to snake case string by using regex.
'''

import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


assert camel_to_snake('GoogleAssistant') == 'google_assistant'
assert camel_to_snake('ChromeCast') == 'chrome_cast'
assert camel_to_snake('QuadCore') == 'quad_core'

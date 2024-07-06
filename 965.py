'''
Write a function to convert camel case string to snake case string.
'''

import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


assert camel_to_snake('PythonProgram')==('python_program')
assert camel_to_snake('pythonLanguage')==('python_language')
assert camel_to_snake('ProgrammingLanguage')==('programming_language')

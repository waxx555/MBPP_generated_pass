'''
Write a function to convert snake case string to camel case string.
'''

def snake_to_camel(string):
    return ''.join([i.capitalize() for i in string.split('_')])


assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('python_language')==('PythonLanguage')
assert snake_to_camel('programming_language')==('ProgrammingLanguage')

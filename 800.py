'''
Write a function to remove all whitespaces from a string.
'''

def remove_all_spaces(s):
    return s.replace(' ', '')


assert remove_all_spaces('python  program')==('pythonprogram')
assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
assert remove_all_spaces('python                     program')==('pythonprogram')

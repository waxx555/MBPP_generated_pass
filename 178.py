'''
Write a function to search some literals strings in a string.
'''

def string_literals(literals,s):
    for i in literals:
        if i in s:
            return 'Matched!'
    return 'Not Matched!'


assert string_literals(['language'],'python language')==('Matched!')
assert string_literals(['program'],'python language')==('Not Matched!')
assert string_literals(['python'],'programming language')==('Not Matched!')

'''
Write a function to check whether a given string has a capital letter, a lower case letter, a number and specified length using lambda function.
'''
def check_string(s):
    errors = []
    check_string = [lambda s: [f'String must have 1 upper case character.'] if not any(x.isupper() for x in s) else None,
                lambda s: [f'String must have 1 lower case character.'] if not any(x.islower() for x in s) else None,
                lambda s: [f'String must have 1 number.'] if not any(x.isdigit() for x in s) else None,
                lambda s: [f'String length should be atleast 8.'] if len(s) < 8 else None]
    for f in check_string:
        if f(s):
            errors.extend(f(s))
    return errors or ['Valid string.']

assert check_string('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']
assert check_string('123python')==['String must have 1 upper case character.']
assert check_string('123Python')==['Valid string.']

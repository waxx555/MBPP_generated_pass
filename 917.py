'''
Write a function to find the sequences of one upper case letter followed by lower case letters.
'''

def text_uppercase_lowercase(txt):
    import re
    if re.search(r'[A-Z][a-z]+', txt):
        return 'Found a match!'
    else:
        return 'Not matched!'
    

assert text_uppercase_lowercase("AaBbGg")==('Found a match!')
assert text_uppercase_lowercase("aA")==('Not matched!')
assert text_uppercase_lowercase("PYTHON")==('Not matched!')

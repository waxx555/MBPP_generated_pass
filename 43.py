'''
Write a function to find sequences of lowercase letters joined with an underscore using regex.
'''

def text_match(text):
    import re
    if re.search(r'^[a-z]+_[a-z]+$',text):
        return ('Found a match!')
    else:
        return ('Not matched!')
    


assert text_match("aab_cbbbc") == 'Found a match!'
assert text_match("aab_Abbbc") == 'Not matched!'
assert text_match("Aaab_abbbc") == 'Not matched!'

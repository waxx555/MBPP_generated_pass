'''
Write a function to find sequences of lowercase letters joined with an underscore.
'''

def text_lowercase_underscore(text):
    import re
    if re.search(r'^[a-z]+_[a-z]+$',text):
        return ('Found a match!')
    else:
        return ('Not matched!')
    


assert text_lowercase_underscore("aab_cbbbc")==('Found a match!')
assert text_lowercase_underscore("aab_Abbbc")==('Not matched!')
assert text_lowercase_underscore("Aaab_abbbc")==('Not matched!')

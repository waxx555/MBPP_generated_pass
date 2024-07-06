'''
Write a function to find maximum run of uppercase characters in the given string.
'''

def max_run_uppercase(s):
    max_run = 0
    run = 0
    for i in s:
        if i.isupper():
            run += 1
            max_run = max(max_run, run)
        else:
            run = 0
    return max_run


assert max_run_uppercase('GeMKSForGERksISBESt') == 5
assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
assert max_run_uppercase('GooGLEFluTTER') == 4

'''
Write a python function to convert the given string to lower case.
'''

def is_lower(s):
    return s.lower()


assert is_lower("InValid") == "invalid"
assert is_lower("TruE") == "true"
assert is_lower("SenTenCE") == "sentence"

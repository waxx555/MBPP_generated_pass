'''
Write a python function to check whether the given string is a binary string or not.
'''

def check(s):
    for i in s:
        if i not in "01":
            return "No"
    return "Yes"


assert check("01010101010") == "Yes"
assert check("name0") == "No"
assert check("101") == "Yes"

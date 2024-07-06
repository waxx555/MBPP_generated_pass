'''
Write a python function to check whether the hexadecimal number is even or odd.
'''

def even_or_odd(s):
    return "Even" if int(s,16)%2==0 else "Odd"


assert even_or_odd("AB3454D") =="Odd"
assert even_or_odd("ABC") == "Even"
assert even_or_odd("AAD") == "Odd"

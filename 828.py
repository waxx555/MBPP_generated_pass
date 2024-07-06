'''
Write a function to count alphabets,digits and special charactes in a given string.
'''

def count_alpha_dig_spl(s):
    alpha = 0
    digit = 0
    spl = 0
    for i in s:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        else:
            spl += 1
    return alpha, digit, spl


assert count_alpha_dig_spl("abc!@#123")==(3,3,3)
assert count_alpha_dig_spl("dgsuy@#$%&1255")==(5,4,5)
assert count_alpha_dig_spl("fjdsif627348#%$^&")==(6,6,5)

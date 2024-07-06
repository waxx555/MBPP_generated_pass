'''
Write a function to convert a roman numeral to an integer.
'''

def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    n = roman[s[-1]]
    for i in range(len(s)-1, 0, -1):
        if roman[s[i]] > roman[s[i-1]]:
            n -= roman[s[i-1]]
        else:
            n += roman[s[i-1]]
    return n


assert roman_to_int('MMMCMLXXXVI')==3986
assert roman_to_int('MMMM')==4000
assert roman_to_int('C')==100

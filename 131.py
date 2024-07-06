'''
Write a python function to reverse only the vowels of a given string.
'''

def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)


assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"

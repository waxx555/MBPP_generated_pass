'''
Write a python function to check whether the two given strings are isomorphic to each other or not.
'''

def is_Isomorphic(s, t):
    if len(s) != len(t):
        return False
    d1, d2 = {}, {}
    for i in range(len(s)):
        if s[i] in d1 and d1[s[i]] != t[i]:
            return False
        if t[i] in d2 and d2[t[i]] != s[i]:
            return False
        d1[s[i]] = t[i]
        d2[t[i]] = s[i]
    return True


assert is_Isomorphic("paper","title") == True
assert is_Isomorphic("ab","ba") == True
assert is_Isomorphic("ab","aa") == False

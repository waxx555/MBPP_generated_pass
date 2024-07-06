'''
Write a function to check if the two given strings are permutations of each other.
'''

def check_permutation(s1, s2):
    return sorted(s1) == sorted(s2)


assert check_permutation("abc", "cba") == True
assert check_permutation("test", "ttew") == False
assert check_permutation("xxyz", "yxzx") == True

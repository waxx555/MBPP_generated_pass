'''
Write a python function to count all the substrings starting and ending with same characters.
'''

def count_Substring_With_Equal_Ends(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if s[i]==s[j]:
                count += 1
    return count




assert count_Substring_With_Equal_Ends("abc") == 3
assert count_Substring_With_Equal_Ends("abcda") == 6
assert count_Substring_With_Equal_Ends("ab") == 2

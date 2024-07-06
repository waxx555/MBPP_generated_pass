'''
Write a python function to count the number of substrings with same first and last characters.
'''

def count_Substring_With_Equal_Ends(s):
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i] == s[j]:
                count += 1
    return count


assert count_Substring_With_Equal_Ends('aba') == 4
assert count_Substring_With_Equal_Ends('abcab') == 7
assert count_Substring_With_Equal_Ends('abc') == 3

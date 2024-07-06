'''
Write a python function to find the minimum number of swaps required to convert one binary string to another.
'''

def min_Swaps(s1, s2):
    if s1.count('1') != s2.count('1'):
        return "Not Possible"
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count // 2


assert min_Swaps("1101","1110") == 1
assert min_Swaps("1111","0100") == "Not Possible"
assert min_Swaps("1110000","0001101") == 3

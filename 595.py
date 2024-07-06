'''
Write a python function to count minimum number of swaps required to convert one binary string to another.
'''

def min_Swaps(s1,s2):
    if s1.count("1") != s2.count("1"):
        return "Not Possible"
    return sum([1 for i in range(len(s1)) if s1[i] != s2[i]])//2


assert min_Swaps("1101","1110") == 1
assert min_Swaps("111","000") == "Not Possible"
assert min_Swaps("111","110") == "Not Possible"

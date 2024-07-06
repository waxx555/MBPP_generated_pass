'''
Write a python function to find the count of rotations of a binary string with odd value.
'''

def odd_Equivalent(s,n):
    count = 0
    for i in range(n):
        if s[i] == '1':
            count += 1
    return count


assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("11011",5) == 4
assert odd_Equivalent("1010",4) == 2

'''
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
'''

def find_length(s, n):
    count = 0
    max_diff = 0
    for i in range(n):
        count = count + 1 if s[i] == '0' else count - 1
        if count < 0:
            count = 0
        max_diff = max(max_diff, count)
    return max_diff


assert find_length("11000010001", 11) == 6
assert find_length("10111", 5) == 1
assert find_length("11011101100101", 14) == 2 

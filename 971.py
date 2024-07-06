'''
Write a function to find the maximum number of segments of lengths a, b and c that can be formed from n.
'''

def maximum_segments(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = max(maximum_segments(n-a, a, b, c), maximum_segments(n-b, a, b, c), maximum_segments(n-c, a, b, c))
    if res == -1:
        return -1
    return res + 1


assert maximum_segments(7, 5, 2, 5) == 2
assert maximum_segments(17, 2, 1, 3) == 17
assert maximum_segments(18, 16, 3, 6) == 6

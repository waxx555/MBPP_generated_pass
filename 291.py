'''
Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.
'''

def count_no_of_ways(n, k):
    total = k
    same = 0
    diff = k
    for i in range(2, n + 1):
        same = diff
        diff = total * (k - 1)
        total = same + diff
    return total


assert count_no_of_ways(2, 4) == 16
assert count_no_of_ways(3, 2) == 6
assert count_no_of_ways(4, 4) == 228

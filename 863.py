'''
Write a function to find the length of the longest sub-sequence such that elements in the subsequences are consecutive integers.
'''

def find_longest_conseq_subseq(lst, n):
    s = set(lst)
    ans = 0
    for i in range(n):
        if lst[i]-1 not in s:
            j = lst[i]
            while j in s:
                j += 1
            ans = max(ans, j-lst[i])
    return ans


assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
assert find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7) == 4
assert find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5

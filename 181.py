'''
Write a function to find the longest common prefix in the given set of strings.
'''

def common_prefix(s, n):
    s.sort()
    a = s[0]
    b = s[n-1]
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += a[i]
        else:
            break
    return res


assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
assert common_prefix(["apples", "ape", "april"], 3) == 'ap'
assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'

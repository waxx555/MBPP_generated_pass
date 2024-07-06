'''
Write a function to create the next bigger number by rearranging the digits of a given number.
'''

def rearrange_bigger(n):
    n = list(str(n))
    i = len(n) - 2
    while i >= 0 and n[i] >= n[i+1]:
        i -= 1
    if i == -1:
        return False
    j = len(n) - 1
    while n[j] <= n[i]:
        j -= 1
    n[i], n[j] = n[j], n[i]
    n[i+1:] = n[i+1:][::-1]
    return int("".join(n))


assert rearrange_bigger(12)==21
assert rearrange_bigger(10)==False
assert rearrange_bigger(102)==120

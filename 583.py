'''
Write a function for nth catalan number.
'''

def catalan_number(n):
    if n == 0:
        return 1
    num = 1
    for i in range(1, n + 1):
        num = num * (n + i) // i
    return num // (n + 1)


assert catalan_number(10)==16796
assert catalan_number(9)==4862
assert catalan_number(7)==429

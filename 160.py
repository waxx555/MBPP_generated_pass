'''
Write a function to find x and y that satisfies ax + by = n.
'''

def solution(a, b, n):
    for x in range(n//a+1):
        y = (n - a*x) / b
        if y.is_integer():
            return ('x = ', x, ', y = ', int(y))
    return 'No solution'


assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
assert solution(4, 2, 7) == 'No solution'
assert solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)

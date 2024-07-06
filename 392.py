'''
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
'''

def get_max_sum(n):
    if n == 0:
        return 0
    return max(n, get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5))


assert get_max_sum(60) == 106
assert get_max_sum(10) == 12
assert get_max_sum(2) == 2

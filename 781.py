'''
Write a python function to check whether the count of divisors is even or odd.
'''

def count_Divisors(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return "Even" if cnt % 2 == 0 else "Odd"


assert count_Divisors(10) == "Even"
assert count_Divisors(100) == "Odd"
assert count_Divisors(125) == "Even"

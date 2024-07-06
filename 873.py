'''
Write a function to solve the fibonacci sequence using recursion.
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34

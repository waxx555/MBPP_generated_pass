'''
Write a python function to find the kth element in an array containing odd elements first and then even elements.
'''

def get_Number(n, k):
    if k <= n//2:
        return 2*k-1
    return 2*(k-n//2)


assert get_Number(8,5) == 2
assert get_Number(7,2) == 3
assert get_Number(5,2) == 3

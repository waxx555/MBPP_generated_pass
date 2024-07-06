'''
Write a function to find the lcm of the given array elements.
'''

def get_lcm(arr):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    lcm = arr[0]
    for i in range(1, len(arr)):
        gcd_val = gcd(lcm, arr[i])
        lcm = (lcm * arr[i]) // gcd_val
    return lcm


assert get_lcm([2, 7, 3, 9, 4]) == 252
assert get_lcm([1, 2, 8, 3]) == 24
assert get_lcm([3, 8, 4, 10, 5]) == 120

'''
Write a function to find the gcd of the given array elements.
'''

def get_gcd(arr):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result



assert get_gcd([2, 4, 6, 8, 16]) == 2
assert get_gcd([1, 2, 3]) == 1
assert get_gcd([2, 4, 6, 8]) == 2 

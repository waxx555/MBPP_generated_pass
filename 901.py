'''
Write a function to find the smallest multiple of the first n numbers.
'''

def smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    res = 1
    for i in range(2, n+1):
        res = lcm(res, i)
    return res


assert smallest_multiple(13)==360360
assert smallest_multiple(2)==2
assert smallest_multiple(1)==1
